#!/usr/bin/env python
import json, requests, base64, sys, os, re
requests.urllib3.disable_warnings()
from variables import *
from ns_mod_basics import *
from ns_mod_auth import *
from ns_mod_vpn import *
from ns_mod_certs import *

# Override parameters in variables.py
vserver_name = "vpnserver_3001"
vserver_port = "3001"
vpnsessionaction_name = "vpn_session_action_3001"
vpnsessionpolicy_name = "vpn_session_policy_3001"
vpnalwayson_name = "vpn_alwaysOn_3001"
ldapaction_name = "vpn_ldap_action_3001"
ldappolicy_name = "vpn_ldap_policy_3001"
saml_action_name = "vpn_saml_action_3001"
saml_policy_name = "vpn_saml_policy_3001"

authToken_ns1 = getAuthCookie(connectiontype,nitroNSIP[0],nitroUser,nitroPass)

# Actions, Profiles and Servers
# addVpnAlwaysOnProfile(connectiontype,nitroNSIP[0],authToken_ns1,vpnalwayson_name,networkaccessonvpnfailure,clientcontrol,locationbasedvpn)
addVpnSessionAction(connectiontype,nitroNSIP[0],authToken_ns1,vpnsessionaction_name,sesstimeout,splittunnel,transparentinterception, defaultauthorizationaction,clientidletimeout,clientcleanupprompt,homepage,icaproxy,clientlessvpnmode,vpnalwayson_name,clientchoices,splitdns)
addVpnSessionPolicy(connectiontype,nitroNSIP[0],authToken_ns1,vpnsessionpolicy_name,rule,vpnsessionaction_name)

addAuthLdapAction(connectiontype,nitroNSIP[0],authToken_ns1,ldapaction_name,ldap_serverip,ldap_serverport,ldapbase,ldapbinddn,ldapbinddnpassword,ldaploginname,searchfilter,groupattrname,subattributename,sectype,passwdchange,authentication)
addAuthLdapPolicy(connectiontype,nitroNSIP[0],authToken_ns1,ldappolicy_name,ldappolicy_rule,ldapaction_name)

addAuthSamlAction(connectiontype,nitroNSIP[0],authToken_ns1,saml_action_name,samlidpcertname,samlredirecturl, samlrejectunsignedassertion, samlissuername, samltwofactor,signaturealg, digestmethod, samlbinding, logouturl, skewtime, logoutbinding, forceauthn)
addAuthSamlPolicy(connectiontype,nitroNSIP[0],authToken_ns1,saml_policy_name,saml_policy_rule,saml_action_name)
addVpnvserver(connectiontype,nitroNSIP[0],authToken_ns1,vserver_name,vserver_servicetype,vserver_ipv46,vserver_port,icaonly,tcpprofilename,certkeynames,downstateflush,listenpolicy)

# Bindings
addSslvserver_SslcertKey_binding(connectiontype,nitroNSIP[0],authToken_ns1,vserver_name,"le-certificate-access","false",crlcheck,skipcaname,snicert,ocspcheck)
addVpnVserver_AuthLdapPolicy_binding(connectiontype,nitroNSIP[0],authToken_ns1,vserver_name,ldappolicy_name,ldappol_bind_priority,ldappol_bind_secondary,ldappol_bind_groupextraction,ldappol_bind_gotopriorityexpression, ldappol_bind_bindpoint)
addVpnVserver_SessionPolicy_binding(connectiontype,nitroNSIP[0],authToken_ns1,vserver_name,vpnsessionpolicy_name,sesspol_bind_priority,sesspol_bind_secondary,sesspol_bind_groupextraction,sesspol_bind_gotopriorityexpression, sesspol_bind_bindpoint)

saveNsConfig(connectiontype,nitroNSIP[0],authToken_ns1)
logOut(connectiontype,nitroNSIP[0],authToken_ns1)
