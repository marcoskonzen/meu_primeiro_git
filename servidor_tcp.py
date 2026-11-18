import socket

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET: Ipv4, SOCK_STREAM: TCP
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind(("127.0.0.1", 8080))
srv.listen(5)
print("Servidor TCP escutando da porta 8080...")

while True:
    conn, cliente = srv.accept()
    print("Conexao de ", cliente)
    with conn:
        while True:
            dados = conn.recv(1024)
            if not dados:
                print("Cliente encerrou:", cliente)
                break
            print("Recebido:", dados.decode())
            conn.sendall(dados.upper())