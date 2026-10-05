import ipaddress

def validate(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except Exception:
        return False

ip = input("Enter the IP address: ")

if validate(ip):
    print("Valid IP address")
else:
    print("Invalid IP address")