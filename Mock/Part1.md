# Instructions
## IP Assignment

**Subnet**
ใส่ค่าลงในตารางด้านล่าง และ configure อุปกรณ์ ให้ถูกต้องครบถ้วน ตามข้อกำหนดต่อไปนี้
1. กำหนดให้ IPv4 เป็นค่า `[172.X.Y.128/25]` และกำหนดให้ **VLAN A กับ B โดย X, Y, A, B จะเป็นเลขที่ถูกสุ่มขึ้นมาของแต่ละคน**
    - Subnet แรก: VLAN A ที่มี ubuntu1 และ Switch มี IP ที่สามารถใช้งานได้อย่างน้อย `30` IP และต้องใกล้เคียงมากที่สุด
    - Subnet แรก: VLAN B ที่มี ubuntu2 มี IP ที่สามารถใช้งานได้อย่างน้อย `50` IP และต้องใกล้เคียงมากที่สุด
    ให้แบ่ง Subnet VLAN `A` ที่มี ubuntu1 ก่อน ดังนั้นค่า Subnet Number ของ VLAN `A` จะต้องน้อยกว่า Subnet Number ของ VLAN `B`
2. กำหนดให้ IPv4 Network ระหว่าง Router1 และ Router2 เป็น [192.168.1.0/24]

---

**IPv4**

- IPv4 ของ `Router1` และ `Router2` มี Host ID ที่สามารถใช้ได้ เป็น Host ลำดับที่ `1` ของ Subnet นั้น ยกเว้น Interface E0/1 ของ `Router2` ให้ใช้ Host ลำดับสุดท้ายของ Subnet นั้น
- IPv4 ของ `ubuntu1` มี Host ID ที่สามารถใช้ได้ เป็น Host ลำดับที่ 2 ที่สามารถใช้ได้ใน Subnet นั้น (DNS Server คือ Router1)
- `ubuntu2`, ได้รับ IPv4, Subnet Mask, Gateway, DNS ผ่าน DHCPv4 จาก Router1 โดยต้องได้ IPv4 ที่มี Host ID ที่สามารถใช้ได้ เป็นลำดับที่ `5-10` ของ Subnet นั้นเท่านั้น (DNS Server คือ Router1)
- IPv4 ของ `Switch` มี Host ID ที่สามารถใช้ได้ เป็น Host ลำดับ `สุดท้าย` ของ Subnet นั้น

***
# Network Variables
| Variable | VLAN ID | Variable | Network (CIDR)  |
| -------- | ------- | -------- | --------------- |
| VLAN A   | 227     | CIDR Q   | 172.16.0.128/27 |
| VLAN B   | 181     | CIDR R   | 172.16.0.192/26 |
| VLAN C   | 6       | CIDR S   | 172.16.0.0/24   |

***
### Your Devices
| Device (Management Interface) | Management IP |
| ----------------------------- | ------------- |
| switch                        | Not assigned  |
| router1 (GigabitEthernet0/0)  | 10.70.38.146  |
| router2                       | Not assigned  |
| ubuntu1                       | Not assigned  |
| ubuntu2                       | Not assigned  |

***
# Table
| Device.Interface | IPv4           | Subnet Mask     | Default Gateway | DNS         |
| ---------------- | -------------- | --------------- | --------------- | ----------- |
| router1.eth_0    | 192.168.1.1    | 255.255.255.0   | -               | -           |
| router2.eth0_0_a | 172.16.227.129 | 255.255.255.224 | -               | -           |
| router2.eth0_0_b | 172.16.181.193 | 255.255.255.192 | -               | -           |
| router2.eth0_1   | 192.168.1.254  | 255.255.255.0   | 192.168.1.1     | -           |
| switch.sw_vlan_a | 172.16.227.158 | 255.255.255.224 | 172.16.227.129  | -           |
| ubuntu1.eth0     | 172.16.227.130 | 255.255.255.224 | 172.16.227.129  | 192.168.1.1 |
| ubuntu2.eth0     | 172.16.181.197 | 255.255.255.192 | 172.16.181.193  | 192.168.1.1 |
