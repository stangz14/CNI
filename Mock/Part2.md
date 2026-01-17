# Instructions
## Basic Connectivity

1. [0.5 คะแนน] PC-1 สามารถ Ping IPv4 Switch ได้
2. [0.5 คะแนน] PC-1 สามารถ Ping IPv4 PC-2 ได้
3. [0.5 คะแนน] PC-1 สามารถ Ping IPv4 Router1 (E0/0) ได้
4. [0.5 คะแนน] PC-2 สามารถ Ping IPv4 Switch ได้
5. [0.5 คะแนน] PC-1 สามารถ Ping IPv4 1.1.1.1 ได้
6. [0.5 คะแนน] PC-2 สามารถ Ping IPv4 1.1.1.1 ได้
  
**จำเป็นต้องตั้งชื่อ Hostname Label ใน GNS3 ให้ตรงที่โจทย์กำหนดเท่านั้น เช่น router1 ต้องมี Label เป็น router1**

# ubuntu1
```Bash
#
# This is a sample network config, please uncomment lines to configure the network
#

# Uncomment this line to load custom interface files
# source /etc/network/interfaces.d/*

# Static config for eth0
auto eth0
iface eth0 inet static
	address 172.16.227.130
	netmask 255.255.255.224
	gateway 172.16.227.129
	up echo nameserver 8.8.8.8 > /etc/resolv.conf

# DHCP config for eth0
#auto eth0
#iface eth0 inet dhcp
#	hostname ubuntu1
```
# ubuntu2
```Bash
#
# This is a sample network config, please uncomment lines to configure the network
#

# Uncomment this line to load custom interface files
# source /etc/network/interfaces.d/*

# Static config for eth0 (ปิดการใช้งานส่วนนี้)
#auto eth0
#iface eth0 inet static
#	address 172.61.227.130
#	netmask 255.255.255.224
#	gateway 172.61.227.129
#	up echo nameserver 8.8.8.8 > /etc/resolv.conf

# DHCP config for eth0 (เปิดใช้งานส่วนนี้)
auto eth0
iface eth0 inet dhcp
	hostname ubuntu1
```
# Switch
## Create Vlan and No shut
```cisco
# conf t
(config)# vlan 227
(config-vlan)# ex
(config)# vlan 181
(config-vlan)# ex
(config)# int vlan 227
(config-if)# no shut
(config-if)# ip add 172.16.227.158 255.255.255.224
(config-if)# ex
(config)# int vlan 181
(config-if)# no shut
(config-if)# ip add 172.16.181.254 255.255.255.192
(config-if)# ex
(config)# do wr
```
## Select Mode interface
```cisco
(config)# int e0/1
(config-if)# switchport mode access
(config-if)# switchport access vlan 227
(config)# exit
(config)# int e0/2
(config-if)# switchport mode access
(config-if)# switchport access vlan 181
(config)# exit
(config)# int e0/0
(config-if)# switchport trunk encapsulation dot1Q
(config-if)# switchport mode trunk
(config-if)# exit
(config)# do wr
```
# Router1
# Add ip
```cisco
# conf t
(config)# int e0/1
(config-if)# no shut
(config-if)# ip address dhcp
(config-if)# ex
(config)# int e0/0
(config-if)# no shut
(config-if)# ip address 192.168.1.1 255.255.255.0
(config-if)# ex
(config)# do wr
```
# Routing
```cisco
(config)# ip route 172.16.227.128 255.255.255.224 192.168.1.254
(config)# ip route 172.16.181.192 255.255.255.192 192.168.1.254
(config)# do wr
```
# PAT
```cisco
(config)# ip access-list standard net
(config-std-ncal)# permit any
(config-std-ncal)# ex
(config)# int e0/0
(config-if)# ip nat inside
(config-if)# ex
(config)# int e0/1
(config-if)# ip nat outside
(config-if)# ex
(config)# ip nat inside source list net interface e0/1np overload
(config)# do wr
```
# DHCP
```cisco
(config)# ip dhcp excluded-address 172.16.181.193 172.16.181.196
(config)# ip dhcp excluded-address 172.16.181.201 172.16.181.254
(config)# ip dhcp pool itkmitl
(dhcp-config)# network 172.16.181.192 255.255.255.192
(dhcp-config)# default-router 172.16.181.193
(dhcp-config)# dns-server 192.168.1.1
(config-if)# exit
(config)# do wr
```
# Router2
# Add ip
```
# conf t
(config)# int e0/1
(config-if)# no shut
(config-if)# ip address 192.168.1.254 255.255.255.0
(config-if)# ex
(config)# int e0/0
(config-if)# no shut
(config-if)# ex
(config)# int e0/0.227
(config-subif)# encapsulation dot1q 227
(config-subif)# ip add 172.16.227.129 255.255.255.224
(config-subif)# no shut
(config-subif)# exit
(config)# int e0/0.181
(config-subif)# encapsulation dot1q 181
(config-subif)# ip add 172.16.181.193 255.255.255.192
(config-subif)# no shut
(config-subif)# exit
(config)# do wr
```

# Routing
```cisco
(config)# ip route 0.0.0.0 0.0.0.0 192.168.1.1
(config)# do wr
```
# DHCP
```cisco
(config)# int e0/0.181
(config-subif)# ip helper-address 192.168.1.1
(config-subif)# ex
(config)# do wr
```