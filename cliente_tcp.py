import socket

try:
    porta = 8080
    with socket.create_connection(("192.168.1.23", porta), timeout=5) as s:
        print("Conectado de", s.getsockname(), "para", s.getpeername())
        s.sendall("Ola, servidor".encode())
        print("Resposta:", s.recv(1024).decode())
except ConnectionRefusedError:
    print(f"Conexão recusada: nenhum servidor na porta {porta} (RST)")
except TimeoutError:
    print("Tempo esgotado: sem resposta.")