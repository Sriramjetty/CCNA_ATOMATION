from inventory import get_devices
from netmiko import ConnectHandler


for device in get_devices():
    with ConnectHandler(**device) as netconnect:
        print(netconnect.find_prompt())
        print(netconnect.send_command("show ip int br",use_textfsm=False))
        
        print(f"Device: {device['host']}")
