# Cliente UDP

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.settimeout(2.0)
s.sendto("ola, UDP".encode(), ("127.0.0.1", 9000))
try:
    resposta, _ = s.recvfrom(2048)
    print(resposta.decode())
except socket.timeout:
    print("Sem resposta: datagrama ou resposta perdidos")