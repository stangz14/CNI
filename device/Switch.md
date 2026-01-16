# Basic
## Add Defaul-gateway
```cisco
ip defaul-gateway {ip_address}
```
# Vlan
## Check Vlan
```cisco
# show vlan
```
## Create Vlan
```cisco
# conf t
(config)# vlan [vlan_id]
(config)# name [name] ! ตั้งชื่อ vlan
(config)# exit
```
## Add ip Vlan
```cisco
# conf t
(config)# int vlan [vlan_id]
(config-if)# no shut
(config-if)# ip add [ip] [subnetmask]
(config)# exit
```
# Select Mode Interface Switch
## Access สายละ 1 vlan
```cisco
# conf t
(config)# int [interface_id]
(config-if)# switchport mode access
(config-if)# switchport access vlan [vlan_id]
(config)# exit
```
## Trunk 1 สายไปได้หลาย vlan
```cisco
# conf t
(config)# int [interface_id]
(config-if)# switchport trunk encapsulation dot1Q
(config-if)# switchport mode trunk
(config)# exit
```
