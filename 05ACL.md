# Basic
- ACL แบ่งออกเป็น 2 ประเภทหลักๆ คือ:
    - **Standard ACL:** กรองทราฟฟิกตาม **Source IP Address** เท่านั้น (หมายเลข 1-99 และ 1300-1999)
    - **Extended ACL:** กรองทราฟฟิกตาม **Source IP Address, Destination IP Address, Protocol (TCP/UDP), และ Port Number** (หมายเลข 100-199 และ 2000-2699)
## Wildcard
สิ่งที่ตรงกันข้ามกับ Subnet
# Config
## 1. Standard ACL (ตรวจสอบแค่ Source IP)
เหมาะสำหรับการ Block หรือ Allow IP ต้นทางแบบกว้างๆ ใช้เลข **1-99  และ 1300-1999**
- **หลักการวาง:** ควรวางให้ **ใกล้ Destination** ที่สุด (เพื่อไม่ให้ไป Block traffic ที่เขาจะไปที่อื่น)
```cisco
(config)# access-list [1-99,1300-1999] [permit/deny] [source_address] [wildcard_mask]
```
### Example
ให้เครื่อง 192.168.1.10 ห้ามออกเน็ต แต่เครื่องอื่นในวง 192.168.1.0/24 ออกได้หมด
```cisco
(config)# access-list 10 deny host 192.168.1.10
(config)# access-list 10 permit 192.168.1.0 0.0.0.255
# อย่าลืม permit ตัวอื่น เพราะบรรทัดสุดท้ายจะมี "Implicit Deny" (ห้ามหมด) ซ่อนอยู่เสมอ
```
## 2. Extended ACL (ตรวจสอบละเอียด: Protocol, Source, Destination, Port)

เหมาะสำหรับกรอง Service เจาะจง เช่น ให้เข้าเว็บได้แต่ห้าม Ping ใช้เลข **100-199**
- **หลักการวาง:** ควรวางให้ **ใกล้ Source** ที่สุด (เพื่อประหยัด Bandwidth จะได้รีบ Block ตั้งแต่ต้นทาง)
```cisco
(config)# access-list [100-199] [permit/deny] [protocol] [source] [destination] [operator port]
```
### Example
อนุญาตให้ทุกคนเข้าเว็บ Server (10.0.0.5) ผ่าน Port 80 (HTTP) ได้ แต่ห้าม Ping (ICMP)
```cisco
# อนุญาต HTTP (TCP Port 80)
(config)# access-list 100 permit tcp any host 10.0.0.5 eq 80

# (Optional) ห้าม Ping (จริงๆ ไม่ต้องเขียนก็ได้เพราะมี deny all อยู่ท้ายสุด แต่อาจเขียนเพื่อ log หรือความชัดเจน)
(config)# access-list 100 deny icmp any host 10.0.0.5

# อนุญาต traffic อื่นๆ (ถ้าต้องการ)
(config)# access-list 100 permit ip any any
```
##  3. ขั้นตอนสำคัญ: การนำไปใช้ (Applying to Interface)

สร้าง ACL เสร็จแล้วมันจะยังไม่ทำงาน จนกว่าเราจะไปสั่งผูกกับขา Interface โดยต้องเลือกว่าจะกรองตอนเข้า (**in**) หรือตอนออก (**out**) จาก Router
```cisco
(config)# interface [interface_name]
(config-if)# ip access-group [acl_number] [in/out]
```
> คำสั่งตรวจสอบ (Verification)
> `show access-lists`: ดูรายการกฎที่เราสร้าง และดูว่ามี packet match กฎไหนบ้าง (hit count)
> `show ip interface [interface_name]`: ดูว่า interface นั้นมี ACL เบอร์อะไรแปะอยู่หรือไม่
