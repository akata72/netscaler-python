import json, requests, base64, sys, os, re
requests.urllib3.disable_warnings()

#### VPN action, policy, server - related tasks ####
def addVpnAlwaysOnProfile(connectiontype,nitroNSIP,authToken,name,networkaccessonvpnfailure,clientcontrol,locationbasedvpn):
   url = '%s://%s/nitro/v1/config/vpnalwaysonprofile' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "vpnalwaysonprofile": {
      "name": name,
      "networkaccessonvpnfailure": networkaccessonvpnfailure,
      "clientcontrol": clientcontrol,
      "locationbasedvpn": locationbasedvpn,
     }
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("\nAdding VPN AlwaysON Profile: %s" % response.reason)
   print ("Response: %s" % response.text)

def addVpnSessionAction(connectiontype,nitroNSIP,authToken,vpnsessionaction_name,sesstimeout,splittunnel,transparentinterception, defaultauthorizationaction,clientidletimeout,clientcleanupprompt,homepage,icaproxy,clientlessvpnmode,alwaysonprofilename,clientchoices):
   url = '%s://%s/nitro/v1/config/vpnsessionaction' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "vpnsessionaction": {
      "name": vpnsessionaction_name,
      "sesstimeout": sesstimeout,
      "splittunnel": splittunnel,
      "transparentinterception": transparentinterception,
      "defaultauthorizationaction": defaultauthorizationaction,
      "clientidletimeout" : clientidletimeout,
      "clientcleanupprompt" : clientcleanupprompt,
      #"homepage" : homepage,
      "icaproxy" : icaproxy,
      "clientlessvpnMode" : clientlessvpnmode,
      "alwaysonprofilename" : alwaysonprofilename,
      "clientchoices": clientchoices,

    #  "useraccounting":<String_value>,
    #  "httpport":<Integer[]_value>,
    #  "winsip":<String_value>,
    #  "dnsvservername":<String_value>,
    #  "splitdns":<String_value>,
    #  "clientsecurity":<String_value>,
    #  "clientsecuritygroup":<String_value>,
    #  "clientsecuritymessage":<String_value>,
    #  "clientsecuritylog":<String_value>,
    #  "locallanaccess":<String_value>,
    #  "rfc1918":<String_value>,
    #  "spoofiip":<String_value>,
    #  "killconnections":<String_value>,
    #  "windowsclienttype":<String_value>,
    #  "authorizationgroup":<String_value>,
    #  "smartgroup":<String_value>,
    #  "clientidletimeout":<Double_value>,
    #  "proxy":<String_value>,
    #  "allprotocolproxy":<String_value>,
    #  "httpproxy":<String_value>,
    #  "ftpproxy":<String_value>,
    #  "socksproxy":<String_value>,
    #  "gopherproxy":<String_value>,
    #  "sslproxy":<String_value>,
    #  "proxyexception":<String_value>,
    #  "proxylocalbypass":<String_value>,
    #  "forcecleanup":<String[]_value>,
    #  "clientoptions":<String_value>,
    #  "clientconfiguration":<String[]_value>,
    #  "sso":<String_value>,
    #  "ssocredential":<String_value>,
    #  "windowsautologon":<String_value>,
    #  "usemip":<String_value>,
    #  "useiip":<String_value>,
    #  "clientdebug":<String_value>,
    #  "loginscript":<String_value>,
    #  "logoutscript":<String_value>,
    #  "wihome":<String_value>,
    #  "wihomeaddresstype":<String_value>,
    #  "citrixreceiverhome":<String_value>,
    #  "wiportalmode":<String_value>,
    #  "epaclienttype":<String_value>,
    #  "iipdnssuffix":<String_value>,
    #  "forcedtimeout":<Double_value>,
    #  "forcedtimeoutwarning":<Double_value>,
    #  "ntdomain":<String_value>,
    #  "emailhome":<String_value>,
    #  "clientlessmodeurlencoding":<String_value>,
    #  "clientlesspersistentcookie":<String_value>,
    #  "allowedlogingroups":<String_value>,
    #  "securebrowse":<String_value>,
    #  "storefronturl":<String_value>,
    #  "sfgatewayauthtype":<String_value>,
    #  "kcdaccount":<String_value>,
    #  "rdpclientprofilename":<String_value>,
    #  "windowspluginupgrade":<String_value>,
    #  "macpluginupgrade":<String_value>,
    #  "linuxpluginupgrade":<String_value>,
    #  "iconwithreceiver":<String_value>,
    #  "autoproxyurl":<String_value>,
    #  "pcoipprofilename":<String_value>
     }
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("\nAdding VPN Session Action: %s" % response.reason)
   print ("Response: %s" % response.text)

def addVpnSessionPolicy(connectiontype,nitroNSIP,authToken,vpnsessionpolicy_name, rule, action):
   url = '%s://%s/nitro/v1/config/vpnsessionpolicy' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "vpnsessionpolicy": {
      "name": vpnsessionpolicy_name,
      "rule": rule,
      "action": action
     }
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("\nAdding VPN Session Policy: %s" % response.reason)
   print ("Response: %s" % response.text)

def addVpnvserver(connectiontype,nitroNSIP,authToken,vserver_name,vserver_servicetype,vserver_ipv46,vserver_port,icaonly,tcpprofilename,certkeynames,downstateflush,listenpolicy):
   url = '%s://%s/nitro/v1/config/vpnvserver' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "vpnvserver": {
      "name": vserver_name,
      "servicetype": vserver_servicetype,
      "ipv46": vserver_ipv46,
      "port": vserver_port,
      #"certkeynames": certkeynames,
      #"range":<Double_value>,
      #"state":<String_value>,
      #"authentication":<String_value>,
      #"doublehop":<String_value>,
      #"maxaaausers":<Double_value>,
      #"icaonly":<String_value>,
      #"icaproxysessionmigration":<String_value>,
      #"dtls":<String_value>,
      #"loginonce":<String_value>,
      #"advancedepa":<String_value>,
      #"devicecert":<String_value>,
      "downstateflush": downstateflush,
      "listenpolicy": listenpolicy,
      #"listenpriority":<Double_value>,
      #"tcpprofilename":<String_value>,
      #"httpprofilename":<String_value>,
      #"comment":<String_value>,
      #"appflowlog":<String_value>,
      #"icmpvsrresponse":<String_value>,
      #"rhistate":<String_value>,
      #"netprofile":<String_value>,
      #"cginfrahomepageredirect":<String_value>,
      #"maxloginattempts":<Double_value>,
      #"failedlogintimeout":<Double_value>,
      #"l2conn":<String_value>,
      #"deploymenttype":<String_value>,
      #"rdpserverprofilename":<String_value>,
      #"windowsepapluginupgrade":<String_value>,
      #"linuxepapluginupgrade":<String_value>,
      #"macepapluginupgrade":<String_value>,
      #"logoutonsmartcardremoval":<String_value>,
      #"userdomains":<String_value>,
      #"authnprofile":<String_value>,
      #"vserverfqdn":<String_value>,
      #"pcoipvserverprofilename":<String_value>
     }
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("\nAdding VPN Vserver: %s" % response.reason)
   print ("Response: %s" % response.text)

def addVpnVserver_SessionPolicy_binding(connectiontype,nitroNSIP,authToken,vserver_name,policy,priority,secondary,groupextraction,gotopriorityexpression, bindpoint):
   url = '%s://%s/nitro/v1/config/vpnvserver_vpnsessionpolicy_binding' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "vpnvserver_vpnsessionpolicy_binding": {
      "name": vserver_name,
      "policy": policy,
      "priority": priority,
      #"secondary": secondary,
      #"groupextraction": groupextraction,
      #"gotopriorityexpression": gotopriorityexpression,
      #"bindpoint": bindpoint,
     }
   }
   payload = json.dumps(json_string)
   response = requests.put(url, data=payload, headers=headers, verify=False)
   print ("\nBinding VPN Session Policy to Vpnvserver: %s" % response.reason)
   print ("Response: %s" % response.text)

def addVpnVserver_Vpnportaltheme_binding(connectiontype,nitroNSIP,authToken,vserver_name,portaltheme):
   url = '%s://%s/nitro/v1/config/vpnvserver_vpnportaltheme_binding' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "vpnvserver_vpnportaltheme_binding": {
      "name": vserver_name,
      "portaltheme": portaltheme,
     }
   }
   payload = json.dumps(json_string)
   response = requests.put(url, data=payload, headers=headers, verify=False)
   print ("\nBinding VPN portaltheme to Vpnvserver: %s" % response.reason)
   print ("Response: %s" % response.text)

def addVpnVserver_AuthLdapPolicy_binding(connectiontype,nitroNSIP,authToken,vserver_name,policy,priority,secondary,groupextraction,gotopriorityexpression, bindpoint):
   url = '%s://%s/nitro/v1/config/vpnvserver_authenticationldappolicy_binding' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "vpnvserver_authenticationldappolicy_binding": {
      "name": vserver_name,
      "policy": policy,
      "priority": priority,
      #"secondary": secondary,
      #"groupextraction": groupextraction,
      #"gotopriorityexpression": gotopriorityexpression,
      #"bindpoint": bindpoint,
     }
   }
   payload = json.dumps(json_string)
   response = requests.put(url, data=payload, headers=headers, verify=False)
   print ("\nBinding Authentication LDAP Policy to Vpnvserver: %s" % response.reason)
   print ("Response: %s" % response.text)
