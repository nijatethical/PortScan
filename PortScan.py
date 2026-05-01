print("""
╔════════════════════════════╗
║   🔧 PORT SCANNER TOOL     ║
╚════════════════════════════╝
""") 

import socket
import time
import json

# Get target IP from user
Ip = input("Enter target IP address (e.g., 192.168.100.1): ")

# List of common ports to scan
Ports = [21,22,23,25,53,67,68,80,110,135,139,145,149,443,445,3389,8080]
OpenPorts = []

print(f"\n🔍 Scanning ports on target {Ip}...\n")

for port in Ports:
    print(f"Port {port}", end=" > ")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    result = sock.connect_ex((Ip, port))
    
    if result == 0:
        print(f"\033[92mOpen!\033[0m")  # Green for open
        OpenPorts.append(port)
    else:
        print(f"\033[91mClosed!\033[0m")  # Red for closed
    
    sock.close()
    time.sleep(1.5)

# Save results in JSON
if OpenPorts:
    output = {
        "IP": Ip,
        "Scanned Ports": Ports,
        "Open Ports": OpenPorts,
        "Date": time.strftime("%Y-%m-%d")
    }
    with open("Open_Ports.json", "w", encoding="utf8") as f:
        json.dump(output, f, indent=4)
    print("\n📁 \033[92mOpen ports saved in 'Open_Ports.json'.\033[0m")
else:
    print("\nNo open ports found, file not created.\n") 

# Print author name at the end
print(" ")
print("by Nijat Zadeh")
