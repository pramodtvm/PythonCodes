import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server = 'IPHERE'

def PortScanner(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False

for x in range(8003,8006):
    if PortScanner(x):
        print("Port is open",x)
    else:
        print("port is Closed",x)