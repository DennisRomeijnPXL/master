def main():
	with open('file') as IP_LIST:
		for IP in IP_LIST:
			RTR = {
				'device_type': 'cisco_ios',
				'ip': IP,
				'username': 'cisco',
				'password': 'cisco'
				}
		
			print ('Connecting to the device ' + IP)
			net_connect = ConnectHandler(**RTR)

			with open('file') as CONFIG_LINES:
				CONFIG = CONFIG_LINES.read()
			output = net_connect.send_config_set(CONFIG)

			output = net_connect.send_command('show ip int brief')
			print(output)

if __name__ == "__main__":
	main()
