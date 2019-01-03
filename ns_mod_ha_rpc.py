import json, requests, base64, sys, os, re
requests.urllib3.disable_warnings()

#### HA/rpc tasks ####
def addHaNode(connectiontype,nitroNSIP,authToken,ha_id, ha_ipaddress, ha_inc):
   url = '%s://%s/nitro/v1/config/hanode' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "hanode": {
       "id": ha_id,
       "ipaddress": ha_ipaddress,
       "inc": ha_inc,}
   }
   payload = json.dumps(json_string)
   response = requests.post(url, data=payload, headers=headers, verify=False)
   print ("\nAdding HA Node: %s" % response.reason)
   print ("Response: %s" % response.text)

def updateNsRpcNode(connectiontype,nitroNSIP,authToken,rpc_ipaddress,rpc_password,rpc_srcip,rpc_secure):
   url = '%s://%s/nitro/v1/config/nsrpcnode' % (connectiontype, nitroNSIP)
   headers = {'Content-type': 'application/json','Cookie': authToken}
   json_string = {
   "nsrpcnode": {
       "ipaddress": rpc_ipaddress,
       "password": rpc_password,
       #"srcip": rpc_srcip,
       "secure": rpc_secure,
      }
   }
   payload = json.dumps(json_string)
   response = requests.put(url, data=payload, headers=headers, verify=False)
   print ("Updating RPC Node: %s" % response.reason)
   print ("Response: %s" % response.text)