import json

with open("devicejson.json", "r") as file:
    inventory = json.load(file)

print(json.dumps(inventory, indent=4))

for interface in inventory["interfaces"]:
    print(interface["name"])