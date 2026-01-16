# Topology
![Vlan_topology|500](./img/Vlan_topology.png)
# Config
## Switch
1. Create Vlan
	```cisco
	# conf t
	(config)# vlan 10
	(config-if)# name vlan10
	(config-if)# exit
	(config)# vlan 20
	(config-if)# name vlan20
	(config-if)# exit
	(config)#
	```
2. Add ip in Vlan
	```cisco
	(config)# int vlan 10
	(config-if)# no shut
	(config-if)# ip add 172.61.10.2 255.255.255.0
	(config)# exit
	(config)# int vlan 20
	(config-if)# no shut
	(config-if)# ip add 172.61.20.2 255.255.255.0
	(config)# exit
	```
3. Select Mode interface
	```cisco
	(config)# int e0/1
	(config-if)# switchport mode access
	(config-if)# switchport access vlan 10
	(config)# exit
	(config)# int e0/2
	(config-if)# switchport mode access
	(config-if)# switchport access vlan 20
	(config)# exit
	(config)# int e0/0
	(config-if)# switchport trunk encapsulation dot1Q
	(config-if)# switchport mode trunk
	(config)# exit
	```

## Router (Route on a stick)
1. no shut interface
	```cisco
	# conf t
	(config)# int e0/0
	(config-if)# no shut
	```
2. Add ip in Subinterface
	```cisco
	(config)# int e0/0.10
	(config-subif)# encapsulation dot1q 10
	(config-subif)# ip add 172.61.10.1 255.255.255.0
	(config-subif)# exit
	(config)# int e0/0.20
	(config-subif)# encapsulation dot1q 20
	(config-subif)# ip add 172.61.20.1 255.255.255.0
	(config-subif)# exit
	```
	