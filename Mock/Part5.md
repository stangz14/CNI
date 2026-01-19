# Instructions
## **IPv6**

**ให้ IPv6 ของนักศึกษาเป็น** **2001:6707:รหัสนศ.สามตัวท้าย:เลข VLAN ที่ได้::Interface ID**

- ใช้ Prefix Length /64 bits ทุก Subnet **ตอนตอบในตารางให้ใส่ / ด้วย เช่น /64
- IPv6 ของ Router1 มี Interface ID = 1 เสมอ
- IPv6 ของ Router2 มี Interface ID = 1 เสมอ ยกเว้น Interface E0/1 ให้ใช้ Interface ID = 2
- GUA IPv6 ของ ubuntu1 มี Interface ID = 2 เสมอ
- GUA IPv6 ของ ubuntu2 ได้รับ IPv6 ผ่านทาง SLAAC **โปรด Config ให้ ubuntu2 ได้รับค่าก่อน เพื่อนำมาใส่ในตารางเนื่องจากจำเป็นต้องใช้ในการตรวจ Part ถัด ๆ ไป**
- Link Local ใช้ FE80:: ทั้งหมดทุก Link และให้ Router ใช้ Interface ID = 1 ทั้งหมด ยกเว้น ที่ Router2 Interface E0/1 ให้ใช้ Interface ID = 2
- ให้ Interface ที่ Router1 และ Router2 เชื่อมกัน เป็น 2001:6707:รหัสนศ.สามตัวท้าย:เลข VLAN C::interface ID ตามตาราง
- ค่า Default Gateway IPv6 address ของ ubuntu1, ubuntu2 และ Switch ให้ใช้ค่า Link Local Address
- Switch อยู่ใน Subnet เดียวกับ VLAN A และ GUA IP ของ Switch มี Interface ID = 3 เสมอ
- **ไม่มี IPv6 ใน Cloud ที่เชื่อมต่อไปยัง Instructor Pod และ Internet**

### Network Variables

|Variable|VLAN ID|Variable|Network (CIDR)|
|---|---|---|---|
|VLAN A|227|CIDR Q|172.16.0.128/27|
|VLAN B|181|CIDR R|172.16.0.192/26|
|VLAN C|6|CIDR S|172.16.0.0/24|

# Table
| Device.Interface | GUA                  | Prefix-Length | Link-Local Address | Gateway |
| ---------------- | -------------------- | ------------- | ------------------ | ------- |
| router1.eth_0    | 2001:6707:182:6::1   | /64           | FE80::1            | N/A     |
| router2.eth0_0_a | 2001:6707:182:227::1 | /64           | FE80::1            | N/A     |
| router2.eth0_0_b | 2001:6707:182:181::1 | /64           | FE80::1            | N/A     |
| router2.eth0_1   | 2001:6707:182:6::1   | /64           | FE80::2            | N/A     |
| switch.sw_vlan_a | 2001:6707:182:227::3 | /64           | FE80::3            | FE80::1 |
| ubuntu1.eth0     | 2001:6707:182:227::2 | /64           | FE80::2            | FE80::1 |
| ubuntu2.eth0     | 2001:6707:182:227::2 | /64           | N/A                | FE80::1 |
