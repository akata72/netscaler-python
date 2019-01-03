# This file could be created based on output from Terraform provisioning. 
# Static information should be replaced.  12.1.50.28.nc (19.12.2018)

# Login/logout
nitroNSIP = ["40.112.89.239","40.113.3.156"]
nitroUser = "nsadmin"
nitroPass = ""
connectiontype = "https"

# NTP server
ntp_serverip = "8.8.8.8"

# DNS server
dns_serverip = "10.0.0.4"
dnsvservername = ""
dns_local = ""
dns_state = ""
dns_type = ""
dnsprofilename = ""

# HA node parameters
ha_ipaddress = ["10.78.225.132","10.78.225.133"]
ha_inc       = "ENABLED"

# RPC node parameters
rpc_ipaddress = ["10.78.225.132","10.78.225.133"]
rpc_password = "I{qfuQ&$Io[8pIo0rA]Osao"
rpc_srcip = "<default is nsip of source>"
rpc_secure = "YES"

# Add Alwaysonvpn profile parameters
vpnalwayson_name = "vpn_alwayson_prof"
networkaccessonvpnfailure = "fullAccess"
clientcontrol = "ALLOW"
locationbasedvpn = "Remote"

# VPN session action (profile) parameters
# !! Important settings are made under Client Experience (GUI)
# !! i.e clientchoices, clientlessvpnmode  
vpnsessionaction_name = "vpn_session_prof"
sesstimeout = 360
splittunnel = "OFF"
transparentinterception = "ON"
defaultauthorizationaction = "ALLOW"
clientidletimeout = 360
clientcleanupprompt = "OFF" 
homepage = "<not used>"
icaproxy = "OFF" 
clientlessvpnmode = "OFF"
alwaysonprofilename = "vpn_alwayson_prof"
clientchoices = "On"   # Web portal will appear after login

# VPN session policy parameters
vpnsessionpolicy_name = "vpn_session_pol"
rule = "ns_true"
action = "vpn_session_prof"

# VPN vserver (netscaler gateway vserver)
vserver_name    = "vpnserver"
vserver_servicetype = "ssl"
vserver_ipv46 = "40.112.88.224"
vserver_port = "443"
icaonly = "off"
tcpprofilename = "default_xa_xd_profile"
vserverfqdn = "access.tech-01.net"
certkeynames = "idss-ns-root-ca"
downstateflush = "DISABLED"
listenpolicy = "NONE"

# Authentication LDAP action
ldapaction_name = "vpn_ldap_srv"
ldap_serverip = "10.0.0.4"
ldap_serverport = 636
ldapbase = "cn=users,dc=tech-01-dev,dc=net"
ldapbinddn = "svc_ldap@tech-01-dev.net"
ldapbinddnpassword = "thisisthepassword"
ldaploginname = "sAMAccountName"
searchfilter = "memberof=cn=vpn_users,ou=groups,dc=tech-01-dev,dc=net"
groupattrname = "memberOf"
subattributename = "cn"
sectype = "SSL"
passwdchange = "ENABLED"

# Authentication LDAP policy
ldappolicy_name = "ldap_vpn_pol"
ldappolicy_rule = "ns_true"
ldappolicy_reqaction = "vpn_ldap_srv"

# Binding between sslservice (vpnserver) and sslcertkey
#vpn_servicename = "vpnserver"
certkeyname = "idss-ns-root-ca"
ca_certkeyname = "idss-ns-root-ca"
ca = "false"
crlcheck = "Optional"
skipcaname = "true"
snicert = ""
ocspcheck = "Optional"


# SSL RSA Key
keyfile = "idss-ca-root-rsa.key"
bits = 2048
exponent = "F4"
keyform = "PEM"
des = "false"
des3 = "false"
password = "this1sthes3cretpa$$phrase71855"

# CA self-signed SSL Certificate Request
reqfile = "idss-ca-root-cert.req"
keyfile = "idss-ca-root-rsa.key"
keyform = "PEM"
pempassphrase = "this1sthes3cretpa$$phrase71855"
countryname = "NO"
statename = "Oslo"
organizationname = "TECH-01"
organizationunitname = "IT ISO IDSS"
localityname = "Oslo"
commonname = "access-dev.tech-01-dev.net"
emailaddress = "postmaster@tech-01-dev.net"
challengepassword = "1410"
companyname = "TECH-01"
digestmethod = "SHA256"

# CA self-signed SSL Certificate
certfile = "idss-ca-root.cer"
reqfile = "idss-ca-root-cert.req"
certtype = "ROOT_CERT"
certkeyfile = "idss-ca-root-rsa.key"
certkeyform = "PEM"
certpempassphrase = "this1sthes3cretpa$$phrase71855"

# CA Cert-Key 
certkey = "idss-ns-root-ca"
cert = "idss-ca-root.cer"
key = "idss-ca-root-rsa.key"
password = "true"
passplain = "this1sthes3cretpa$$phrase71855"
certificatetype = "ROOT_CERT"

# Binding between VPN vserver and Portaltheme
vserver_name = "vpnserver"
portaltheme = "RfWebUI"

# Binding between VPN vserver and Session policy
sesspol_bind_priority = 100
sesspol_bind_secondary = ""
sesspol_bind_groupextraction = ""
sesspol_bind_gotopriorityexpression = ""
sesspol_bind_bindpoint = ""

# Binding between VPN vserver and LDAP policy
ldappol_bind_priority = 100
ldappol_bind_secondary = ""
ldappol_bind_groupextraction = ""
ldappol_bind_gotopriorityexpression = ""
ldappol_bind_bindpoint = ""

# SAML action/profile
saml_action_name = "azure_saml_server"
samlidpcertname = "azure"
samlredirecturl = "https://login.microsoftonline.com/2f88d25e-2ffb-4c88-ac60-39cfc82cc98f/saml2"
samlrejectunsignedassertion = "Off"
logouturl = "https://login.microsoftonline.com/common/wsfederation?wa=wsignout1.0"
samlbinding = "POST"
logoutbinding = "POST"
samltwofactor = "Off" 
signaturealg = "RSA-SHA1"
digestmethod = "SHA1"
forceauthn = ""
samlidpmetadataurl = "https://login.microsoftonline.com/2f88d25e-2ffb-4c88-ac60-39cfc82cc98f/federationmetadata/2007-06/federationmetadata.xml?appid=430ce5ac-caee-4dff-8a59-cb8ee62e50bc"

# SAML profile
samlprofilename = "azuresamlprofile"
samlspcertname = ""   # this is for netscaler to sign tokens - not required initially. 
samlidpcertname = "azurecertkey"   #must be imported from the command line for this to work it seems. 
assertionconsumerserviceurl = "https://login.microsoftonline.com/2f88d25e-2ffb-4c88-ac60-39cfc82cc98f/saml2"
relaystaterule = ""
samlissuername = "https://access.tech-01-dev.net"
rejectunsignedrequests = "Off"
signaturealg = "RSA-SHA1"
digestmethod = "SHA1"
audience = ""
nameidformat = ""
nameidexpr = ""
encryptassertion = "OFF"
encryptionalgorithm = "AES256"
samlbinding = "POST"
skewtime = "5"
serviceproviderid = "https://sts.windows.net/2f88d25e-2ffb-4c88-ac60-39cfc82cc98f/"
signassertion= "ASSERTION"
keytransportalg = "RSA_OAEP"
splogouturl = "https://login.microsoftonline.com/common/wsfederation?wa=wsignout1.0"
logoutbinding = "POST"
defaultauthenticationgroup = ""
