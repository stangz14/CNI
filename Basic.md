# 1. ลำดับโหมดการทำงาน (Operation Modes)
ก่อนเริ่ม config ต้องเข้าใจลำดับชั้นของโหมดต่างๆ:
1. **User EXEC Mode** (`Switch>`): โหมดแรกเมื่อเข้าอุปกรณ์ ทำอะไรไม่ได้มากนอกจากดูค่าเบื้องต้น 
2. **Privileged EXEC Mode** (`Switch#`): โหมดสิทธิ์ผู้ดูแลระบบ ใช้ดูค่า config (show) และสั่ง reload ได้ 
3. **Global Configuration Mode** (`Switch(config)#`): โหมดสำหรับแก้ไขการตั้งค่าของอุปกรณ์

# 2. การตั้งค่าชื่ออุปกรณ์และการเข้าโหมด Config การเปลี่ยน Hostname ช่วยให้เราแยกแยะอุปกรณ์ในระบบเครือข่ายได้ง่ายขึ้น

```cisco
Switch> enable ! เข้าสู่ Privileged Mode 
Switch# configure terminal ! เข้าสู่ Global Configuration Mode 
Switch(config)# hostname R1-Main ! เปลี่ยนชื่ออุปกรณ์เป็น R1-Main 
R1-Main(config)#
``````