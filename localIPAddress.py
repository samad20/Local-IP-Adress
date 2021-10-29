import socket
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print("Your Local IP Address is:")
print(ip)
