import socket
import requests

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_ip = s.getsockname()[0]
s.close()

public_ip = requests.get("https://api64.ipify.org").text

# Tulosta molemmat
print(f"Local IP: {local_ip}")
print(f"Public IP: {public_ip}")