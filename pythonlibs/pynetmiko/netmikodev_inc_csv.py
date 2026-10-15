from netmiko import ConnectHandler
import csv
from getpass import getpass
from dotenv import load_dotenv
import os

load_dotenv(".env")  # Load environment variables from .env file



with open("device.csv") as file:
    devices = csv.DictReader(file)
    
    for device in devices:
        device["username"] = os.getenv("NETMIKO_USERNAME")
        device["password"] = os.getenv("NETMIKO_PASSWORD")
        with ConnectHandler(**device) as netconnect:
            print(netconnect.find_prompt())
            print(netconnect.send_command("show ip int br"))
            
            print(f"Device: {device["host"]}")


