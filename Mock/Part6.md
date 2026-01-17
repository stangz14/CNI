# Router1
```cisco
(config)# ipv6 unicast-routing
(config)# interface e0/0
(config-if)# ipv6 enable
! Link-Local ใช้ FE80::1 ตามโจทย์
(config-if)# ipv6 address fe80::1 link-local
! GUA สำหรับ VLAN C (6)
(config-if)# ipv6 address 2001:6707:182:6::1/64
(config-if)# no shutdown
(config-if)# exit

! สร้าง Route ไปยังวง VLAN ของ Ubuntu ผ่าน R2 (Next hop คือ R2 ขา e0/1)
(config)# ipv6 route 2001:6707:182:227::/64 2001:6707:182:6::2
(config)# ipv6 route 2001:6707:182:181::/64 2001:6707:182:6::2
```
# Router2
```cisco
(config)# ipv6 unicast-routing
(config)# interface e0/1
(config-if)# ipv6 enable
! Link-Local ID = 2 เฉพาะขานี้
(config-if)# ipv6 address fe80::2 link-local
! GUA สำหรับ VLAN C (6) เป็นเบอร์ 2
(config-if)# ipv6 address 2001:6707:182:6::2/64
(config-if)# no shutdown
(config-if)# exit

! Default Route ชี้ไปหา R1
(config)# ipv6 route ::/0 2001:6707:182:6::1

(config)# interface e0/0
(config-if)# no shutdown
(config-if)# exit

! Sub-interface VLAN 227 (VLAN A)
(config)# interface e0/0.227
(config-subif)# encapsulation dot1Q 227
! Link-Local กลับมาใช้ FE80::1
(config-subif)# ipv6 address fe80::1 link-local
! Gateway Address ของ VLAN 227
(config-subif)# ipv6 address 2001:6707:182:227::1/64
(config-subif)# exit

! Sub-interface VLAN 181 (VLAN B)
(config)# interface e0/0.181
(config-subif)# encapsulation dot1Q 181
(config-subif)# ipv6 address fe80::1 link-local
! Gateway Address ของ VLAN 181
(config-subif)# ipv6 address 2001:6707:182:181::1/64
(config-subif)# exit
```

# Switch
```cisco
(config)# interface vlan 227
(config-if)# ipv6 enable
! Link-Local ID = 3 แต่ Gateway ชี้ไป FE80::1
(config-if)# ipv6 address fe80::3 link-local
(config-if)# ipv6 address 2001:6707:182:227::3/64
(config-if)# no shutdown
(config-if)# exit

! Default Gateway IPv6
(config)# ipv6 route ::/0 fe80::1
```