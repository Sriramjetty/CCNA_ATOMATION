import json

inventory = {
  "device_name": "Router01",
  "vendor": "Cisco",
  "model": "ISR4331",
  "management_ip": "192.168.1.1",
  "status": "active",
}

with open ("invetoryfile.json","w") as file:
    json.dump(inventory,file,indent=4)
    
print("Inventory file has been written successfully")