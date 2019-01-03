##Configuring Netscaler VPX using Python 

| Order | Description | NITRO API | Method | Operation |
|-------|-------------|:-----------:|:--------:|:--------:|
| 0.1 | Add HA Node | hanode | POST | add |
| 0.2 | Update rpcnode | nsrpcnode | PUT | add |
| 1.0 | Add NTP Server | ntpserver | POST | add |
| 1.1 | Add DNS Server | domainnameserver | POST | add |
| 1.2 | Enable ns feature ssl sslvpn | nsfeature?action=enable | PUT | |
| 2.1 | Create AlwaysON Profile | vpnalwaysonprofile | POST | add |
| 2.2 | Create Session Profile | vpnsessionaction | POST | add |
| 2.3 | Create Session Policy | vpnsessionpolicy | POST | add |
| 2.4 | Create Authentication LDAP Action | authenticationldapaction | POST | add |
| 2.5 | Create Authentication LDAP Policy | authenticationldappolicy | POST | add |
| 2.6 | Create VPN Vserver | vpnvserver | POST | add |
| 2.7 | Bind SSL Certificates to VPN vserver | sslvserver_sslcertkey_binding | PUT | add |
| 2.8 | Bind Portaltheme to VPN vserver | vpnvserver_vpnportaltheme_binding | PUT | add |
| 2.9 | Bind LDAP Policy to VPN vserver | vpnvserver_authenticationldappolicy_binding | PUT | add |
| 2.10 | Bind Session Policy to VPN vserver | vpnvserver_vpnsessionpolicy_binding | PUT | add | 

## Qualys optimization


## References
#https://www.carlstalhood.com/netscaler-gateway-12-ssl-vpn/
