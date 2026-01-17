# Instructions
## Basic Connectivity
1. DNS service
    1. เปิด DNS Service ที่ Router1 และทำให้ ubuntu1 สามารถ Ping Switch ด้วยชื่อ `SW.itkmitl.lab` ได้
    2. ตั้งค่า DNS ที่ Router1 และให้ ubuntu2 ให้สามารถ curl ไปที่ WebServer IP `10.70.38.253` ด้วย `http://web.itkmitl.lab` ได้
2. เปิด TFTP Service ที่ ubuntu1 และให้ Backup running-config ของ Router1 มาเก็บที่ ubuntu1
3. เปิด Telnet Service ที่ Switch และให้ ubuntu2 สามารถ Telnet มาที่ Switch ได้
4. ใช้คำสั่ง Curl จาก ubuntu1 ไปที่ Internet เช่น [www.google.com](http://www.google.com/) สำเร็จ โดยให้ตั้งค่า Router2 Relay DNS ไปที่ Public DNS Server เช่น 8.8.8.8

# DNS
## Router1
```cisco
(config)# ip dns server
(config)# ip domain-lookup
(config)# ip dns primary itkmitl.lab soa ns1.itkmitl.lab
(config)# ip host SW.itkmitl.lab 172.16.227.158
(config)# ip host web.itkmit.lab 10.70.38.253
(config)# ip name-server 8.8.8.8
```