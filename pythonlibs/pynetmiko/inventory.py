
import csv
import os
from dotenv import load_dotenv
import hvac

# Load environment variables from .env
load_dotenv(".env")


def get_device_credentials():
    """Get credentials from the .env file."""
    username = os.getenv("NETMIKO_USERNAME")
    password = os.getenv("NETMIKO_PASSWORD")

    if not username or not password:
        raise RuntimeError(
            "NETMIKO_USERNAME or NETMIKO_PASSWORD is missing in .env"
        )

    return username, password


def get_device_creds_from_vault():
    """Get credentials from HashiCorp Vault."""
    vault_addr = os.getenv("VAULT_ADDR")
    vault_token = os.getenv("VAULT_TOKEN")

    if not vault_addr or not vault_token:
        raise RuntimeError(
            "VAULT_ADDR or VAULT_TOKEN is missing in .env"
        )

    client = hvac.Client(
        url=vault_addr,
        token=vault_token,
        timeout=10
    )

    if not client.is_authenticated():
        raise RuntimeError("Vault authentication failed")

    result = client.secrets.kv.v2.read_secret(
        path="useraccess",
        mount_point="secret"
    )

    secret = result["data"]["data"]
    username = secret["username"]
    password = secret["password"]

    return username, password


def get_devices(csv_file="devices.csv"):
    """Read device IP addresses from the CSV file."""

    # Use Vault credentials
    username, password = get_device_creds_from_vault()

    devices = []

    if not os.path.isfile(csv_file):
        raise FileNotFoundError(
            f"CSV file not found: {os.path.abspath(csv_file)}"
        )

    with open(csv_file, mode="r", newline="") as file:
        reader = csv.DictReader(file)

        required_columns = {"host", "device_type"}
        if not reader.fieldnames or not required_columns.issubset(
            reader.fieldnames
        ):
            raise ValueError(
                "CSV must contain these columns: host, device_type"
            )

        for row in reader:
            device = {
                "device_type": row["device_type"].strip(),
                "host": row["host"].strip(),
                "username": username,
                "password": password,
            }

            devices.append(device)

    return devices
