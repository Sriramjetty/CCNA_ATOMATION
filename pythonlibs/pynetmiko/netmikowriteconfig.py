import csv
import os
from netmiko import ConnectHandler
from dotenv import load_dotenv

# load credentials from .env file
load_dotenv(".env")

username = os.getenv("NETMIKO_USERNAME")
password = os.getenv("NETMIKO_PASSWORD")

with open("device.csv") as file:
    devices = csv.DictReader(file)
    
    for device in devices:
        device["username"] = username
        device["password"] = password
        pod_id = int(device.pop("pod_id"))  # Remove pod_id from device dictionary and convert to int
        loopback_ip = f"10.10.{pod_id}.1"
        print(f"Connecting to device: {device['host']} with loopback IP: {loopback_ip}")    
        with ConnectHandler(**device) as netconnect:
            commands = [
                "interface loopback0",
                f"ip address {loopback_ip} 255.255.255.0"
            ]
            output = netconnect.send_config_set(commands)
            print(output)
            
            # Verfy the configuration change
            output = netconnect.send_command("show ip int brief")
            print(output)
            
            # Save the configuration to startup-config
            output = netconnect.save_config()
            print(output)
            
            