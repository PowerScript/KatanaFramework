#!/usr/bin/env python

__author__ = "Gawen Arab"
__copyright__ = "Copyright 2012, Gawen Arab"
__credits__ = ["Gawen Arab"]
__license__ = "MIT"
__version__ = "1.0.3"
__maintainer__ = "Gawen Arab"
__email__ = "g@wenarab.com"
__status__ = "Production"

# Snippet from http://code.activestate.com/recipes/146306/
import httplib, mimetypes
import urlparse
import urllib
import urllib2
import hashlib
import json
import time
import re
import logging
import threading

logger = logging.getLogger("virustotal")

FILE_SIZE_LIMIT = 30 * 1024 * 1024   # 30MB

class postfile:
    @staticmethod
    def post_multipart(host, selector, fields, files):
        """
        Post fields and files to an http host as multipart/form-data.
        fields is a sequence of (name, value) elements for regular form fields.
        files is a sequence of (name, filename, value) elements for data to be uploaded as files
        Return the server's response page.
        """
        content_type, body = postfile.encode_multipart_formdata(fields, files)
        h = httplib.HTTPS(host)
        h.putrequest('POST', selector)
        h.putheader('content-type', content_type)
        h.putheader('content-length', str(len(body)))
        h.endheaders()
        h.send(body)
        errcode, errmsg, headers = h.getreply()
    
        return h.file.read()

    @staticmethod
    def encode_multipart_formdata(fields, files):
        """
        fields is a sequence of (name, value) elements for regular form fields.
        files is a sequence of (name, filename, value) elements for data to be uploaded as files
        Return (content_type, body) ready for httplib.HTTP instance
        """
        BOUNDARY = '----------ThIs_Is_tHe_bouNdaRY_$'
        CRLF = '\r\n'
        L = []
        for (key, value) in fields:
            L.append('--' + BOUNDARY)
            L.append('Content-Disposition: form-data; name="%s"' % key)
            L.append('')
            L.append(value)
        for (key, filename, value) in files:
            L.append('--' + BOUNDARY)
            L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filename))
            L.append('Content-Type: %s' % postfile.get_content_type(filename))
            L.append('')
            L.append(value)
        L.append('--' + BOUNDARY + '--')
        L.append('')
        body = CRLF.join((bytes(i) for i in L))
        content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
        
        return content_type, body

    @staticmethod
    def get_content_type(filename):
        return mimetypes.guess_type(filename)[0] or 'application/octet-stream'

class VirusTotal(object):
    _SCAN_ID_RE = re.compile(r"^[a-fA-F0-9]{64}-[0-9]{10}$")

    class EntityTooLarge(Exception):
        pass

    class ApiError(Exception):
        pass

    def __init__(self, api_key, limit_per_min = None):
        limit_per_min = limit_per_min if limit_per_min is not None else 4

        super(VirusTotal, self).__init__()

        self.api_key = api_key
        self.limit_per_min = limit_per_min
        self.limits = []
        self.limit_lock = threading.Lock()

    def __repr__(self):
        return "<VirusTotal proxy>"

    def _limit_call_handler(self):
        with self.limit_lock:
            if self.limit_per_min <= 0:
                return

            now = time.time()
            self.limits = [l for l in self.limits if l > now]
            self.limits.append(now + 60)
            
            if len(self.limits) >= self.limit_per_min:
                wait = self.limits[0] - now
                logger.info("Wait for %.2fs because of quotat limit." % (self.limits[0] - now, ))
                time.sleep(self.limits[0] - now)
            
    @classmethod
    def _fileobj_to_fcontent(cls, anything, filename = None):
        # anything can be:
        # - A MD5, SHA1, SHA256
        # - A scan id
        # - A filepath or URL
        # - A file object

        if isinstance(anything, basestring):
            # Is MD5, SHA1, SHA256?
            if all(i in "1234567890abcdef" for i in anything.lower()) and len(anything) in [32, 40, 64]:
                return ["resource", anything, filename]

            if cls._SCAN_ID_RE.match(anything):
                return ["resource", anything, filename]

            # Is URL ?
            if urlparse.urlparse(anything).scheme:
                fh = urllib2.urlopen(anything)

            else:
                # it's file
                fh = file(anything, "rb")

            with fh as f:
                return cls._fileobj_to_fcontent(f)

        assert hasattr(anything, "read")

        content = anything.read()

        if hasattr(anything, "name") and isinstance(anything.name, basestring):
            filename = anything.name

        return ["file", filename, content]

    def get(self, anything, filename = None):
        logger.info("Get report of %r" % (anything, ))
        o = self._fileobj_to_fcontent(anything, filename)

        if o[0] == "file":
            o = (
                "resource",
                hashlib.sha256(o[2]).hexdigest(),
                o[2],
            )

        data = urllib.urlencode({
            "apikey": self.api_key,
            "resource": o[1],
        })

        self._limit_call_handler()
        req = urllib2.urlopen(urllib2.Request(
           "http://www.virustotal.com/vtapi/v2/file/report",
            data,
        )).read()

        report = Report(req, self)

        return report
    
    def scan(self, anything, filename = None, reanalyze = None):
        reanalyze = reanalyze if reanalyze is not None else False
        
        if not reanalyze:
            # Check if already exists
            report = self.get(anything, filename)

            if report is not None:
                return report

        logger.info("Analyze %r" % (anything, ))
        o = self._fileobj_to_fcontent(anything, filename)

        assert o[0] == "file"

        if o[1] is None:
            o[1] = "file"

        if len(o[2]) > FILE_SIZE_LIMIT:
            raise self.EntityTooLarge()

        self._limit_call_handler()
        ret_json = postfile.post_multipart(
            host = "www.virustotal.com",
            selector = "https://www.virustotal.com/vtapi/v2/file/scan",
            fields = {
                "apikey": self.api_key,
            }.items(),
            files = [
                o,
            ],
        )

        report = Report(ret_json, self)
        
        if report:
            report.update()

        return report

class Report(object):
    def __new__(cls, r, parent):
        if isinstance(r, basestring):
            try:
                r = json.loads(r)

            except ValueError:
                raise VirusTotal.ApiError()

        assert isinstance(r, dict)
        
        if r["response_code"] == 0:
            return None

        self = super(Report, cls).__new__(cls)
        self.parent = parent

        self.update(r)

        return self

    def update(self, data = None):
        data = data if data is not None else self.parent.get(self.scan_id)._report
        self._report = data

    def __getattr__(self, attr):
        # Aliases
        item = {
            "id": "resource",
            "status": "verbose_msg",
        }.get(attr, attr)

        try:
            return self._report[item]

        except KeyError:
            raise AttributeError(attr)

    def __repr__(self):
        return "<VirusTotal report %s (%s)>" % (
            self.id,
            self.status,
        )

    @property
    def state(self):
        return {
            -2: "analyzing",
            1: "ok",
            0: "ko",
        }.get(self.response_code, "unknown")

    @property
    def done(self):
        return self.state == "ok"

    def __iter__(self):
        for antivirus, report in self.scans.iteritems():
            yield (
                (antivirus, report["version"], report["update"]),
                report["result"],
            )

    def join(self, timeout = None, interval = None):
        interval = interval if interval is not None else 60
        if timeout is not None:
            timeout = time.time() + timeout

        self.update()
        while self.state != "ok" and (timeout is None or time.time() < timeout):
            time.sleep(interval)
            self.update()

def main():
    import sys
    import optparse
    import threading
    import Queue
    import glob

    parser = optparse.OptionParser(usage = """%prog [-k API_KEY] (scan|get) RESOURCE ...
'scan' asks virustotal to scan the file, even if a report
  is available. The resource must be a file.

'get' asks virustotal if a report is available for the given
  resource.

A resource can be:
- a hash (md5, sha1, sha256)
- a scan ID
- a filepath or URL""")
    parser.add_option("-k", "--key", dest = "api_key", default = None, help = "Set VirusTotal API key.")
    parser.add_option("-l", "--limit", dest = "limit_per_min", default = "4", help = "Set limit per minute API call. VirusTotal specifies no more 4 API calls must be done per minute. You can change this value, but VirusTotal maybe ignores some calls and may make this script bug.")
    parser.add_option("-v", "--verbose", dest = "verbose", action = "store_true", default = False, help = "Verbose.")
    (options, arguments) = parser.parse_args()

    logging.getLogger().setLevel(logging.DEBUG if options.verbose else logging.WARNING)
    logging.basicConfig()

    # This is my API key. Please use it only for examples, not for any production stuff
    # You can get an API key signing-up on VirusTotal. It takes 2min.
    API_KEY = "22c6d056f1e99b8fb4fa6c2a811178723735e9840de18fa2df83fccfd21c95a0"

    api_key = options.api_key or API_KEY

    if len(sys.argv) < 3:
        parser.print_usage()
        return -1
    
    action = arguments.pop(0)

    if action.lower() not in ("scan", "get", ):
        print "ERROR: unknown action"
        return -1

    resources = []
    for argument in arguments:
        for resource in glob.glob(argument):
            resources.append(resource)

    v = VirusTotal(API_KEY, limit_per_min = int(options.limit_per_min))

    q = Queue.Queue()
    def analyze(resource):
        try:
            if action.lower() == "scan":
                report = v.scan(resource, reanalyze = True)
                print "%s: Scan started: %s" % (resource, report, )
                report.join()
                q.put((resource, report))
                print "%s: Scan finished: %s" % (resource, report, )

            elif action.lower() == "get":
                report = v.get(resource)
                q.put((resource, report))
        
        except VirusTotal.ApiError:
            print "VirusTotal returned a non correct response. It may be because the script does too many requests at the minute. See the parameter -l"

    threads = []
    for resource in resources:
        thread = threading.Thread(target = analyze, args = (resource, ))
        threads.append(thread)

        thread.daemon = True
        thread.start()

    for thread in threads:
        while thread.is_alive():
            try:
                thread.join(0.1)

            except KeyboardInterrupt:
                return

    while not q.empty():
        resource, report = q.get()
        
        print "=== %s ===" % (resource, )

        if report is None:
            print "No report is available."
            return 0

        print "Report:"
        for antivirus, virus in report:
            print "- %s (%s, %s):\t%s" % (antivirus[0], antivirus[1], antivirus[2], virus, )

        print

if __name__ == "__main__":
    main()
