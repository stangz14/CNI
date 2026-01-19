| **Commands**                                        | **Description**                                                                               |
| --------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `(config)#hostname R1`                              | Router1 ตั้งชื่อเป็น R1, Router2 ตั้งชื่อเป็น R2 กรณีเป็น Switch เช่น Switch1 ตั้งชื่อเป็น S1 |
| `(config)#enable secret class`                      | ตั้งค่า Enable Secret เป็น `class`                                                            |
| `(config)#line console 0`                           | ตั้งค่า Line Console                                                                          |
| `(config-line)#exec-timeout 0 0`                    | ไม่มี Idle Timeout                                                                            |
| `(config-line)#logging synchronous`                 | แสดงข้อความก่อนถูก Interrupted อีกครั้ง                                                       |
| `(config)#ip domain-name itkmitl.lab`               | ตั้งชื่อ Domain name เป็น `itkmitl.lab`                                                       |
| `(config)#ip ssh version 2`                         | ใช้ SSH version 2                                                                             |
| `(config)#crypto key generate rsa modulus 2048`     | สร้าง RSA public/private keys (use 2048 bits)                                                 |
| `(config)#username admin privilege 15 secret cisco` | ตั้งค่า local username `admin` มี privilege login (15)<br>และ password secret `cisco`         |
| `(config)#line vty 0 15`                            | ตั้งค่า Line vty 0 15                                                                         |
| `(config-line)#login local`                         | การ Login เข้า vty 0 15 ใช้ local username/password                                           |
| `(config-line)#transport input telnet ssh`          | สามารถ telnet and SSH เข้ามาที่ Line vty ได้                                                  |
| `(config-line)#exec-timeout 0 0`                    | ไม่มี Idle Timeout                                                                            |
| `(config-line)#logging synchronous`                 | แสดงข้อความก่อนถูก Interrupted อีกครั้ง                                                       |