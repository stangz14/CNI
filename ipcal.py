def ip_to_int(ip_str):
    """แปลง IP String (x.x.x.x) เป็นตัวเลข Integer 32-bit"""
    octets = ip_str.split('.')
    if len(octets) != 4:
        raise ValueError("Invalid IP Address format")
    return (int(octets[0]) << 24) + (int(octets[1]) << 16) + (int(octets[2]) << 8) + int(octets[3])

def int_to_ip(ip_int):
    """แปลงตัวเลข Integer 32-bit กลับเป็น IP String"""
    return ".".join([
        str((ip_int >> 24) & 0xFF),
        str((ip_int >> 16) & 0xFF),
        str((ip_int >> 8) & 0xFF),
        str(ip_int & 0xFF)
    ])

def calculate_subnet_scratch(cidr_input):
    try:
        # แยก IP และ CIDR (เช่น 192.168.1.10/24)
        ip_part, cidr_part = cidr_input.split('/')
        cidr = int(cidr_part)
        
        # 1. แปลง IP เป็นตัวเลข (Integer)
        ip_num = ip_to_int(ip_part)
        
        # 2. สร้าง Subnet Mask (Binary)
        # นำ 1 มาเรียงกันตามจำนวน CIDR แล้ว shift ไปทางซ้าย
        # 0xFFFFFFFF คือเลข 32-bit ที่มีค่าเป็น 1 ทั้งหมด
        mask_num = (0xFFFFFFFF << (32 - cidr)) & 0xFFFFFFFF
        
        # 3. คำนวณ Network Address (IP AND Mask)
        network_num = ip_num & mask_num
        
        # 4. คำนวณ Wildcard (Inverse Mask)
        # ใช้ XOR กับ 32-bit เพื่อกลับค่าบิต (0->1, 1->0)
        wildcard_num = mask_num ^ 0xFFFFFFFF
        
        # 5. คำนวณ Broadcast Address (Network OR Wildcard)
        broadcast_num = network_num | wildcard_num
        
        # 6. คำนวณจำนวน Host
        # สูตร: 2^(32 - cidr) - 2
        total_ips = 2 ** (32 - cidr)
        usable_hosts = total_ips - 2 if total_ips > 2 else 0

        # แสดงผล
        print(f"--- Result for {cidr_input} ---")
        print(f"IP Address:        {ip_part}")
        print(f"Network Address:   {int_to_ip(network_num)}")
        print(f"Broadcast Address: {int_to_ip(broadcast_num)}")
        print(f"Subnet Mask:       {int_to_ip(mask_num)}")
        print(f"Wildcard Mask:     {int_to_ip(wildcard_num)}")
        print(f"Usable Hosts:      {usable_hosts}")
        
        if usable_hosts > 0:
            print(f"Host Range:        {int_to_ip(network_num + 1)} - {int_to_ip(broadcast_num - 1)}")
        print("-" * 30)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    calculate_subnet_scratch("172.16.0.128/27")
    calculate_subnet_scratch("172.16.0.192/26")
    calculate_subnet_scratch("172.16.0.0/24")