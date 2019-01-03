#!/usr/bin/env python
import json, requests, base64, sys, os, re
requests.urllib3.disable_warnings()

#### Enable Responder feature ####
def EnableResponder(connectiontype,nitroNSIP,authToken):
   url = '%s://%s/nitro/v1/config/nsfeature?action=enable' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "nsfeature": {
      "feature": "responder",
     }
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("\nEnabling nsfeature %s: " % (response.reason))
   print ("Response: %s" % response.text)

#### Disable Responder feature ####
def DisableResponder(connectiontype,nitroNSIP,authToken):
   url = '%s://%s/nitro/v1/config/nsfeature?action=disable' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "nsfeature": {
      "feature": "responder",
     }
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("\nDisabling Responder feature %s:" % (response.reason))
   print ("Response: %s" % response.text)

#### Create nsip vip for letsencrypt ####
def CreateNSIPVIP(connectiontype,nitroNSIP,authToken,vserver_ipv46,nsipvip_mask,nsipvip_type):
   url = '%s://%s/nitro/v1/config/nsip' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "nsip": {
      "ipaddress": vserver_ipv46,
      "netmask": nsipvip_mask,
      "type": nsipvip_type,
     }
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("\nCreating NSIP VIP %s: %s" % (vserver_ipv46, response.reason))
   print ("Response: %s" % response.text)

#### Create ipset for letsencrypt ####
def CreateIpSet(connectiontype,nitroNSIP,authToken,ipset_name):
   url = '%s://%s/nitro/v1/config/ipset' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "ipset": {
      "name": ipset_name,
     }
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("\nCreating IPset %s: %s" % (ipset_name, response.reason))
   print ("Response: %s" % response.text)

#### Bind ipset for letsencrypt ####
def BindIpSet(connectiontype,nitroNSIP,authToken,ipset_name,vserver_ipv46):
   url = '%s://%s/nitro/v1/config/ipset_nsip_binding' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "ipset_nsip_binding": {
      "name": ipset_name,
      "ipaddress": vserver_ipv46,
     }
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("\nBind IPset %s to %s: %s" % (ipset_name, vserver_ipv46, response.reason))
   print ("Response: %s" % response.text)

#### Create content switch vserver for letsencrypt ####
def CreateCSV(connectiontype,nitroNSIP,authToken,csvserver_name,csvserver_IPv4,csvserver_port,csvserver_svctype,ipset_name):
   url = '%s://%s/nitro/v1/config/csvserver' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "csvserver": {
      "name": csvserver_name,
      "ipv46": csvserver_IPv4,
      "port": csvserver_port,
      "servicetype": csvserver_svctype,
      "ipset": ipset_name,
     }
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("\nCreating ContentSwitch: %s" % (response.reason))
   print ("Response: %s" % response.text)

