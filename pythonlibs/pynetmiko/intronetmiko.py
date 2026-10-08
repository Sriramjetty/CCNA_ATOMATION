from netmiko import ConnectHandler 

csr={
    "device_type": "cisco_ios",
    "host":"198.18.128.10",
    "username": "admin",
    "password": "admin"
}    
    
netconnect= ConnectHandler(**csr)
output1=netconnect.find_prompt()
output=netconnect.send_command("show ip int brief")
print(output1)
print(output)    

netconnect.disconnect()