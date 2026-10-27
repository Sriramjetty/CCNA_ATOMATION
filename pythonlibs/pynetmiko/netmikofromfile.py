from inventory import get_devices
from netmiko import ConnectHandler


for device in get_devices():
    with ConnectHandler(**device) as netconnect:
        print(netconnect.find_prompt())
        print(netconnect.send_config_from_file("config.txt"))
        
        print(f"Device: {device['host']}")
