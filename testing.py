#!/usr/bin/env python
import json, requests, base64, sys, os, re
requests.urllib3.disable_warnings()
from variables import *
from ns_mod_auth import *
from ns_mod_basics import *

authToken_ns1 = getAuthCookie(connectiontype,nitroNSIP[0],nitroUser,nitroPass)

addAuthLdapAction(connectiontype,nitroNSIP[0],authToken_ns1,ldapaction_name,ldap_serverip,ldap_serverport,ldapbase,ldapbinddn,ldapbinddnpassword,ldaploginname,searchfilter,groupattrname,subattributename,sectype,passwdchange,authentication)
addAuthLdapPolicy(connectiontype,nitroNSIP[0],authToken_ns1,ldappolicy_name,ldappolicy_rule,ldappolicy_reqaction)

#saveNsConfig(connectiontype,nitroNSIP[1],authToken_ns2)

### Qualys
""" 
set ssl profile ns_default_ssl_profile_frontend -sessreuse DISABLED
create ssl dhparam "/nsconfig/ssl/dhkey2048-vpn.key" 2048 -gen 2
set ssl profile ns_default_ssl_profile_frontend -dh ENABLED -dhFile "/nsconfig/ssl/dhkey2048-vpn.key"
set ssl profile ns_default_ssl_profile_frontend -ssl3 DISABLED
set ssl profile ns_default_ssl_profile_frontend -tls1 DISABLED
set ssl profile ns_default_ssl_profile_frontend -HSTS ENABLED
bind ssl vserver vpnserver -eccCurveName ALL
set ssl profile ns_default_ssl_profile_frontend -HSTS ENABLED -maxage 157680000 
"""

### Cipher optimization
"""
add ssl cipher ssllabs-smw-q2-2018
bind ssl cipher ssllabs-smw-q2-2018 -cipherName TLS1.2-ECDHE-ECDSA-AES128-GCM-SHA256
bind ssl cipher ssllabs-smw-q2-2018 -cipherName TLS1.2-ECDHE-ECDSA-AES256-GCM-SHA384
bind ssl cipher ssllabs-smw-q2-2018 -cipherName TLS1.2-ECDHE-ECDSA-AES128-SHA256
bind ssl cipher ssllabs-smw-q2-2018 -cipherName TLS1.2-ECDHE-ECDSA-AES256-SHA384
bind ssl cipher ssllabs-smw-q2-2018 -cipherName TLS1-ECDHE-ECDSA-AES128-SHA
bind ssl cipher ssllabs-smw-q2-2018 -cipherName TLS1-ECDHE-ECDSA-AES256-SHA
bind ssl cipher ssllabs-smw-q2-2018 -cipherName TLS1.2-ECDHE-RSA-AES128-GCM-SHA256
bind ssl cipher ssllabs-smw-q2-2018 -cipherName TLS1.2-ECDHE-RSA-AES256-GCM-SHA384
bind ssl cipher ssllabs-smw-q2-2018 -cipherName TLS1.2-ECDHE-RSA-AES-128-SHA256
bind ssl cipher ssllabs-smw-q2-2018 -cipherName TLS1.2-ECDHE-RSA-AES-256-SHA384
bind ssl cipher ssllabs-smw-q2-2018 -cipherName TLS1-ECDHE-RSA-AES128-SHA
bind ssl cipher ssllabs-smw-q2-2018 -cipherName TLS1-ECDHE-RSA-AES256-SHA
bind ssl cipher ssllabs-smw-q2-2018 -cipherName TLS1.2-DHE-RSA-AES128-GCM-SHA256
bind ssl cipher ssllabs-smw-q2-2018 -cipherName TLS1.2-DHE-RSA-AES256-GCM-SHA384
bind ssl cipher ssllabs-smw-q2-2018 -cipherName TLS1-DHE-RSA-AES-128-CBC-SHA
bind ssl cipher ssllabs-smw-q2-2018 -cipherName TLS1-DHE-RSA-AES-256-CBC-SHA
bind ssl cipher ssllabs-smw-q2-2018 -cipherName TLS1-AES-128-CBC-SHA
bind ssl cipher ssllabs-smw-q2-2018 -cipherName TLS1-AES-256-CBC-SHA
unbind ssl vserver vpnserver -cipherName DEFAULT
bind ssl vserver vpnserver -cipherName ssllabs-smw-q2-2018
"""

logOut(connectiontype,nitroNSIP[1],authToken_ns1)


