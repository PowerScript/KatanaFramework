# -*- coding: utf-8 -*-

# parser.py - Module for parsing whois response data
# Copyright (c) 2008 Andrey Petrov
#
# This module is part of pywhois and is released under
# the MIT license: http://www.opensource.org/licenses/mit-license.php

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from future import standard_library
standard_library.install_aliases()
from builtins import *
from builtins import str
from past.builtins import basestring

import json
from datetime import datetime
import re
try:
    import dateutil.parser as dp
    from .time_zones import tz_data
    DATEUTIL = True
except ImportError:
    DATEUTIL = False

EMAIL_REGEX = "[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"

KNOWN_FORMATS = [
    '%d-%b-%Y', 				# 02-jan-2000
    '%Y-%m-%d', 				# 2000-01-02
    '%d.%m.%Y', 				# 2.1.2000
    '%Y.%m.%d',                 # 2000.01.02
    '%Y/%m/%d',                 # 2000/01/02
    '%d/%m/%Y',                 # 02/01/2013
    '%Y. %m. %d.',              # 2000. 01. 02.
    '%Y.%m.%d %H:%M:%S',        # 2014.03.08 10:28:24
    '%d-%b-%Y %H:%M:%S %Z',		# 24-Jul-2009 13:20:03 UTC
    '%a %b %d %H:%M:%S %Z %Y',  # Tue Jun 21 23:59:59 GMT 2011
    '%Y-%m-%dT%H:%M:%SZ',       # 2007-01-26T19:10:31Z
    '%Y-%m-%dT%H:%M:%S%z',      # 2013-12-06T08:17:22-0800
    '%Y-%m-%d %H:%M:%SZ',       # 2000-08-22 18:55:20Z
    '%Y-%m-%d %H:%M:%S',        # 2000-08-22 18:55:20
    '%d %b %Y %H:%M:%S',        # 08 Apr 2013 05:44:00
    '%d/%m/%Y %H:%M:%S',     # 23/04/2015 12:00:07 EEST
    '%d/%m/%Y %H:%M:%S %Z',     # 23/04/2015 12:00:07 EEST
    '%d/%m/%Y %H:%M:%S.%f %Z',  # 23/04/2015 12:00:07.619546 EEST
    '%B %d %Y',                 # August 14 2017
]


class PywhoisError(Exception):
    pass


def datetime_parse(s):
    for known_format in KNOWN_FORMATS:
        try:
            s = datetime.strptime(s, known_format)
            break
        except ValueError as e:
            pass  # Wrong format, keep trying
    return s

def cast_date(s, dayfirst=False, yearfirst=False):
    """Convert any date string found in WHOIS to a datetime object.
    """
    if DATEUTIL:
        try:
            return dp.parse(
                s,
                tzinfos=tz_data,
                dayfirst=dayfirst,
                yearfirst=yearfirst
            ).replace(tzinfo=None)
        except Exception:
            return datetime_parse(s)
    else:
        return datetime_parse(s)


class WhoisEntry(dict):
    """Base class for parsing a Whois entries.
    """
    # regular expressions to extract domain data from whois profile
    # child classes will override this
    _regex = {
        'domain_name':          'Domain Name: *(.+)',
        'registrar':            'Registrar: *(.+)',
        'whois_server':         'Whois Server: *(.+)',
        'referral_url':         'Referral URL: *(.+)',  # http url of whois_server
        'updated_date':         'Updated Date: *(.+)',
        'creation_date':        'Creation Date: *(.+)',
        'expiration_date':      'Expir\w+ Date: *(.+)',
        'name_servers':         'Name Server: *(.+)',  # list of name servers
        'status':               'Status: *(.+)',  # list of statuses
        'emails':               EMAIL_REGEX,  # list of email s
        'dnssec':               'dnssec: *([\S]+)',
        'name':                 'Registrant Name: *(.+)',
        'org':                  'Registrant\s*Organization: *(.+)',
        'address':              'Registrant Street: *(.+)',
        'city':                 'Registrant City: *(.+)',
        'state':                'Registrant State/Province: *(.+)',
        'zipcode':              'Registrant Postal Code: *(.+)',
        'country':              'Registrant Country: *(.+)',
    }
    dayfirst = False
    yearfirst = False

    def __init__(self, domain, text, regex=None):
        if 'This TLD has no whois server, but you can access the whois database at' in text:
            raise PywhoisError(text)
        else:
            self.domain = domain
            self.text = text
            if regex is not None:
                self._regex = regex
            self.parse()

    def parse(self):
        """The first time an attribute is called it will be calculated here.
        The attribute is then set to be accessed directly by subsequent calls.
        """
        for attr, regex in list(self._regex.items()):
            if regex:
                values = []
                for data in re.findall(regex, self.text, re.IGNORECASE):
                    matches = data if isinstance(data, tuple) else [data]
                    for value in matches:
                        value = value.strip()
                        if value and isinstance(value, basestring) and not value.isdigit() and '_date' in attr:
                            # try casting to date format
                            value = cast_date(
                                value,
                                dayfirst=self.dayfirst,
                                yearfirst=self.yearfirst)
                        if value and value not in values:
                            # avoid duplicates
                            values.append(value)
                if values and attr in ('registrar', 'whois_server', 'referral_url'):
                    values = values[-1] # ignore junk
                if len(values) == 1:
                    values = values[0]
                elif not values:
                    values = None

                self[attr] = values


    def __setitem__(self, name, value):
        super(WhoisEntry, self).__setitem__(name, value)


    def __getattr__(self, name):
        return self.get(name)


    def __str__(self):
        handler = lambda e: str(e)
        return json.dumps(self, indent=2, default=handler)

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__ = state

    @staticmethod
    def load(domain, text):
        """Given whois output in ``text``, return an instance of ``WhoisEntry``
        that represents its parsed contents.
        """
        if text.strip() == 'No whois server is known for this kind of object.':
            raise PywhoisError(text)

        if domain.endswith('.com'):
            return WhoisCom(domain, text)
        elif domain.endswith('.net'):
            return WhoisNet(domain, text)
        elif domain.endswith('.org'):
            return WhoisOrg(domain, text)
        elif domain.endswith('.name'):
            return WhoisName(domain, text)
        elif domain.endswith('.me'):
            return WhoisMe(domain, text)
        elif domain.endswith('.au'):
            return WhoisAU(domain, text)
        elif domain.endswith('.ru'):
            return WhoisRu(domain, text)
        elif domain.endswith('.us'):
            return WhoisUs(domain, text)
        elif domain.endswith('.uk'):
            return WhoisUk(domain, text)
        elif domain.endswith('.fr'):
            return WhoisFr(domain, text)
        elif domain.endswith('.nl'):
            return WhoisNl(domain, text)
        elif domain.endswith('.fi'):
            return WhoisFi(domain, text)
        elif domain.endswith('.jp'):
            return WhoisJp(domain, text)
        elif domain.endswith('.pl'):
            return WhoisPl(domain, text)
        elif domain.endswith('.br'):
            return WhoisBr(domain, text)
        elif domain.endswith('.eu'):
            return WhoisEu(domain, text)
        elif domain.endswith('.ee'):
            return WhoisEe(domain, text)
        elif domain.endswith('.kr'):
            return WhoisKr(domain, text)
        elif domain.endswith('.pt'):
            return WhoisPt(domain, text)
        elif domain.endswith('.bg'):
            return WhoisBg(domain, text)
        elif domain.endswith('.de'):
            return WhoisDe(domain, text)
        elif domain.endswith('.at'):
            return WhoisAt(domain, text)
        elif domain.endswith('.ca'):
            return WhoisCa(domain, text)
        elif domain.endswith('.be'):
            return WhoisBe(domain, text)
        elif domain.endswith('.рф'):
            return WhoisRf(domain, text)
        elif domain.endswith('.info'):
            return WhoisInfo(domain, text)
        elif domain.endswith('.su'):
            return WhoisSu(domain, text)
        elif domain.endswith('.kg'):
            return WhoisKg(domain, text)
        elif domain.endswith('.io'):
            return WhoisIo(domain, text)
        elif domain.endswith('.biz'):
            return WhoisBiz(domain, text)
        elif domain.endswith('.mobi'):
            return WhoisMobi(domain, text)
        elif domain.endswith('.ch'):
            return WhoisChLi(domain, text)
        elif domain.endswith('.li'):
            return WhoisChLi(domain, text)
        elif domain.endswith('.id'):
            return WhoisID(domain, text)
        elif domain.endswith('.sk'):
            return WhoisSK(domain, text)
        elif domain.endswith('.se'):
            return WhoisSe(domain, text)
        elif domain.endswith('.nu'):
            return WhoisSe(domain, text)
        elif domain.endswith('.is'):
            return WhoisIs(domain, text)
        else:
            return WhoisEntry(domain, text)


class WhoisCom(WhoisEntry):
    """Whois parser for .com domains
    """
    def __init__(self, domain, text):
        if 'No match for "' in text:
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text)


class WhoisNet(WhoisEntry):
    """Whois parser for .net domains
    """
    def __init__(self, domain, text):
        if 'No match for "' in text:
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text)


class WhoisOrg(WhoisEntry):
    """Whois parser for .org domains
    """
    regex = {
        'domain_name':      'Domain Name: *(.+)',
        'registrar':        'Registrar: *(.+)',
        'whois_server':     'Whois Server: *(.+)', # empty usually
        'referral_url':     'Referral URL: *(.+)', # http url of whois_server: empty usually
        'updated_date':     'Updated Date: *(.+)',
        'creation_date':    'Creation Date: *(.+)',
        'expiration_date':  'Registry Expiry Date: *(.+)',
        'name_servers':     'Name Server: *(.+)', # list of name servers
        'status':           'Status: *(.+)', # list of statuses
        'emails':           EMAIL_REGEX, # list of email addresses
    }

    def __init__(self, domain, text):
        if text.strip() == 'NOT FOUND':
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text)


class WhoisRu(WhoisEntry):
    """Whois parser for .ru domains
    """
    regex = {
        'domain_name': 'domain: *(.+)',
        'registrar': 'registrar: *(.+)',
        'creation_date': 'created: *(.+)',
        'expiration_date': 'paid-till: *(.+)',
        'name_servers': 'nserver: *(.+)',  # list of name servers
        'status': 'state: *(.+)',  # list of statuses
        'emails': EMAIL_REGEX,  # list of email addresses
        'org': 'org: *(.+)'
    }

    def __init__(self, domain, text):
        if text.strip() == 'No entries found':
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisNl(WhoisEntry):
    """Whois parser for .nl domains
    """
    regex = {
        'name': None,
        'address': None,
        'zip_code': None,
        'city': None,
        'country': None
    }

    def __init__(self, domain, text):
        if text.endswith('is free'):
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)

        match = re.compile('Registrar:(.*?)DNSSEC', re.DOTALL).search(text)
        if match:
            lines = [line.strip() for line in match.groups()[0].strip().splitlines()]
            self['name'] = lines[0]
            self['address'] = lines[1]
            if len(lines) == 4:
                self['zip_code'], _, self['city'] = lines[2].partition(' ')
            self['country'] = lines[-1]



class WhoisName(WhoisEntry):
    """Whois parser for .name domains
    """
    regex = {
        'domain_name_id':  'Domain Name ID: *(.+)',
        'domain_name':     'Domain Name: *(.+)',
        'registrar_id':    'Sponsoring Registrar ID: *(.+)',
        'registrar':       'Sponsoring Registrar: *(.+)',
        'registrant_id':   'Registrant ID: *(.+)',
        'admin_id':        'Admin ID: *(.+)',
        'technical_id':    'Tech ID: *(.+)',
        'billing_id':      'Billing ID: *(.+)',
        'creation_date':   'Created On: *(.+)',
        'expiration_date': 'Expires On: *(.+)',
        'updated_date':    'Updated On: *(.+)',
        'name_server_ids': 'Name Server ID: *(.+)',  # list of name server ids
        'name_servers':    'Name Server: *(.+)',  # list of name servers
        'status':          'Domain Status: *(.+)',  # list of statuses
    }

    def __init__(self, domain, text):
        if 'No match for ' in text:
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisUs(WhoisEntry):
    """Whois parser for .us domains
    """
    regex = {
        'domain_name':                    'Domain Name: *(.+)',
        'domain__id':                     'Domain ID: *(.+)',
        'registrar':                      'Sponsoring Registrar: *(.+)',
        'registrar_id':                   'Sponsoring Registrar IANA ID: *(.+)',
        'registrar_url':                  'Registrar URL \(registration services\): *(.+)',
        'status':                         'Domain Status: *(.+)',  # list of statuses
        'registrant_id':                  'Registrant ID: *(.+)',
        'registrant_name':                'Registrant Name: *(.+)',
        'registrant_address1':            'Registrant Address1: *(.+)',
        'registrant_address2':            'Registrant Address2: *(.+)',
        'registrant_city':                'Registrant City: *(.+)',
        'registrant_state_province':      'Registrant State/Province: *(.+)',
        'registrant_postal_code':         'Registrant Postal Code: *(.+)',
        'registrant_country':             'Registrant Country: *(.+)',
        'registrant_country_code':        'Registrant Country Code: *(.+)',
        'registrant_phone_number':        'Registrant Phone Number: *(.+)',
        'registrant_email':               'Registrant Email: *(.+)',
        'registrant_application_purpose': 'Registrant Application Purpose: *(.+)',
        'registrant_nexus_category':      'Registrant Nexus Category: *(.+)',
        'admin_id':                       'Administrative Contact ID: *(.+)',
        'admin_name':                     'Administrative Contact Name: *(.+)',
        'admin_address1':                 'Administrative Contact Address1: *(.+)',
        'admin_address2':                 'Administrative Contact Address2: *(.+)',
        'admin_city':                     'Administrative Contact City: *(.+)',
        'admin_state_province':           'Administrative Contact State/Province: *(.+)',
        'admin_postal_code':              'Administrative Contact Postal Code: *(.+)',
        'admin_country':                  'Administrative Contact Country: *(.+)',
        'admin_country_code':             'Administrative Contact Country Code: *(.+)',
        'admin_phone_number':             'Administrative Contact Phone Number: *(.+)',
        'admin_email':                    'Administrative Contact Email: *(.+)',
        'admin_application_purpose':      'Administrative Application Purpose: *(.+)',
        'admin_nexus_category':           'Administrative Nexus Category: *(.+)',
        'billing_id':                     'Billing Contact ID: *(.+)',
        'billing_name':                   'Billing Contact Name: *(.+)',
        'billing_address1':               'Billing Contact Address1: *(.+)',
        'billing_address2':               'Billing Contact Address2: *(.+)',
        'billing_city':                   'Billing Contact City: *(.+)',
        'billing_state_province':         'Billing Contact State/Province: *(.+)',
        'billing_postal_code':            'Billing Contact Postal Code: *(.+)',
        'billing_country':                'Billing Contact Country: *(.+)',
        'billing_country_code':           'Billing Contact Country Code: *(.+)',
        'billing_phone_number':           'Billing Contact Phone Number: *(.+)',
        'billing_email':                  'Billing Contact Email: *(.+)',
        'billing_application_purpose':    'Billing Application Purpose: *(.+)',
        'billing_nexus_category':         'Billing Nexus Category: *(.+)',
        'tech_id':                        'Technical Contact ID: *(.+)',
        'tech_name':                      'Technical Contact Name: *(.+)',
        'tech_address1':                  'Technical Contact Address1: *(.+)',
        'tech_address2':                  'Technical Contact Address2: *(.+)',
        'tech_city':                      'Technical Contact City: *(.+)',
        'tech_state_province':            'Technical Contact State/Province: *(.+)',
        'tech_postal_code':               'Technical Contact Postal Code: *(.+)',
        'tech_country':                   'Technical Contact Country: *(.+)',
        'tech_country_code':              'Technical Contact Country Code: *(.+)',
        'tech_phone_number':              'Technical Contact Phone Number: *(.+)',
        'tech_email':                     'Technical Contact Email: *(.+)',
        'tech_application_purpose':       'Technical Application Purpose: *(.+)',
        'tech_nexus_category':            'Technical Nexus Category: *(.+)',
        'name_servers':                   'Name Server: *(.+)',  # list of name servers
        'created_by_registrar':           'Created by Registrar: *(.+)',
        'last_updated_by_registrar':      'Last Updated by Registrar: *(.+)',
        'creation_date':                  'Domain Registration Date: *(.+)',
        'expiration_date':                'Domain Expiration Date: *(.+)',
        'updated_date':                   'Domain Last Updated Date: *(.+)',
    }

    def __init__(self, domain, text):
        if 'Not found:' in text:
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisPl(WhoisEntry):
    """Whois parser for .pl domains
    """
    regex = {
        'domain_name':                    'DOMAIN NAME: *(.+)\n',
        'registrar':                      'REGISTRAR:\n\s*(.+)',
        'registrar_url':                  'URL: *(.+)',        # not available
        'status':                         'Registration status:\n\s*(.+)',  # not available
        'registrant_name':                'Registrant:\n\s*(.+)',   # not available
        'creation_date':                  'created: *(.+)\n',
        'expiration_date':                'renewal date: *(.+)',
        'updated_date':                   'last modified: *(.+)\n',
    }

    def __init__(self, domain, text):
        if 'No information available about domain name' in text:
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisCa(WhoisEntry):
    """Whois parser for .ca domains
    """
    regex = {
        'domain_name':                    'Domain name: *(.+)',
        'registrant_name':                '(?<!Domain) Name: *(.+)',
        'registrant_number':              'Number: *(.+)\n',
        'domain_status':                  'Domain status: *(.+)',
        'emails':                         'Email: *(.+)',
        'updated_date':                   'Updated Date: *(.+)',
        'creation_date':                  'Creation Date: *(.+)',
        'expiration_date':                'Expiry Date: *(.+)',
        'phone':                          'Phone: *(.+)',
        'fax':                            'Fax: *(.+)',
        'dnssec':                         'dnssec: *([\S]+)'
    }

    def __init__(self, domain, text):
        if 'Domain status:         available' in text:
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisMe(WhoisEntry):
    """Whois parser for .me domains
    """
    regex = {
        'domain_id':                   'Domain ID:(.+)',
        'domain_name':                 'Domain Name:(.+)',
        'creation_date':               'Domain Create Date:(.+)',
        'updated_date':                'Domain Last Updated Date:(.+)',
        'expiration_date':             'Domain Expiration Date:(.+)',
        'transfer_date':               'Last Transferred Date:(.+)',
        'trademark_name':              'Trademark Name:(.+)',
        'trademark_country':           'Trademark Country:(.+)',
        'trademark_number':            'Trademark Number:(.+)',
        'trademark_application_date':  'Date Trademark Applied For:(.+)',
        'trademark_registration_date': 'Date Trademark Registered:(.+)',
        'registrar':                   'Sponsoring Registrar:(.+)',
        'created_by':                  'Created by:(.+)',
        'updated_by':                  'Last Updated by Registrar:(.+)',
        'status':                      'Domain Status:(.+)',  # list of statuses
        'registrant_id':               'Registrant ID:(.+)',
        'registrant_name':             'Registrant Name:(.+)',
        'registrant_org':              'Registrant Organization:(.+)',
        'registrant_address':          'Registrant Address:(.+)',
        'registrant_address2':         'Registrant Address2:(.+)',
        'registrant_address3':         'Registrant Address3:(.+)',
        'registrant_city':             'Registrant City:(.+)',
        'registrant_state_province':   'Registrant State/Province:(.+)',
        'registrant_country':          'Registrant Country/Economy:(.+)',
        'registrant_postal_code':      'Registrant Postal Code:(.+)',
        'registrant_phone':            'Registrant Phone:(.+)',
        'registrant_phone_ext':        'Registrant Phone Ext\.:(.+)',
        'registrant_fax':              'Registrant FAX:(.+)',
        'registrant_fax_ext':          'Registrant FAX Ext\.:(.+)',
        'registrant_email':            'Registrant E-mail:(.+)',
        'admin_id':                    'Admin ID:(.+)',
        'admin_name':                  'Admin Name:(.+)',
        'admin_org':                   'Admin Organization:(.+)',
        'admin_address':               'Admin Address:(.+)',
        'admin_address2':              'Admin Address2:(.+)',
        'admin_address3':              'Admin Address3:(.+)',
        'admin_city':                  'Admin City:(.+)',
        'admin_state_province':        'Admin State/Province:(.+)',
        'admin_country':               'Admin Country/Economy:(.+)',
        'admin_postal_code':           'Admin Postal Code:(.+)',
        'admin_phone':                 'Admin Phone:(.+)',
        'admin_phone_ext':             'Admin Phone Ext\.:(.+)',
        'admin_fax':                   'Admin FAX:(.+)',
        'admin_fax_ext':               'Admin FAX Ext\.:(.+)',
        'admin_email':                 'Admin E-mail:(.+)',
        'tech_id':                     'Tech ID:(.+)',
        'tech_name':                   'Tech Name:(.+)',
        'tech_org':                    'Tech Organization:(.+)',
        'tech_address':                'Tech Address:(.+)',
        'tech_address2':               'Tech Address2:(.+)',
        'tech_address3':               'Tech Address3:(.+)',
        'tech_city':                   'Tech City:(.+)',
        'tech_state_province':         'Tech State/Province:(.+)',
        'tech_country':                'Tech Country/Economy:(.+)',
        'tech_postal_code':            'Tech Postal Code:(.+)',
        'tech_phone':                  'Tech Phone:(.+)',
        'tech_phone_ext':              'Tech Phone Ext\.:(.+)',
        'tech_fax':                    'Tech FAX:(.+)',
        'tech_fax_ext':                'Tech FAX Ext\.:(.+)',
        'tech_email':                  'Tech E-mail:(.+)',
        'name_servers':                'Nameservers:(.+)',  # list of name servers
    }

    def __init__(self, domain, text):
        if 'NOT FOUND' in text:
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisUk(WhoisEntry):
    """Whois parser for .uk domains
    """
    regex = {
        'domain_name':                    'Domain name:\n\s*(.+)',
        'registrar':                      'Registrar:\n\s*(.+)',
        'registrar_url':                  'URL: *(.+)',
        'status':                         'Registration status:\n\s*(.+)',  # list of statuses
        'registrant_name':                'Registrant:\n\s*(.+)',
        'creation_date':                  'Registered on: *(.+)',
        'expiration_date':                'Expiry date: *(.+)',
        'updated_date':                   'Last updated: *(.+)',
        'name_servers':                   'Name servers: *(.+)',
    }

    def __init__(self, domain, text):
        if 'No match for ' in text:
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisFr(WhoisEntry):
    """Whois parser for .fr domains
    """
    regex = {
        'domain_name': 'domain: *(.+)',
        'registrar': 'registrar: *(.+)',
        'creation_date': 'created: *(.+)',
        'expiration_date': 'Expir\w+ Date:\s?(.+)',
        'name_servers': 'nserver: *(.+)',  # list of name servers
        'status': 'status: *(.+)',  # list of statuses
        'emails': EMAIL_REGEX,  # list of email addresses
        'updated_date': 'last-update: *(.+)',
    }

    def __init__(self, domain, text):
        if 'No entries found' in text:
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisFi(WhoisEntry):
    """Whois parser for .fi domains
    """
    regex = {
        'domain_name':                    'domain\.*: *([\S]+)',
        'name':                           'descr\.*: *([\S\ ]+)',
        'address':                        'address\.*: *([\S\ ]+)',
        'phone':                          'phone\.*: *([\S\ ]+)',
        'status':                         'status\.*: *([\S]+)',  # list of statuses
        'creation_date':                  'created\.*: *([\S]+)',
        'updated_date':                   'modified\.*: *([\S]+)',
        'expiration_date':                'expires\.*: *([\S]+)',
        'name_servers':                   'nserver\.*: *([\S]+) \[\S+\]',  # list of name servers
        'name_server_statuses':           'nserver\.*: *([\S]+) \[\S+\]',  # list of name servers and statuses
        'dnssec':                         'dnssec\.*: *([\S]+)',

    }

    def __init__(self, domain, text):
        if 'Domain not ' in text:
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisJp(WhoisEntry):
    """Whois parser for .jp domains
    """
    regex = {
        'domain_name': 'a\. \[Domain Name\]\s*(.+)',
        'registrant_org': 'g\. \[Organization\](.+)',
        'creation_date': r'\[Registered Date\]\s*(.+)',
        'name_servers': 'p\. \[Name Server\]\s*(.+)',  # list of name servers
        'updated_date':  '\[Last Update\]\s?(.+)',
        'status': '\[State\]\s*(.+)',  # list of statuses
    }

    def __init__(self, domain, text):
        if 'No match!!' in text:
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisAU(WhoisEntry):
    """Whois parser for .au domains
    """
    regex = {
        'domain_name':                    'Domain Name: *(.+)\n',
        'last_modified':			      'Last Modified: *(.+)\n',
        'registrar':                      'Registrar Name: *(.+)\n',
        'status':                         'Status: *(.+)',
        'registrant_name':                'Registrant: *(.+)',
        'name_servers':                   'Name Server: *(.+)',
    }

    def __init__(self, domain, text):
        if text.strip() == 'No Data Found':
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisEu(WhoisEntry):
    """Whois parser for .eu domains
    """
    regex = {
        'domain_name': r'Domain: *([^\n\r]+)',
        'tech_name': r'Technical: *Name: *([^\n\r]+)',
        'tech_org': r'Technical: *Name: *[^\n\r]+\s*Organisation: *([^\n\r]+)',
        'tech_phone': r'Technical: *Name: *[^\n\r]+\s*Organisation: *[^\n\r]+\s*Language: *[^\n\r]+\s*Phone: *([^\n\r]+)',
        'tech_fax': r'Technical: *Name: *[^\n\r]+\s*Organisation: *[^\n\r]+\s*Language: *[^\n\r]+\s*Phone: *[^\n\r]+\s*Fax: *([^\n\r]+)',
        'tech_email': r'Technical: *Name: *[^\n\r]+\s*Organisation: *[^\n\r]+\s*Language: *[^\n\r]+\s*Phone: *[^\n\r]+\s*Fax: *[^\n\r]+\s*Email: *([^\n\r]+)',
        'registrar': r'Registrar: *Name: *([^\n\r]+)',
        'name_servers': r'Name servers: *([^\n\r]+)\s*([^\n\r]*)',  # list of name servers
    }

    def __init__(self, domain, text):
        if text.strip() == 'Status: AVAILABLE':
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisEe(WhoisEntry):
    """Whois parser for .ee domains
    """
    regex = {
        'domain_name': r'Domain: *[\n\r]+\s*name: *([^\n\r]+)',
        'status': r'Domain: *[\n\r]+\s*name: *[^\n\r]+\sstatus: *([^\n\r]+)',
        'registered': r'Domain: *[\n\r]+\s*name: *[^\n\r]+\sstatus: *[^\n\r]+\sregistered: *([^\n\r]+)',
        'changed': r'Domain: *[\n\r]+\s*name: *[^\n\r]+\sstatus: *[^\n\r]+\sregistered: *[^\n\r]+\schanged: *([^\n\r]+)',
        'expire': r'Domain: *[\n\r]+\s*name: *[^\n\r]+\sstatus: *[^\n\r]+\sregistered: *[^\n\r]+\schanged: *[^\n\r]+\sexpire: *([^\n\r]+)',

        # 'tech_name': r'Technical: *Name: *([^\n\r]+)',
        # 'tech_org': r'Technical: *Name: *[^\n\r]+\s*Organisation: *([^\n\r]+)',
        # 'tech_phone': r'Technical: *Name: *[^\n\r]+\s*Organisation: *[^\n\r]+\s*Language: *[^\n\r]+\s*Phone: *([^\n\r]+)',
        # 'tech_fax': r'Technical: *Name: *[^\n\r]+\s*Organisation: *[^\n\r]+\s*Language: *[^\n\r]+\s*Phone: *[^\n\r]+\s*Fax: *([^\n\r]+)',
        # 'tech_email': r'Technical: *Name: *[^\n\r]+\s*Organisation: *[^\n\r]+\s*Language: *[^\n\r]+\s*Phone: *[^\n\r]+\s*Fax: *[^\n\r]+\s*Email: *([^\n\r]+)',
        'registrar': r'Registrar: *[\n\r]+\s*name: *([^\n\r]+)',
        'name_servers': r'nserver: *(.*)',  # list of name servers
    }

    def __init__(self, domain, text):
        if text.strip() == 'Domain not found':
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisBr(WhoisEntry):
    """Whois parser for .br domains
    """
    regex = {
        'domain':                        'domain: *(.+)\n',
        'owner':                         'owner: *([\S ]+)',
        'ownerid':                       'ownerid: *(.+)',
        'country':                       'country: *(.+)',
        'owner_c':                       'owner-c: *(.+)',
        'admin_c':                       'admin-c: *(.+)',
        'tech_c':                        'tech-c: *(.+)',
        'billing_c':                     'billing-c: *(.+)',
        'nserver':                       'nserver: *(.+)',
        'nsstat':                        'nsstat: *(.+)',
        'nslastaa':                      'nslastaa: *(.+)',
        'saci':                          'saci: *(.+)',
        'created':                       'created: *(.+)',
        'expires':                       'expires: *(.+)',
        'changed':                       'changed: *(.+)',
        'status':                        'status: *(.+)',
        'nic_hdl_br':                    'nic-hdl-br: *(.+)',
        'person':                        'person: *([\S ]+)',
        'email':                         'e-mail: *(.+)',
    }

    def __init__(self, domain, text):

        if 'Not found:' in text:
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisKr(WhoisEntry):
    """Whois parser for .kr domains
    """
    regex = {
        'domain_name': 'Domain Name\s*: *(.+)',
        'registrant_org': 'Registrant\s*: *(.+)',
        'registrant_address': 'Registrant Address\s*: *(.+)',
        'registrant_zip': 'Registrant Zip Code\s*: *(.+)',
        'admin_name': 'Administrative Contact\(AC\)\s*: *(.+)',
        'admin_email': 'AC E-Mail\s*: *(.+)',
        'admin_phone': 'AC Phone Number\s*: *(.+)',
        'creation_date': 'Registered Date\s*: *(.+)',
        'updated_date':  'Last updated Date\s*: *(.+)',
        'expiration_date':  'Expiration Date\s*: *(.+)',
        'registrar':  'Authorized Agency\s*: *(.+)',
        'name_servers': 'Host Name\s*: *(.+)',  # list of name servers
    }

    def __init__(self, domain, text):
        if text.endswith(' no match'):
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisPt(WhoisEntry):
    """Whois parser for .pt domains
    """
    regex = {
        'domain_name': 'domain name: *(.+)',
        'creation_date': 'creation date \(dd\/mm\/yyyy\): *(.+)',
        'expiration_date': 'expiration date \(dd\/mm\/yyyy\): *(.+)',
        'name_servers': '\tNS\t(.+).',  # list of name servers
        'status': 'status: *(.+)',  # list of statuses
        'emails': EMAIL_REGEX,  # list of email addresses
    }

    def __init__(self, domain, text):
        if text.strip() == 'No entries found':
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisBg(WhoisEntry):
    """Whois parser for .bg domains
    """
    regex = {
        'expiration_date': 'expires at: *(.+)',
    }

    dayfirst = True

    def __init__(self, domain, text):
        if 'does not exist in database!' in text:
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisDe(WhoisEntry):
    """Whois parser for .de domains
    """
    regex = {
        'name': 'name: *(.+)',
        'org': 'Organisation: *(.+)',
        'address': 'Address: *(.+)',
        'zipcode': 'PostalCode: *(.+)',
        'city': 'City: *(.+)',
        'country_code': 'CountryCode: *(.+)',
        'phone': 'Phone: *(.+)',
        'fax': 'Fax: *(.+)'
    }

    def __init__(self, domain, text):
        if 'Status: free' in text:
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)

class WhoisAt(WhoisEntry):
    """Whois parser for .at domains
    """
    regex = {
        'name': 'personname: *(.+)',
        'org': 'organization: *(.+)',
        'address': 'street address: *(.+)',
        'zipcode': 'postal code: *(.+)',
        'city': 'city: *(.+)',
        'country': 'country: *(.+)',
        'phone': 'phone: *(.+)',
        'fax': 'fax-no: *(.+)',
        'changed': 'changed: *(.+)',
    }

    def __init__(self, domain, text):
        if 'Status: free' in text:
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)

class WhoisBe(WhoisEntry):
    """Whois parser for .be domains
    """
    regex = {
        'name': 'Name: *(.+)',
        'org': 'Organisation: *(.+)',
        'phone': 'Phone: *(.+)',
        'fax': 'Fax: *(.+)',
        'email': 'Email: *(.+)',
    }

    def __init__(self, domain, text):
        if 'Status: AVAILABLE' in text:
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)



class WhoisInfo(WhoisEntry):
    """Whois parser for .info domains
    """
    regex = {
        'domain_name':      'Domain Name: *(.+)',
        'registrar':        'Registrar: *(.+)',
        'whois_server':     'Whois Server: *(.+)', # empty usually
        'referral_url':     'Referral URL: *(.+)', # http url of whois_server: empty usually
        'updated_date':     'Updated Date: *(.+)',
        'creation_date':    'Creation Date: *(.+)',
        'expiration_date':  'Registry Expiry Date: *(.+)',
        'name_servers':     'Name Server: *(.+)', # list of name servers
        'status':           'Status: *(.+)', # list of statuses
        'emails':           EMAIL_REGEX, # list of email addresses
        'name':             'Registrant Name: *(.+)',
        'org':              'Registrant Organization: *(.+)',
        'address':          'Registrant Street: *(.+)',
        'city':             'Registrant City: *(.+)',
        'state':            'Registrant State/Province: *(.+)',
        'zipcode':          'Registrant Postal Code: *(.+)',
        'country':          'Registrant Country: *(.+)',
    }

    def __init__(self, domain, text):
        if text.strip() == 'NOT FOUND':
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisRf(WhoisRu):
    """Whois parser for .su domains
    """
    def __init__(self, domain, text):
        WhoisRu.__init__(self, domain, text)


class WhoisSu(WhoisRu):
    """Whois parser for .su domains
    """
    def __init__(self, domain, text):
        WhoisRu.__init__(self, domain, text)


class WhoisClub(WhoisEntry):
    """Whois parser for .us domains
    """
    regex = {
        'domain_name':                    'Domain Name: *(.+)',
        'domain__id':                     'Domain ID: *(.+)',
        'registrar':                      'Sponsoring Registrar: *(.+)',
        'registrar_id':                   'Sponsoring Registrar IANA ID: *(.+)',
        'registrar_url':                  'Registrar URL \(registration services\): *(.+)',
        # list of statuses
        'status':                         'Domain Status: *(.+)',
        'registrant_id':                  'Registrant ID: *(.+)',
        'registrant_name':                'Registrant Name: *(.+)',
        'registrant_address1':            'Registrant Address1: *(.+)',
        'registrant_address2':            'Registrant Address2: *(.+)',
        'registrant_city':                'Registrant City: *(.+)',
        'registrant_state_province':      'Registrant State/Province: *(.+)',
        'registrant_postal_code':         'Registrant Postal Code: *(.+)',
        'registrant_country':             'Registrant Country: *(.+)',
        'registrant_country_code':        'Registrant Country Code: *(.+)',
        'registrant_phone_number':        'Registrant Phone Number: *(.+)',
        'registrant_email':               'Registrant Email: *(.+)',
        'registrant_application_purpose': 'Registrant Application Purpose: *(.+)',
        'registrant_nexus_category':      'Registrant Nexus Category: *(.+)',
        'admin_id':                       'Administrative Contact ID: *(.+)',
        'admin_name':                     'Administrative Contact Name: *(.+)',
        'admin_address1':                 'Administrative Contact Address1: *(.+)',
        'admin_address2':                 'Administrative Contact Address2: *(.+)',
        'admin_city':                     'Administrative Contact City: *(.+)',
        'admin_state_province':           'Administrative Contact State/Province: *(.+)',
        'admin_postal_code':              'Administrative Contact Postal Code: *(.+)',
        'admin_country':                  'Administrative Contact Country: *(.+)',
        'admin_country_code':             'Administrative Contact Country Code: *(.+)',
        'admin_phone_number':             'Administrative Contact Phone Number: *(.+)',
        'admin_email':                    'Administrative Contact Email: *(.+)',
        'admin_application_purpose':      'Administrative Application Purpose: *(.+)',
        'admin_nexus_category':           'Administrative Nexus Category: *(.+)',
        'billing_id':                     'Billing Contact ID: *(.+)',
        'billing_name':                   'Billing Contact Name: *(.+)',
        'billing_address1':               'Billing Contact Address1: *(.+)',
        'billing_address2':               'Billing Contact Address2: *(.+)',
        'billing_city':                   'Billing Contact City: *(.+)',
        'billing_state_province':         'Billing Contact State/Province: *(.+)',
        'billing_postal_code':            'Billing Contact Postal Code: *(.+)',
        'billing_country':                'Billing Contact Country: *(.+)',
        'billing_country_code':           'Billing Contact Country Code: *(.+)',
        'billing_phone_number':           'Billing Contact Phone Number: *(.+)',
        'billing_email':                  'Billing Contact Email: *(.+)',
        'billing_application_purpose':    'Billing Application Purpose: *(.+)',
        'billing_nexus_category':         'Billing Nexus Category: *(.+)',
        'tech_id':                        'Technical Contact ID: *(.+)',
        'tech_name':                      'Technical Contact Name: *(.+)',
        'tech_address1':                  'Technical Contact Address1: *(.+)',
        'tech_address2':                  'Technical Contact Address2: *(.+)',
        'tech_city':                      'Technical Contact City: *(.+)',
        'tech_state_province':            'Technical Contact State/Province: *(.+)',
        'tech_postal_code':               'Technical Contact Postal Code: *(.+)',
        'tech_country':                   'Technical Contact Country: *(.+)',
        'tech_country_code':              'Technical Contact Country Code: *(.+)',
        'tech_phone_number':              'Technical Contact Phone Number: *(.+)',
        'tech_email':                     'Technical Contact Email: *(.+)',
        'tech_application_purpose':       'Technical Application Purpose: *(.+)',
        'tech_nexus_category':            'Technical Nexus Category: *(.+)',
        # list of name servers
        'name_servers':                   'Name Server: *(.+)',
        'created_by_registrar':           'Created by Registrar: *(.+)',
        'last_updated_by_registrar':      'Last Updated by Registrar: *(.+)',
        'creation_date':                  'Domain Registration Date: *(.+)',
        'expiration_date':                'Domain Expiration Date: *(.+)',
        'updated_date':                   'Domain Last Updated Date: *(.+)',
    }

    def __init__(self, domain, text):
        if 'Not found:' in text:
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisIo(WhoisEntry):
    """Whois parser for .io domains
    """
    regex = {
        'status':           'Status\s*: *(.+)',
        'name_servers':     'NS \d?\s*: *(.+)',
        #'owner':            'Owner\s*: *(.+)',
        'owner':            'Owner OrgName\s*: *(.+)',
        'expiration_date':  'Expiry\s*: *(.+)',
        'domain_name':      'Domain\s*: *(.+)',
        'registrar':        r'Check for \'[\w\.]*\' --- (.+)',
    }

    def __init__(self, domain, text):
        if 'is available for purchase' in text:
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisBiz(WhoisUs):
    """Whois parser for .biz domains
    """
    def __init__(self, domain, text):
        WhoisUs.__init__(self, domain, text)


class WhoisMobi(WhoisMe):
    """Whois parser for .mobi domains
    """
    def __init__(self, domain, text):
        WhoisMe.__init__(self, domain, text)


class WhoisKg(WhoisEntry):
    """Whois parser for .kg domains
    """
    regex = {
        'domain_name':                    'Domain\s*([\w]+\.[\w]{2,5})',
        'registrar':                      'Domain support: \s*(.+)',
        'registrant_name':                'Name: *(.+)',
        'registrant_address1':            'Address: *(.+)',
        'registrant_phone_number':        'phone: *(.+)',
        'registrant_email':               'Email: *(.+)',
        # # list of name servers
        'name_servers':                   'Name servers in the listed order: *([\d\w\.\s]+)',
        # 'name_servers':      r'([\w]+\.[\w]+\.[\w]{2,5}\s*\d{1,3}\.\d]{1,3}\.[\d]{1-3}\.[\d]{1-3})',
        'creation_date':                  'Record created: *(.+)',
        'expiration_date':                'Record expires on \s*(.+)',
        'updated_date':                   'Record last updated on\s*(.+)',

    }
    def __init__(self, domain, text):
        if 'Data not found. This domain is available for registration' in text:
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisChLi(WhoisEntry):
    """Whois Parser for .ch and .li domains
    """
    regex = {
        'domain_name':                      '\nDomain name:\n*(.+)',
        'registrant':                       'Holder of domain name:\n*([\n\s\S]+)\nContractual Language:',
        'registrar':                        'Registrar:\n*(.+)',
        'creation_date':                    'First registration date:\n*(.+)',
        'dnssec':                           'DNSSEC:*([\S]+)',
        'tech-c':                           'Technical contact:\n*([\n\s\S]+)\nRegistrar:',
        'name_servers':                     'Name servers:\n *([\n\S\s]+)'
    }
    def __init__(self,domain,text):
        if 'We do not have an entry in our database matching your query.' in text:
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisID(WhoisEntry):
        """Whois parser for .id domains
        """
        regex = {
            'domain_id':                   'Domain ID:(.+)',
            'domain_name':                 'Domain Name:(.+)',
            'creation_date':               'Created On:(.+)',
            'expiration_date':             'Expiration Date(.+)',
            'registrar':                   'Sponsoring Registrar ID:(.+)',
            'status':                      'Status:(.+)',  # list of statuses
            'registrant_id':               'Registrant ID:(.+)',
            'registrant_name':             'Registrant Name:(.+)',
            'registrant_org':              'Registrant Organization:(.+)',
            'registrant_address':          'Registrant Street1:(.+)',
            'registrant_address2':         'Registrant Street2:(.+)',
            'registrant_address3':         'Registrant Street3:(.+)',
            'registrant_city':             'Registrant City:(.+)',
            'registrant_country':          'Registrant Country:(.+)',
            'registrant_postal_code':      'Registrant Postal Code:(.+)',
            'registrant_phone':            'Registrant Phone:(.+)',
            'registrant_fax':              'Registrant FAX:(.+)',
            'registrant_email':            'Registrant Email:(.+)',
            'name_servers':                'Name Server:(.+)',  # list of name servers
        }

        def __init__(self, domain, text):
            if 'NOT FOUND' in text:
                raise PywhoisError(text)
            else:
                WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisSK(WhoisEntry):
        """
        Whois parser for .sk domains
         """
        regex = {
            'domain_name':                  'Domain-name *(.+)',
            'expiration_date':              'Valid-date *(.+)',
            'status':                       'Domain-status *(.+)',
            'name_servers':                 'dns_name *(.+)',
            'tech_id':                      'Tech-id *(.+)',
            'tech_name':                    'Tech-name *(.+)',
            'tech_org_id':                  'Tech-org.-ID *(.+)',
            'tech_address':                 'Tech-address *(.+)',
            'tech_email':                   'Tech-email *(.+)',
            'admin_id':                     'Admin-id *(.+)',
            'admin_name':                   'Admin-name *(.+)',
            'admin_legal_form':             'Admin-legal-form (.+)',
            'admin_org_id':                 'Admin-org.-ID *(.+)',
            'admin_address':                'Admin-address *(.+)',
            'admin_email':                  'Admin-email *(.+)',
            'updated_date':                 'Last-update *(.+)',
            'tech_phone':                   'Tech-telephone *(.+)',
            'name_servers_ipv4':            'dns_IPv4 *(.+)',

        }

        def __init__(self, domain, text):
            if 'Not found' in text:
                raise PywhoisError(text)
            else:
                WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisSe(WhoisEntry):
    """Whois parser for .se domains
    """
    regex = {
        'domain_name':                    'domain\.*: *(.+)',
        'creation_date':                  'created\.*: *(.+)',
        'updated_date':                   'modified\.*: *(.+)',
        'expiration_date':                'expires\.*: *(.+)',
        'transfer_date':                  'transferred\.*: *(.+)',
        'name_servers':                   'nserver\.*: *(.+)',  # list of name servers
        'dnssec':                         'dnssec\.*: *(.+)',
        'status':                         'status\.*: *(.+)',  # list of statuses
        'registrar':                      'registrar: *(.+)',
    }

    def __init__(self, domain, text):
        if 'not found.' in text:
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisIs(WhoisEntry):
    """Whois parser for .se domains
    """
    regex = {
        'domain_name':      'domain\.*: *(.+)',
        'name':             'person\.*: *(.+)',
        'address':          'address\.*: *(.+)',
        'creation_date':    'created\.*: *(.+)',
        'expiration_date':  'expires\.*: *(.+)',
        'name_servers':     'nserver\.*: *(.+)',  # list of name servers
        'dnssec':           'dnssec\.*: *(.+)',
    }

    def __init__(self, domain, text):
        if 'No entries found' in text:
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)
