# ICON
![Router|100](Router-icon.png)

# general
```cisco
(config)#hostname R1 ! ตั้งชื่อ
(config)#enable secret class ! ตั้งค่า Enable Secret เป็น class

```
# IP Address
```cisco
R1-Main(config)# interface [interface]
R1-Main(config-if)# description 
R1-Main(config-if)# ip address [ip] [subnetmask]
R1-Main(config-if)# no shutdown
R1-Main(config-if)# exit
```