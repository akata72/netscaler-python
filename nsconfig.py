#!/usr/bin/env python
import json, requests, base64, sys, os, re
requests.urllib3.disable_warnings()
from variables import *
from ns_mod_basics import *
from ns_mod_ha_rpc import *
from ns_mod_auth import *
from ns_mod_vpn import *
from ns_mod_certs import *

############## Getting authentication token from both devices  ###################

authToken_ns1 = getAuthCookie(connectiontype,nitroNSIP[0],nitroUser,nitroPass)
authToken_ns2 = getAuthCookie(connectiontype,nitroNSIP[1],nitroUser,nitroPass)

############## Adding the opposite node and updating the rpcnode (and password) ###################

addHaNode(connectiontype,nitroNSIP[0],authToken_ns1,1,ha_ipaddress[1],"ENABLED")
updateNsRpcNode(connectiontype,nitroNSIP[0],authToken_ns1,rpc_ipaddress[0],rpc_password,rpc_srcip,"NO")
updateNsRpcNode(connectiontype,nitroNSIP[0],authToken_ns1,rpc_ipaddress[1],rpc_password,rpc_srcip,"YES")

addHaNode(connectiontype,nitroNSIP[1],authToken_ns2,1,ha_ipaddress[0],"ENABLED")
updateNsRpcNode(connectiontype,nitroNSIP[1],authToken_ns2,rpc_ipaddress[1],rpc_password,rpc_srcip,"NO")
updateNsRpcNode(connectiontype,nitroNSIP[1],authToken_ns2,rpc_ipaddress[0],rpc_password,rpc_srcip,"YES")

saveNsConfig(connectiontype,nitroNSIP[1],authToken_ns2)
logOut(connectiontype,nitroNSIP[1],authToken_ns2)


######### Remaining configuration will be replicated if HA enabled correctly ##########

enable_nsfeature(connectiontype,nitroNSIP[0],authToken_ns1,"ssl sslvpn")
addNtpServer(connectiontype,nitroNSIP[0],authToken_ns1,ntp_serverip)
addDnsNameServer(connectiontype,nitroNSIP[0],authToken_ns1,dns_serverip,dnsvservername,dns_local,dns_state,dns_type,dnsprofilename)

########## Creates a self-signed Certificates ##########

createSslRsaKey(connectiontype,nitroNSIP[0],authToken_ns1,keyfile,bits,exponent,keyform,des,des3,password)
createSslCertReq(connectiontype,nitroNSIP[0],authToken_ns1,reqfile,keyfile,keyform,pempassphrase,countryname,statename,organizationname,organizationunitname,localityname,commonname,emailaddress, challengepassword,companyname,digestmethod)
createSslCert(connectiontype,nitroNSIP[0],authToken_ns1,certfile,reqfile,certtype,certkeyfile,certkeyform,certpempassphrase)
addSslCertKey(connectiontype,nitroNSIP[0],authToken_ns1,certkey,cert,key,password,passplain,certificatetype)

# CLI Verification: show vpn alwaysONProfile
addVpnAlwaysOnProfile(connectiontype,nitroNSIP[0],authToken_ns1,vpnalwayson_name,networkaccessonvpnfailure,clientcontrol,locationbasedvpn)

# CLI Verification: show vpn sessionaction vpn_session_prof
addVpnSessionAction(connectiontype,nitroNSIP[0],authToken_ns1,vpnsessionaction_name,sesstimeout,splittunnel,transparentinterception, defaultauthorizationaction,clientidletimeout,clientcleanupprompt,homepage,icaproxy,clientlessvpnmode,alwaysonprofilename,clientchoices)

# CLI Verification: show vpn sessionpolicy vpn_session_pol
addVpnSessionPolicy(connectiontype,nitroNSIP[0],authToken_ns1,vpnsessionpolicy_name,rule,action)

# CLI Verification: show authentication ldapaction vpn_ldap_srv
addAuthLdapAction(connectiontype,nitroNSIP[0],authToken_ns1,ldapaction_name,ldap_serverip,ldap_serverport,ldapbase,ldapbinddn,ldapbinddnpassword,ldaploginname,searchfilter,groupattrname,subattributename,sectype,passwdchange)

# CLI Verification: show authentication ldappolicy vpn_ldap_pol
addAuthLdapPolicy(connectiontype,nitroNSIP[0],authToken_ns1,ldappolicy_name,ldappolicy_rule,ldappolicy_reqaction)

addAuthSamlAction(connectiontype,nitroNSIP[0],authToken_ns1,saml_action_name,samlidpcertname,samlredirecturl, samlrejectunsignedassertion, samlissuername, samltwofactor,signaturealg, digestmethod, samlbinding, logouturl, skewtime, logoutbinding, forceauthn)
addAuthSamlPolicy(connectiontype,nitroNSIP[0],authToken_ns1,"vpn_saml_pol","ns_true","")

# CLI Verification: show vpn vserver sslvpnserver
addVpnvserver(connectiontype,nitroNSIP[0],authToken_ns1,vserver_name,vserver_servicetype,vserver_ipv46,vserver_port,icaonly,tcpprofilename,certkeynames,downstateflush,listenpolicy)

# CLI Verification: show ssl vserver sslvpnserver
#addSslService_sslCertKey_binding(connectiontype,nitroNSIP[0],authToken_ns1,vserver_name,certkeyname,"false",crlcheck,skipcaname,snicert,ocspcheck)
#addSslService_sslCertKey_binding(connectiontype,nitroNSIP[0],authToken_ns1,vpn_servicename,ca_certkeyname,"true",crlcheck,skipcaname,snicert,ocspcheck)
addSslvserver_SslcertKey_binding(connectiontype,nitroNSIP[0],authToken_ns1,vserver_name,certkeyname,"false",crlcheck,skipcaname,snicert,ocspcheck)

# CLI Verification: show vpn vserver sslvpnserver | more
addVpnVserver_Vpnportaltheme_binding(connectiontype,nitroNSIP[0],authToken_ns1,vserver_name,portaltheme)

# CLI Verification: show vpn vserver sslvpnserver | more
addVpnVserver_AuthLdapPolicy_binding(connectiontype,nitroNSIP[0],authToken_ns1,vserver_name,ldappolicy_name,ldappol_bind_priority,ldappol_bind_secondary,ldappol_bind_groupextraction,ldappol_bind_gotopriorityexpression, ldappol_bind_bindpoint)

# CLI Verification: show vpn vserver sslvpnserver | more

addVpnVserver_SessionPolicy_binding(connectiontype,nitroNSIP[0],authToken_ns1,vserver_name,vpnsessionpolicy_name,sesspol_bind_priority,sesspol_bind_secondary,sesspol_bind_groupextraction,sesspol_bind_gotopriorityexpression, sesspol_bind_bindpoint)

#addAuthenticationSamlIdpProfile(connectiontype,nitroNSIP,authToken,samlprofilename,samlspcertname,samlidpcertname,assertionconsumerserviceurl,relaystaterule,samlissuername,rejectunsignedrequests,signaturealg,digestmethod,audience,nameidformat,nameidexpr,encryptassertion,encryptionalgorithm,samlbinding,skewtime,serviceproviderid,signassertion,keytransportalg,splogouturl,logoutbinding,defaultauthenticationgroup)

########## Save configuration and log out ##########

saveNsConfig(connectiontype,nitroNSIP[0],authToken_ns1)
logOut(connectiontype,nitroNSIP[0],authToken_ns1)
