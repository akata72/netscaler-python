import json, requests, base64, sys, os, re
requests.urllib3.disable_warnings()

def getAuthCookie(connectiontype,nitroNSIP,nitroUser,nitroPass):
   url = '%s://%s/nitro/v1/config/login' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/vnd.com.citrix.netscaler.login+json'}
   json_string = {
       "login":{
       "username":nitroUser,
       "password":nitroPass,
       }
   }
   payload = json.dumps(json_string)
   try:
     response = requests.post(url, data=payload, headers=headers, verify=False, timeout=1.0)
     response.raise_for_status()      
   except requests.exceptions.RequestException as e:
     print(e)
     sys.exit(1)
   except requests.exceptions.HTTPError as err:
     print(err)
     sys.exit(1)
    
   cookie = response.cookies['NITRO_AUTH_TOKEN']
   nitroCookie = 'NITRO_AUTH_TOKEN=%s' % cookie
   print ("Creating Authentication Token: %s" % response.reason)
   return nitroCookie 
   
def logOut(connectiontype,nitroNSIP,authToken):
   url = '%s://%s/nitro/v1/config/logout' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/vnd.com.citrix.netscaler.logout+json','Cookie': authToken}
   json_string = {
       "logout":{}
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("\nLogging Out: %s" % response.reason)
   
def saveNsConfig(connectiontype,nitroNSIP,authToken):
   url = '%s://%s/nitro/v1/config/nsconfig?action=save' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
       "nsconfig":{}
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("\nSaving Netscaler Configuration: %s" % response.reason)


#### File handling ####
def sendFile(connectiontype,nitroNSIP,authToken,nscert,localcert,nscertpath):
   url = '%s://%s/nitro/v1/config/systemfile' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/vnd.com.citrix.netscaler.systemfile+json','Cookie': authToken}
   f = open(localcert, 'r')
   filecontent = base64.b64encode(f.read())
   json_string = {
   "systemfile": {
       "filename": nscert,
       "filelocation": nscertpath,
       "filecontent":filecontent,
       "fileencoding": "BASE64",}
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("UPLOADING %s: %s") % (nscert, response.reason)


def enable_nsfeature(connectiontype,nitroNSIP,authToken,feature):
   url = '%s://%s/nitro/v1/config/nsfeature?action=enable' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "nsfeature": {
      "feature": feature,
     }
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("\nEnabling nsfeature %s: %s" % (feature, response.reason))
   print ("Response: %s" % response.text)


#### dns,ntp related tasks ####

def addNtpServer(connectiontype,nitroNSIP,authToken,ntp_serverip):
   url = '%s://%s/nitro/v1/config/ntpserver' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "ntpserver": {
       "serverip": ntp_serverip,
     #  "servername": servername,
     #  "minpoll" : minpoll,
     #  "maxpoll" : maxpoll,
     #  "autokey" : autokey,
     #  "key" : key,
     }
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("\nAdding NTP Server: %s" % response.reason)
   print ("Response: %s" % response.text)

def addDnsNameServer(connectiontype,nitroNSIP,authToken,dns_serverip,dnsvservername,dns_local,dns_state,dns_type,dnsprofilename):
   url = '%s://%s/nitro/v1/config/dnsnameserver' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "dnsnameserver": {
      "ip": dns_serverip,
      #"dnsvservername": dnsvservername,
      #"local": dns_local,
      #"state": dns_state,
      #"type": dns_type,
      #"dnsprofilename": dnsprofilename,
     }
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("\nAdding DNS Server: %s" % response.reason)
   print ("Response: %s" % response.text)
