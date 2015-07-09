import re
import sys
import os
import subprocess
import socket
from parser import WhoisEntry
from whois import NICClient


def whois(url, experimental=False):
    # clean domain to expose netloc
    ip_match = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", url)
    if ip_match:
        domain = url
    else:
        domain = extract_domain(url)
    if not experimental:
        try:
            # try native whois command first
            r = subprocess.Popen(['whois', domain], stdout=subprocess.PIPE)
            text = r.stdout.read()
        except OSError:
            # try experimental client
            nic_client = NICClient()
            text = nic_client.whois_lookup(None, domain, 0)
    else:
        nic_client = NICClient()
        text = nic_client.whois_lookup(None, domain, 0)
    return WhoisEntry.load(domain, text)


def extract_domain(url):
    """Extract the domain from the given URL

    >>> extract_domain('http://www.google.com.au/tos.html')
    'google.com.au'
    >>> extract_domain('http://blog.webscraping.com')
    'webscraping.com'
    >>> extract_domain('www.bbc.co.uk')
    'bbc.co.uk'
    >>> extract_domain('198.252.206.140')
    'stackoverflow.com'
    >>> extract_domain('102.112.2O7.net')
    '2o7.net'
    >>> extract_domain('1-0-1-1-1-0-1-1-1-1-1-1-1-.0-0-0-0-0-0-0-0-0-0-0-0-0-10-0-0-0-0-0-0-0-0-0-0-0-0-0.info')
    '0-0-0-0-0-0-0-0-0-0-0-0-0-10-0-0-0-0-0-0-0-0-0-0-0-0-0.info'
    """
    if re.match(r'\d+\.\d+\.\d+\.\d+', url):
        # this is an IP address
        return socket.gethostbyaddr(url)[0]

    tlds_path = os.path.join(os.getcwd(), os.path.dirname(__file__), 'data', 'tlds.txt')
    suffixes = [
        line.lower().strip()
        for line in open(tlds_path).readlines()
        if not line.startswith('#')
    ]

    if type(url) is not unicode:
        url = url.decode('utf-8')
    url = re.sub('^.*://', '', url.encode('idna')).split('/')[0].lower()
    domain = []

    for section in url.split('.'):
        if section in suffixes:
            domain.append(section)
        else:
            domain = [section]
    return '.'.join(domain).decode('idna').encode('utf-8')


if __name__ == '__main__':
    try:
        url = sys.argv[1]
    except IndexError:
        print('Usage: %s url' % sys.argv[0])
    else:
        print(whois(url))
