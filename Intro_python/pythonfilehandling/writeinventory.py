import csv


def write_inventory(filename, devices):

    with open(filename, "w", newline="") as file:

        fieldname = [
            "hostname",
            "ip_add",
            "platform",
            "version",
            "status"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldname)

        writer.writeheader()

        for row in devices:
            writer.writerow(row)


devices = [

    {
        "hostname": "R1",
        "ip_add": "125.255.255.1",
        "platform": "cisco",
        "version": "15.1",
        "status": "active"
    },

    {
        "hostname": "R2",
        "ip_add": "125.255.255.2",
        "platform": "cisco",
        "version": "15.1",
        "status": "active"
    }

]


write_inventory("dictinventory.csv", devices)

print("Inventory file created successfully!")