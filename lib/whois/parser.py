# coding=utf-8
from datetime import datetime

# parser.py - Module for parsing whois response data
# Copyright (c) 2008 Andrey Petrov
#
# This module is part of pywhois and is released under
# the MIT license: http://www.opensource.org/licenses/mit-license.php

import re
try:
    import dateutil.parser as dp
    from time_zones import tz_data
    DATEUTIL = True
except ImportError:
    DATEUTIL = False

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
]


class PywhoisError(Exception):
    pass


def datetime_parse(s):
    for known_format in KNOWN_FORMATS:
        try:
            s = datetime.strptime(s.strip(), known_format)
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
                s.strip(),
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
        'domain_name':          'Domain Name:\s?(.+)',
        'registrar':            'Registrar:\s?(.+)',
        'whois_server':         'Whois Server:\s?(.+)',
        'referral_url':         'Referral URL:\s?(.+)',  # http url of whois_server
        'updated_date':         'Updated Date:\s?(.+)',
        'creation_date':        'Creation Date:\s?(.+)',
        'expiration_date':      'Expir\w+ Date:\s?(.+)',
        'name_servers':         'Name Server:\s?(.+)',  # list of name servers
        'status':               'Status:\s?(.+)',  # list of statuses
        'emails':               '[\w.-]+@[\w.-]+\.[\w]{2,4}',  # list of email s
        'dnssec':               'dnssec:\s*([\S]+)',
        'name':                 'Registrant Name:\s*(.+)',
        'org':                  'Registrant\s*Organization:\s*(.+)',
        'address':              'Registrant Street:\s*(.+)',
        'city':                 'Registrant City:\s*(.+)',
        'state':                'Registrant State/Province:\s*(.+)',
        'zipcode':              'Registrant Postal Code:\s*(.+)',
        'country':              'Registrant Country:\s*(.+)',
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
        for attr, regex in self._regex.items():
            if regex:
                values = []
                for value in re.findall(regex, self.text, re.IGNORECASE):
                    if isinstance(value, basestring):
                        # try casting to date format
                        value = cast_date(value.strip(),
                                          dayfirst=self.dayfirst,
                                          yearfirst=self.yearfirst)
                    if value and value not in values:
                        # avoid duplicates
                        values.append(value)
                if len(values) == 1:
                    values = values[0]
                elif not values:
                    values = None

                self[attr] = values


    def __setitem__(self, name, value):
        super(WhoisEntry, self).__setitem__(name, value)
        setattr(self, name, value)


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
        elif domain.endswith('.kr'):
            return WhoisKr(domain, text)
        elif domain.endswith('.pt'):
            return WhoisPt(domain, text)
        elif domain.endswith('.bg'):
            return WhoisBg(domain, text)
        elif domain.endswith('.de'):
            return WhoisDe(domain, text)
        elif domain.endswith('.ca'):
            return WhoisCa(domain, text)
        elif domain.endswith('.be'):
            return WhoisBe(domain, text)
        elif domain.endswith('.рф'):
            return WhoisRf(domain, text)
        elif domain.endswith('.info'):
            return WhoisInfo(domain, text)
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
        'domain_name':      'Domain Name:\s?(.+)',
        'registrar':        'Registrar:\s?(.+)',
        'whois_server':     'Whois Server:\s?(.+)', # empty usually
        'referral_url':     'Referral URL:\s?(.+)', # http url of whois_server: empty usually
        'updated_date':     'Updated Date:\s?(.+)',
        'creation_date':    'Creation Date:\s?(.+)',
        'expiration_date':  'Registry Expiry Date:\s?(.+)',
        'name_servers':     'Name Server:\s?(.+)', # list of name servers
        'status':           'Status:\s?(.+)', # list of statuses
        'emails':           '[\w.-]+@[\w.-]+\.[\w]{2,4}', # list of email addresses
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
        'domain_name': 'domain:\s*(.+)',
        'registrar': 'registrar:\s*(.+)',
        'creation_date': 'created:\s*(.+)',
        'expiration_date': 'paid-till:\s*(.+)',
        'name_servers': 'nserver:\s*(.+)',  # list of name servers
        'status': 'state:\s*(.+)',  # list of statuses
        'emails': '[\w.-]+@[\w.-]+\.[\w]{2,4}',  # list of email addresses
        'org': 'org:\s*(.+)'
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
            lines = match.groups()[0].strip().splitlines()
            self.name = lines[0]
            self.address = lines[1]
            if len(lines) == 4:
                self.zip_code, _, self.city = lines[2].partition(' ')
            self.country = lines[-1]
                

class WhoisName(WhoisEntry):
    """Whois parser for .name domains
    """
    regex = {
        'domain_name_id':  'Domain Name ID:\s*(.+)',
        'domain_name':     'Domain Name:\s*(.+)',
        'registrar_id':    'Sponsoring Registrar ID:\s*(.+)',
        'registrar':       'Sponsoring Registrar:\s*(.+)',
        'registrant_id':   'Registrant ID:\s*(.+)',
        'admin_id':        'Admin ID:\s*(.+)',
        'technical_id':    'Tech ID:\s*(.+)',
        'billing_id':      'Billing ID:\s*(.+)',
        'creation_date':   'Created On:\s*(.+)',
        'expiration_date': 'Expires On:\s*(.+)',
        'updated_date':    'Updated On:\s*(.+)',
        'name_server_ids': 'Name Server ID:\s*(.+)',  # list of name server ids
        'name_servers':    'Name Server:\s*(.+)',  # list of name servers
        'status':          'Domain Status:\s*(.+)',  # list of statuses
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
        'domain_name':                    'Domain Name:\s*(.+)',
        'domain__id':                     'Domain ID:\s*(.+)',
        'registrar':                      'Sponsoring Registrar:\s*(.+)',
        'registrar_id':                   'Sponsoring Registrar IANA ID:\s*(.+)',
        'registrar_url':                  'Registrar URL \(registration services\):\s*(.+)',
        'status':                         'Domain Status:\s*(.+)',  # list of statuses
        'registrant_id':                  'Registrant ID:\s*(.+)',
        'registrant_name':                'Registrant Name:\s*(.+)',
        'registrant_address1':            'Registrant Address1:\s*(.+)',
        'registrant_address2':            'Registrant Address2:\s*(.+)',
        'registrant_city':                'Registrant City:\s*(.+)',
        'registrant_state_province':      'Registrant State/Province:\s*(.+)',
        'registrant_postal_code':         'Registrant Postal Code:\s*(.+)',
        'registrant_country':             'Registrant Country:\s*(.+)',
        'registrant_country_code':        'Registrant Country Code:\s*(.+)',
        'registrant_phone_number':        'Registrant Phone Number:\s*(.+)',
        'registrant_email':               'Registrant Email:\s*(.+)',
        'registrant_application_purpose': 'Registrant Application Purpose:\s*(.+)',
        'registrant_nexus_category':      'Registrant Nexus Category:\s*(.+)',
        'admin_id':                       'Administrative Contact ID:\s*(.+)',
        'admin_name':                     'Administrative Contact Name:\s*(.+)',
        'admin_address1':                 'Administrative Contact Address1:\s*(.+)',
        'admin_address2':                 'Administrative Contact Address2:\s*(.+)',
        'admin_city':                     'Administrative Contact City:\s*(.+)',
        'admin_state_province':           'Administrative Contact State/Province:\s*(.+)',
        'admin_postal_code':              'Administrative Contact Postal Code:\s*(.+)',
        'admin_country':                  'Administrative Contact Country:\s*(.+)',
        'admin_country_code':             'Administrative Contact Country Code:\s*(.+)',
        'admin_phone_number':             'Administrative Contact Phone Number:\s*(.+)',
        'admin_email':                    'Administrative Contact Email:\s*(.+)',
        'admin_application_purpose':      'Administrative Application Purpose:\s*(.+)',
        'admin_nexus_category':           'Administrative Nexus Category:\s*(.+)',
        'billing_id':                     'Billing Contact ID:\s*(.+)',
        'billing_name':                   'Billing Contact Name:\s*(.+)',
        'billing_address1':               'Billing Contact Address1:\s*(.+)',
        'billing_address2':               'Billing Contact Address2:\s*(.+)',
        'billing_city':                   'Billing Contact City:\s*(.+)',
        'billing_state_province':         'Billing Contact State/Province:\s*(.+)',
        'billing_postal_code':            'Billing Contact Postal Code:\s*(.+)',
        'billing_country':                'Billing Contact Country:\s*(.+)',
        'billing_country_code':           'Billing Contact Country Code:\s*(.+)',
        'billing_phone_number':           'Billing Contact Phone Number:\s*(.+)',
        'billing_email':                  'Billing Contact Email:\s*(.+)',
        'billing_application_purpose':    'Billing Application Purpose:\s*(.+)',
        'billing_nexus_category':         'Billing Nexus Category:\s*(.+)',
        'tech_id':                        'Technical Contact ID:\s*(.+)',
        'tech_name':                      'Technical Contact Name:\s*(.+)',
        'tech_address1':                  'Technical Contact Address1:\s*(.+)',
        'tech_address2':                  'Technical Contact Address2:\s*(.+)',
        'tech_city':                      'Technical Contact City:\s*(.+)',
        'tech_state_province':            'Technical Contact State/Province:\s*(.+)',
        'tech_postal_code':               'Technical Contact Postal Code:\s*(.+)',
        'tech_country':                   'Technical Contact Country:\s*(.+)',
        'tech_country_code':              'Technical Contact Country Code:\s*(.+)',
        'tech_phone_number':              'Technical Contact Phone Number:\s*(.+)',
        'tech_email':                     'Technical Contact Email:\s*(.+)',
        'tech_application_purpose':       'Technical Application Purpose:\s*(.+)',
        'tech_nexus_category':            'Technical Nexus Category:\s*(.+)',
        'name_servers':                   'Name Server:\s*(.+)',  # list of name servers
        'created_by_registrar':           'Created by Registrar:\s*(.+)',
        'last_updated_by_registrar':      'Last Updated by Registrar:\s*(.+)',
        'creation_date':                  'Domain Registration Date:\s*(.+)',
        'expiration_date':                'Domain Expiration Date:\s*(.+)',
        'updated_date':                   'Domain Last Updated Date:\s*(.+)',
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
        'domain_name':                    'DOMAIN NAME:\s*(.+)\n',
        'registrar':                      'REGISTRAR:\n\s*(.+)',
        'registrar_url':                  'URL:\s*(.+)',        # not available
        'status':                         'Registration status:\n\s*(.+)',  # not available
        'registrant_name':                'Registrant:\n\s*(.+)',   # not available
        'creation_date':                  'created:\s*(.+)\n',
        'expiration_date':                'renewal date:\s*(.+)',
        'updated_date':                   'last modified:\s*(.+)\n',
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
        'registrant_name':                'Name:\s*(.+)',
        'registrant_number':              'Number:\s*(.+)\n',
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
        'registrar_url':                  'URL:\s*(.+)',
        'status':                         'Registration status:\n\s*(.+)',  # list of statuses
        'registrant_name':                'Registrant:\n\s*(.+)',
        'creation_date':                  'Registered on:\s*(.+)',
        'expiration_date':                'Expiry date:\s*(.+)',
        'updated_date':                   'Last updated:\s*(.+)',
        'name_servers':                   'Name servers:\s*(.+)',
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
        'domain_name': 'domain:\s*(.+)',
        'registrar': 'registrar:\s*(.+)',
        'creation_date': 'created:\s*(.+)',
        'expiration_date': 'anniversary:\s*(.+)',
        'name_servers': 'nserver:\s*(.+)',  # list of name servers
        'status': 'status:\s*(.+)',  # list of statuses
        'emails': '[\w.-]+@[\w.-]+\.[\w]{2,4}',  # list of email addresses
        'updated_date': 'last-update:\s*(.+)',
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
        'domain_name':                    'domain:\s*([\S]+)',
        'name':                           'descr:\s*([\S\ ]+)',
        'address':                        'address:\s*([\S\ ]+)',
        'phone':                          'phone:\s*([\S\ ]+)',
        'status':                         'status:\s*([\S]+)',  # list of statuses
        'creation_date':                  'created:\s*([\S]+)',
        'updated_date':                   'modified:\s*([\S]+)',
        'expiration_date':                'expires:\s*([\S]+)',
        'name_servers':                   'nserver:\s*([\S]+) \[\S+\]',  # list of name servers
        'name_server_statuses':           'nserver:\s*([\S]+) \[(\S+)\]',  # list of name servers and statuses
        'dnssec':                         'dnssec:\s*([\S]+)',
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
        'domain_name':                    'Domain Name:\s*(.+)\n',
        'last_modified':			      'Last Modified:\s*(.+)\n',
        'registrar':                      'Registrar Name:\s*(.+)\n',
        'status':                         'Status:\s*(.+)',
        'registrant_name':                'Registrant:\s*(.+)',
        'name_servers':                   'Name Server:\s*(.+)',
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
        'domain_name': r'Domain:\s*([^\n\r]+)',
        'tech_name': r'Technical:\s*Name:\s*([^\n\r]+)',
        'tech_org': r'Technical:\s*Name:\s*[^\n\r]+\s*Organisation:\s*([^\n\r]+)',
        'tech_phone': r'Technical:\s*Name:\s*[^\n\r]+\s*Organisation:\s*[^\n\r]+\s*Language:\s*[^\n\r]+\s*Phone:\s*([^\n\r]+)',
        'tech_fax': r'Technical:\s*Name:\s*[^\n\r]+\s*Organisation:\s*[^\n\r]+\s*Language:\s*[^\n\r]+\s*Phone:\s*[^\n\r]+\s*Fax:\s*([^\n\r]+)',
        'tech_email': r'Technical:\s*Name:\s*[^\n\r]+\s*Organisation:\s*[^\n\r]+\s*Language:\s*[^\n\r]+\s*Phone:\s*[^\n\r]+\s*Fax:\s*[^\n\r]+\s*Email:\s*([^\n\r]+)',
        'registrar': r'Registrar:\s*Name:\s*([^\n\r]+)',
        'name_servers': r'Name servers:\s*([^\n\r]+)\s*([^\n\r]*)',  # list of name servers
    }

    def __init__(self, domain, text):
        if text.strip() == 'Status: AVAILABLE':
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisBr(WhoisEntry):
    """Whois parser for .br domains
    """
    regex = {
        'domain':                        'domain:\s*(.+)\n',
        'owner':                         'owner:\s*([\S ]+)',
        'ownerid':                       'ownerid:\s*(.+)',
        'country':                       'country:\s*(.+)',
        'owner_c':                       'owner-c:\s*(.+)',
        'admin_c':                       'admin-c:\s*(.+)',
        'tech_c':                        'tech-c:\s*(.+)',
        'billing_c':                     'billing-c:\s*(.+)',
        'nserver':                       'nserver:\s*(.+)',
        'nsstat':                        'nsstat:\s*(.+)',
        'nslastaa':                      'nslastaa:\s*(.+)',
        'saci':                          'saci:\s*(.+)',
        'created':                       'created:\s*(.+)',
        'expires':                       'expires:\s*(.+)',
        'changed':                       'changed:\s*(.+)',
        'status':                        'status:\s*(.+)',
        'nic_hdl_br':                    'nic-hdl-br:\s*(.+)',
        'person':                        'person:\s*([\S ]+)',
        'email':                         'e-mail:\s*(.+)',
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
        'domain_name': 'Domain Name\s*:\s*(.+)',
        'registrant_org': 'Registrant\s*:\s*(.+)',
        'registrant_address': 'Registrant Address\s*:\s*(.+)',
        'registrant_zip': 'Registrant Zip Code\s*:\s*(.+)',
        'admin_name': 'Administrative Contact\(AC\)\s*:\s*(.+)',
        'admin_email': 'AC E-Mail\s*:\s*(.+)',
        'admin_phone': 'AC Phone Number\s*:\s*(.+)',
        'creation_date': 'Registered Date\s*:\s*(.+)',
        'updated_date':  'Last updated Date\s*:\s*(.+)',
        'expiration_date':  'Expiration Date\s*:\s*(.+)',
        'registrar':  'Authorized Agency\s*:\s*(.+)',
        'name_servers': 'Host Name\s*:\s*(.+)',  # list of name servers
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
        'domain_name': 'domain name:\s*(.+)',
        'creation_date': 'creation date \(dd\/mm\/yyyy\):\s*(.+)',
        'expiration_date': 'expiration date \(dd\/mm\/yyyy\):\s*(.+)',
        'name_servers': '\tNS\t(.+).',  # list of name servers
        'status': 'status:\s*(.+)',  # list of statuses
        'emails': '[\w.-]+@[\w.-]+\.[\w]{2,4}',  # list of email addresses
    }

    def __init__(self, domain, text):
        if text.strip() == 'No entries found':
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisBg(WhoisEntry):
    """Whois parser for .bg domains"""

    regex = {
        'expiration_date': 'expires at:\s*(.+)',
    }

    dayfirst = True

    def __init__(self, domain, text):
        if 'does not exist in database!' in text:
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisRf(WhoisEntry):
    """Whois parser for .rf domains"""

    regex = {
        'expiration_date': 'free-date:\s*(.+)',
    }

    def __init__(self, domain, text):
        if text.strip() == 'No entries found':
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisDe(WhoisEntry):
    """Whois parser for .de domains"""

    regex = {
        'name': 'name:\s*(.+)',
        'org': 'Organisation:\s*(.+)',
        'address': 'Address:\s*(.+)',
        'zipcode': 'PostalCode:\s*(.+)',
        'city': 'City:\s*(.+)',
        'country_code': 'CountryCode:\s*(.+)',
        'phone': 'Phone:\s*(.+)',
        'fax': 'Fax:\s*(.+)'
    }

    def __init__(self, domain, text):
        if 'Status: free' in text:
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)


class WhoisBe(WhoisEntry):
    """Whois parser for .be domains"""

    regex = {
        'name': 'Name:\s*(.+)',
        'org': 'Organisation:\s*(.+)',
        'phone': 'Phone:\s*(.+)',
        'fax': 'Fax:\s*(.+)',
        'email': 'Email:\s*(.+)',
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
        'domain_name':      'Domain Name:\s?(.+)',
        'registrar':        'Registrar:\s?(.+)',
        'whois_server':     'Whois Server:\s?(.+)', # empty usually
        'referral_url':     'Referral URL:\s?(.+)', # http url of whois_server: empty usually
        'updated_date':     'Updated Date:\s?(.+)',
        'creation_date':    'Creation Date:\s?(.+)',
        'expiration_date':  'Registry Expiry Date:\s?(.+)',
        'name_servers':     'Name Server:\s?(.+)', # list of name servers
        'status':           'Status:\s?(.+)', # list of statuses
        'emails':           '[\w.-]+@[\w.-]+\.[\w]{2,4}', # list of email addresses
        'name':             'Registrant Name:\s*(.+)',
        'org':              'Registrant Organization:\s*(.+)',
        'address':          'Registrant Street:\s*(.+)',
        'city':             'Registrant City:\s*(.+)',
        'state':            'Registrant State/Province:\s*(.+)',
        'zipcode':          'Registrant Postal Code:\s*(.+)',
        'country':          'Registrant Country:\s*(.+)',
    }

    def __init__(self, domain, text):
        if text.strip() == 'NOT FOUND':
            raise PywhoisError(text)
        else:
            WhoisEntry.__init__(self, domain, text, self.regex)
