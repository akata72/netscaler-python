import json, requests, base64, sys, os, re
requests.urllib3.disable_warnings()

#### SAML Authentication related ####

def addAuthSamlAction(connectiontype,nitroNSIP,authToken,name,samlidpcertname,samlredirecturl, samlrejectunsignedassertion, samlissuername, samltwofactor,signaturealg, digestmethod, samlbinding, logouturl, skewtime, logoutbinding, forceauthn):
   url = '%s://%s/nitro/v1/config/authenticationsamlaction' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "authenticationsamlaction": {
      "name": name,
      "samlidpcertname": samlidpcertname,
      #"samlsigningcertname": samlsigningcertname,
      "samlredirecturl": samlredirecturl,
      #"samlacsindex": samlacsindex,
      #"samluserfield": samluserfield,
      "samlrejectunsignedassertion" : samlrejectunsignedassertion,
      "samlissuername": samlissuername,
      "samltwofactor": samltwofactor,
      #"defaultauthenticationgroup": defaultauthenticationgroup,
      "signaturealg": signaturealg,
      "digestmethod": digestmethod,
      #"requestedauthncontext": requestedauthncontext,
      #"authnctxclassref":authnctxclassref,
      "samlbinding" : samlbinding,
      #"attributeconsumerserviceindex", attributeconsumerserviceindex,
      #"sendthumbprint": sendthumbprint,
      #"enforceusername": enforceusername,
      "logouturl": logouturl,
      #"artifactresolutionserviceurl":artifactresolutionserviceurl,
      "skewtime": skewtime,
      "logoutbinding": logoutbinding,
      #"forceauthn": forceauthn,
      #"groupnamefield": groupnamefield,
      #"audience": audience,   
     }
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("\nAdding Authentication SAML Server(Action): %s" % response.reason)
   print ("Response: %s" % response.text)

def addAuthSamlPolicy(connectiontype,nitroNSIP,authToken,name,rule,reqaction):
   url = '%s://%s/nitro/v1/config/authenticationsamlpolicy' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "authenticationsamlpolicy": {
       "name": name,
       "rule": rule,
       "reqaction": reqaction, 
     }
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("\nAdding Authentication SAML Policy: %s" % response.reason)
   print ("Response: %s" % response.text)

def addAuthSamlIdpProfile(connectiontype,nitroNSIP,authToken,name):
   url = '%s://%s/nitro/v1/config/authenticationsamlidpprofile' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "authenticationsamlidpprofile": {
       "name": name,
    # not completed
     }
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("\nAdding Authentication SAML Policy: %s" % response.reason)
   print ("Response: %s" % response.text)

def addAuthenticationSamlIdpProfile(connectiontype,nitroNSIP,authToken,samlprofilename,samlspcertname,samlidpcertname,assertionconsumerserviceurl,relaystaterule,samlissuername,rejectunsignedrequests,signaturealg,digestmethod,audience,nameidformat,nameidexpr,encryptassertion,encryptionalgorithm,samlbinding,skewtime,serviceproviderid,signassertion,keytransportalg,splogouturl,logoutbinding,defaultauthenticationgroup):
   url = '%s://%s/nitro/v1/config/authenticationsamlidpprofile' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "authenticationsamlidpprofile": {
      "name": samlprofilename,
      #"samlspcertname": samlspcertname,
      "samlidpcertname": samlidpcertname,
      "assertionconsumerserviceurl": assertionconsumerserviceurl,
      #"relaystaterule": relaystaterule,
      "samlissuername": samlissuername,
      "rejectunsignedrequests" : rejectunsignedrequests,
      "signaturealg": signaturealg,
      "digestmethod": digestmethod,
      #"audience": audience,
      #"nameidformat": nameidformat,
      #"nameidexpr": nameidexpr,
      "encryptassertion": encryptassertion,
      "encryptionalgorithm": encryptionalgorithm,
      "samlbinding" : samlbinding,
      "skewtime": skewtime,
      "serviceproviderid": serviceproviderid,
      "signassertion":signassertion,
      "keytransportalg": keytransportalg,
      "splogouturl": splogouturl,
      "logoutbinding": logoutbinding,
      #"defaultauthenticationgroup": defaultauthenticationgroup,
     }
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("\nAdding Authentication SAML Idp Profile: %s" % response.reason)
   print ("Response: %s" % response.text)

#### LDAP Authentication related ####

def addAuthLdapAction(connectiontype,nitroNSIP,authToken,ldapaction_name,ldap_serverip,ldap_serverport,ldapbase,ldapbinddn,ldapbinddnpassword,ldaploginname,searchfilter,groupattrname,subattributename,sectype,passwdchange):
   url = '%s://%s/nitro/v1/config/authenticationldapaction' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "authenticationldapaction": {
      "name": ldapaction_name,
      "serverip": ldap_serverip,
      #"servername":<String_value>,
      "serverport": ldap_serverport,
      #"authtimeout":<Double_value>,
      "ldapbase": ldapbase,
      "ldapbinddn": ldapbinddn,
      "ldapbinddnpassword":ldapbinddnpassword,
      "ldaploginname":ldaploginname,
      "searchfilter": searchfilter,
      "groupattrname": groupattrname,
      "subattributename": subattributename,
      "sectype": sectype,
      #"svrtype":<String_value>,
      #"ssonameattribute":<String_value>,
      #"authentication":<String_value>,
      #"requireuser":<String_value>,
      "passwdchange": passwdchange,
      #"nestedgroupextraction":<String_value>,
      #"maxnestinglevel":<Double_value>,
      #"followreferrals":<String_value>,
      #"maxldapreferrals":<Double_value>,
      #"referraldnslookup":<String_value>,
      #"mssrvrecordlocation":<String_value>,
      #"validateservercert":<String_value>,
      #"ldaphostname":<String_value>,
      #"groupnameidentifier":<String_value>,
      #"groupsearchattribute":<String_value>,
      #"groupsearchsubattribute":<String_value>,
      #"groupsearchfilter":<String_value>,
      #"defaultauthenticationgroup":<String_value>,
     }
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("\nAdding Authentication LDAP Action: %s" % response.reason)
   print ("Response: %s" % response.text)

def addAuthLdapPolicy(connectiontype,nitroNSIP,authToken,ldappolicy_name,ldappolicy_rule,ldappolicy_reqaction):
   url = '%s://%s/nitro/v1/config/authenticationldappolicy' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "authenticationldappolicy": {
      "name": ldappolicy_name,
      "rule": ldappolicy_rule,
      "reqaction": ldappolicy_reqaction,
     }
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("\nAdding Authentication LDAP Policy: %s" % response.reason)
   print ("Response: %s" % response.text)
