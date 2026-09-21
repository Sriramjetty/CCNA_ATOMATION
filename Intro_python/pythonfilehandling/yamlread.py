import yaml

with open("deviceyaml.yaml","r") as file:
    inventory = yaml.safe_load(file)
    

for dev in inventory["device"]:
    print(f"Hostname: {dev['hostname']}")
    print(f"ip_address: {dev['management']['ip_address']}")  ## fix this as homework.