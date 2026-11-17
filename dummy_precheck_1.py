# Dummy Router - Bina Router Ke Practice Ke Liye
import time

print("=== Router Login ===")
ip = input("1.1.1.1: ")
username = input("test: ")
password = input("test123: ")

print(f"\n{ip} se connect ho raha hu...")
time.sleep(1)
print("Connected! ✅ (Dummy Router)")

# Dummy output - Jaise asli router deta hai
dummy_outputs = {
    "show bgp vrf all": "BGP VRF: default - Neighbor 213.51.0.1 UP, 150 routes received",
    "show isis segment-routing": "ISIS SR: Enabled, SID 16001, 12 neighbors UP",
    "show bgp ipv4 labeled-unicast": "BGP LU: 250 prefixes, Label 24001-24250 allocated",
    "show bgp vpnv4 unicast summary": "VPNv4: 8 VRFs, 45 neighbors, All UP",
    "show mpls forwarding": "MPLS: 180 labels forwarding, No drops",
    "show route vrf all": "VRF Routes: default 150, CUSTOMER-A 80, CUSTOMER-B 65",
    "show interface": "Interface Gi0/0/0/0 UP, Gi0/0/0/1 UP, 0 errors",
}

# commands.txt se padhega
try:
    with open("commands.txt", "r") as f:
        commands = [line.strip() for line in f if line.strip()]
except:
    commands = list(dummy_outputs.keys())
    print("commands.txt nahi mili, default commands chala raha hu")

print("\n=== Pre-Check Shuru ===")
result_file = open("precheck_result.txt", "w")

for cmd in commands:
    print(f"\n--- {cmd} ---")
    output = dummy_outputs.get(cmd, f"{cmd} - OK, No Issue Found ✅")
    print(output)
    result_file.write(f"\n--- {cmd} ---\n{output}\n")
    time.sleep(0.5)

result_file.close()
print("\n=== Pre-Check Khatam ✅ ===")
print("Result save ho gaya: precheck_result.txt me")
