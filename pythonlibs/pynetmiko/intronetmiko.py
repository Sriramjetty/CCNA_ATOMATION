from netmiko import ConnectHandler

csr = {
    "device_type": "cisco_ios",
    "host": "198.18.128.10",
    "username": "admin",
    "password": "admin123",
    #"port": 8022,  # optional, defaults to 22
    #"secret": "secret",  # optional, defaults to ''
}


netconnect = ConnectHandler(**csr)
output = netconnect.send_command("show ip int brief")
print(output)

netconnect.disconnect()

# The above could be written  as below..as context manager give advantage to not follow with the disconnect part of the syntax.(analogy with Filehandling with context manager)
# with ConnectHandler(**csr) as netconnect:
#     print(netconnect.find_prompt())
#     print(netconnect.send_command("show ip int br"))

#send_command() is used to send a single command to the device and return the output as a string.
#send_command_timing() is used to send a command to the device and return the output as a string, but it will wait for the command prompt to return before returning the output. This can be useful for commands that take a long time to execute or for commands that do not return a prompt.
#send_config() is used to send a list of configuration commands to the device and return the output as a string. This can be useful for making changes to the device configuration.
#send_config_set() is used to send a set of configuration commands to the device and return the output as a string. This can be useful for making changes to the device configuration.
#send_config_from_file() is used to send a set of configuration commands from a file to the device and return the output as a string. This can be useful for making changes to the device configuration from a file.
#save_config() is used to save the current configuration of the device to the startup configuration. This can be useful for ensuring that changes made to the device configuration are saved and will persist after a reboot.
#conn_timout is used to set the timeout for the connection to the device. This can be useful for ensuring that the connection does not hang indefinitely if the device is not responding.
#banner_timeout is used to set the timeout for the banner message that is displayed when connecting to the device. This can be useful for ensuring that the connection does not hang indefinitely if the banner message is not displayed.
#read_Timeout is used to set the timeout for reading data from the device. This can be useful for ensuring that the connection does not hang indefinitely if the device is not responding.

