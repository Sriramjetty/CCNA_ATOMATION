import xml.etree.ElementTree as ET

tree = ET.parse("device.xml")

root = tree.getroot()

print(root.tag)



interfaces = root.findall("interfaces/interface")

for intf in interfaces:
    name = intf.find("name").text
    ip = intf.find("ipAddress").text
    subnet = intf.find("subnetMask").text
    
    print("Inteface:" , name)
    print("IP:" , ip)
    print("subnetmask:", subnet)