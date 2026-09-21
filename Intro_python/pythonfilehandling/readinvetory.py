import csv


def read_inventory(filename):
    devices = []

    with open(filename, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            devices.append(row)

    return devices


devices = read_inventory("invetory.csv")

for dev in devices:
    print(dev)