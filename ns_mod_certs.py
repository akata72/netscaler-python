import json, requests, base64, sys, os, re
requests.urllib3.disable_warnings()

#### Certificate related tasks #### 
def createSslRsaKey(connectiontype,nitroNSIP,authToken,keyfile,bits,exponent,keyform,des,des3,password):
   url = '%s://%s/nitro/v1/config/sslrsakey?action=create' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "sslrsakey": {
      "keyfile": keyfile,
      "bits": bits,
      "exponent": exponent,
      "keyform": keyform,
      "des" : des,
      "des3": des3,
      "password": password,
     }
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("\nCreating SSL RSAKey %s: %s" % (keyfile, response.reason))
   print ("Response: %s" % response.text)

def createSslCertReq(connectiontype,nitroNSIP,authToken,reqfile,keyfile,keyform,pempassphrase,countryname,statename,organizationname,organizationunitname,localityname,commonname,emailaddress, challengepassword,companyname,digestmethod):
   url = '%s://%s/nitro/v1/config/sslcertreq?action=create' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "sslcertreq": {
      "reqfile": reqfile,
      "keyfile": keyfile,
      #"fipskeyname": fipskeyname,
      "keyform": keyform,
      "pempassphrase": pempassphrase,
      "countryname": countryname,
      "statename": statename,
      "organizationname": organizationname,
      "organizationunitname": organizationunitname,
      "localityname": localityname,
      "commonname": commonname,
      "emailaddress": emailaddress,
      "challengepassword": challengepassword,
      "companyname": companyname,
      "digestmethod": digestmethod,
     }
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("Creating SSL Certificate Request %s: %s" % (reqfile, response.reason))
   print ("Response: %s" % response.text)

def createSslCert(connectiontype,nitroNSIP,authToken,certfile,reqfile,certtype,certkeyfile,certkeyform,certpempassphrase):
   url = '%s://%s/nitro/v1/config/sslcert?action=create' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "sslcert": {
      "certfile": certfile,
      "reqfile": reqfile,
      "certtype": certtype,
      "keyfile": certkeyfile,
      "keyform": certkeyform,
      "pempassphrase": certpempassphrase,
     }
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("\nCreating SSL Certificate %s: %s" % (certfile, response.reason))
   print ("Response: %s" % response.text)

def addSslCertKey(connectiontype,nitroNSIP,authToken,certkey,cert,key,password,passplain,certificatetype):
   url = '%s://%s/nitro/v1/config/sslcertkey' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "sslcertkey": {
      "certkey": certkey,
      "cert": cert,
      "key": key,
      "password": password,
     # "fipskey":<String_value>,
     # "hsmkey":<String_value>,
     # "inform":<String_value>,
      "passplain": passplain,
     # "certificatetype": certificatetype
     # "expirymonitor":<String_value>,
     # "notificationperiod":<Double_value>,
     # "bundle":<String_value>
     }
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("\nAdding SSL Cert-Key Pair: %s" % response.reason)
   print ("Response: %s" % response.text)

def addSslService_sslCertKey_binding(connectiontype,nitroNSIP,authToken,servicename,certkeyname,ca,crlcheck,skipcaname,snicert,ocspcheck):
   url = '%s://%s/nitro/v1/config/sslservice_sslcertkey_binding' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "sslservice_sslcertkey_binding": {
      "servicename": servicename,
      "certkeyname": certkeyname,
      #"ca": ca,
      #"crlcheck": crlcheck,
      #"skipcaname": skipcaname,
      #"snicert": snicert,
      #"ocspcheck": ocspcheck,
     }
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("\nBinding SSLService to SSLCertKey-Pair: %s" % response.reason)
   print ("Response: %s" % response.text)

def addSslvserver_SslcertKey_binding(connectiontype,nitroNSIP,authToken,servicename,certkeyname,ca,crlcheck,skipcaname,snicert,ocspcheck):
   url = '%s://%s/nitro/v1/config/sslvserver_sslcertkey_binding' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "sslvserver_sslcertkey_binding": {
      "vservername": servicename,
      "certkeyname": certkeyname,
      #"ca": ca,
      #"crlcheck": crlcheck,
      #"skipcaname": skipcaname,
      #"snicert": snicert,
      #"ocspcheck": ocspcheck,
     }
   }
   payload = json.dumps(json_string)
   response = requests.put(url, data=payload, headers=headers, verify=False)
   print ("\nBinding SSLService to SSLCertKey-Pair: %s" % response.reason)
   print ("Response: %s" % response.text)
