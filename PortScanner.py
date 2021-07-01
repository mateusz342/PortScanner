import socket

target=input("Type the server IP address: ")
portrange=input("Type the port range to scan(np.5-200): ")

lowport=int(portrange.split('-')[0])
highport=int(portrange.split('-')[1])

for port in range(lowport,highport):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status=sock.connect_ex((target,port))
    if(status==0):
        print("open - ", port)
    else:
        print("closed - ", port)
    sock.close()

