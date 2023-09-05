import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

my_ip = s.getsockname()[0]
#my_ip = socket.gethostbyname("sjf-cpgmsa19")

print("Ip for my machine is:", my_ip)

s.close()
