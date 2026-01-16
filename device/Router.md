# Basic
# Add ip router
```cisco
(config)# interface [interface]
(config-if)# description 
(config-if)# ip address [ip] [subnetmask]
(config-if)# no shutdown
(config-if)# exit
```
## Add ip in Subinterface
```cisco
(config)# int [interface_id]
(config-if)# no shut
(config-if)# exit
(config)# int [interface_id].[vlan_id]
(config-subif)# encapsulation dot1Q [vlan]
(config-subif)# ip address [ip] [subnetmask]
(config-subif)# exit
```