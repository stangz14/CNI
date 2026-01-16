# Vlan
## ตรวจสอบ Vlan
```cisco
# show vlan
```
## สร้าง Vlan
```cisco
# conf t
(config)# vlan [vlan_id]
(config)# name [name] ! ตั้งชื่อ vlan
(config)# exit
```
## กำหนด ip ใน vlan
```cisco
# conf t
(config)# int vlan [vlan_id]
(config-if)# no shut
(config-if)# ip add [ip] [subnetmask]
(config)# exit
```
# กำหนด mode ในสาย
## access สายละ 1 vlan
```cisco
# conf t
(config)# int [interface_id]
(config-if)# switchport mode access
(config-if)# switchport access vlan [vlan_id]
(config)# exit
```
## trunk
```cisco
# conf t
(config)# int [interface_id]
(config-if)# switchport trunk encapsulation dot1Q
(config-if)# switchport mode trunk
(config)# exit
```
