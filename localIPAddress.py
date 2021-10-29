import socket
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print("Your IP Address is:")
print(ip)
