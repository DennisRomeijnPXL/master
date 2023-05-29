from netmiko import ConnectHandler

cisco_881 = {
    'device_type': 'cisco_ios',
    'host':   '172.16.6.5',
    'username': 'cisco',
    'password': 'cisco',
    'port' : 22,          # optional, defaults to 22
    'secret': 'cisco',     # optional, defaults to ''
}

config_commands = [ 'logging buffered 20000',
                    'logging buffered 20010',
                    'no logging console' ]
output = net_connect.send_config_set(config_commands)
print(output)
