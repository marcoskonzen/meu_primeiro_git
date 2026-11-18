#Servidor UDP

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 9000))

print("Servidor UDP aguardando na porta 9000...")
while True:
    dados, origem = s.recvfrom(2048)
    print("Recebido de", origem, ":", dados.decode())
    s.sendto(b"eco: " + dados, origem)