from netmiko import ConnectHandler

print("=== Router Login ===")
ip = input("Router IP daalo: ")
username = input("Username: ")
password = input("Password: ")

router = {
    'device_type': 'cisco_ios',
    'host': ip,
    'username': username,
    'password': password,
}

try:
    net_connect = ConnectHandler(**router)
    print("Connected! ✅")
    with open("commands.txt", "r") as f:
        commands = [line.strip() for line in f if line.strip()]
    for cmd in commands:
        print(f"\n--- {cmd} ---")
        print(net_connect.send_command(cmd))
    net_connect.disconnect()
    print("\n=== Khatam ===")
except Exception as e:
    print(f"Error: {e}")