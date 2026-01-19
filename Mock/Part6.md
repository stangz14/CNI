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
อุปกรณ์นี้ทำหน้าที่เป็นตัวเชื่อมต่อไปยังเครือข่ายภายนอก (หรือ VLAN C) และต้องรู้วิธีส่งข้อมูลไปยัง VLAN A และ B ที่อยู่หลัง Router2

- **Global Config:**
    - `ipv6 unicast-routing`: **คำสั่งสำคัญที่สุด** เปิดใช้งานฟังก์ชันการ Routing สำหรับ IPv6 บน Router (ถ้าไม่พิมพ์คำสั่งนี้ Router จะทำตัวเหมือนคอมพิวเตอร์ธรรมดา ไม่ส่งต่อแพ็กเก็ต)
- **Interface e0/0 (เชื่อมต่อกับ Router2):**
    
    - `ipv6 enable`: เปิดใช้งาน IPv6 บนอินเทอร์เฟซนี้
    - `ipv6 address fe80::1 link-local`: กำหนด Link-Local Address แบบ Manual ให้เป็น `FE80::1` (แทนที่จะใช้ค่า EUI-64 ที่จำยาก) เพื่อให้ง่ายต่อการอ้างอิงเป็น Next Hop
    - `ipv6 address 2001:6707:182:6::1/64`: กำหนด Global Unicast Address (GUA) ซึ่งเป็น IP จริงที่ใช้สื่อสารข้ามเครือข่าย ในวง VLAN C
    - `no shutdown`: เปิดการทำงานของพอร์ต
- **Routing (Static Routes):**
    - `ipv6 route 2001:6707:182:227::/64 2001:6707:182:6::2`: บอก Router1 ว่า "ถ้าจะไปหาเครือข่าย VLAN 227 (VLAN A) ให้ส่งแพ็กเก็ตไปที่ `...::2` (ซึ่งคือขาของ Router2)"
    - `ipv6 route 2001:6707:182:181::/64 2001:6707:182:6::2`: เช่นเดียวกัน สำหรับเครือข่าย VLAN 181 (VLAN B) ให้ส่งไปที่ Router2
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

อุปกรณ์นี้ทำหน้าที่เป็น Gateway ให้กับ VLAN ต่างๆ (A และ B) และส่ง Traffic ออกไปหา Router1
- **Interface e0/1 (ขา Uplink ไปหา Router1):**
    - `ipv6 address fe80::2 link-local`: กำหนด Link-Local เป็นเบอร์ 2 (เพื่อให้ไม่ชนกับ Router1 ที่ใช้เบอร์ 1)
    - `ipv6 address 2001:6707:182:6::2/64`: กำหนด IP ในวง VLAN C (วงเดียวกับ Router1)
- **Routing:**
    - `ipv6 route ::/0 2001:6707:182:6::1`: สร้าง **Default Route** (เทียบเท่า 0.0.0.0/0 ใน IPv4) บอกว่า "ถ้าไม่รู้จะส่งแพ็กเก็ตไปไหน ให้โยนไปหา Router1 (`...::1`)"
- **Sub-interfaces (การทำ Inter-VLAN Routing):**
    - **Interface e0/0.227 (สำหรับ VLAN 227/A):**
        - `encapsulation dot1Q 227`: บอกให้ Sub-interface นี้จัดการกับ Traffic ที่แปะป้าย (Tag) VLAN 227
        - `ipv6 address fe80::1 link-local`: กำหนด Link-Local เป็น `FE80::1` (ใช้ซ้ำได้เพราะอยู่คนละวง VLAN/Broadcast Domain กับขา e0/1) ซึ่งเครื่องลูกข่าย (Client) จะชี้ Gateway มาที่เบอร์นี้
        - `ipv6 address 2001:6707:182:227::1/64`: กำหนด IP Gateway หลักของวง VLAN 227
    - **Interface e0/0.181 (สำหรับ VLAN 181/B):**
        - ทำหน้าที่เหมือนกันแต่เปลี่ยนเป็น VLAN ID 181 และใช้ IP subnet `...:181::1`

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

Switch ตัวนี้ถูกตั้งค่า IP ไว้ที่ Interface VLAN (SVI) เพื่อให้ผู้ดูแลระบบสามารถ Remote (SSH/Telnet) เข้ามาจัดการได้

- **Interface vlan 227:**
    - `ipv6 enable`: เปิด IPv6
    - `ipv6 address fe80::3 link-local`: กำหนด Link-Local เป็นเบอร์ 3 (ในวง VLAN 227 นี้ Gateway คือ `fe80::1` ที่อยู่ที่ R2, ตัว Switch เลยขอใช้เบอร์ 3 เพื่อไม่ให้ชน)
    - `ipv6 address 2001:6707:182:227::3/64`: กำหนด IP Management ให้ Switch ในวง VLAN 227
- **Routing:**
    - `ipv6 route ::/0 fe80::1`: กำหนด Default Gateway ของตัว Switch เอง ให้ชี้ไปที่ `fe80::1` (ซึ่งคือขา Sub-interface e0/0.227 ของ Router2) เพื่อให้ Switch ตอบกลับ Traffic ไปยังวงอื่นได้