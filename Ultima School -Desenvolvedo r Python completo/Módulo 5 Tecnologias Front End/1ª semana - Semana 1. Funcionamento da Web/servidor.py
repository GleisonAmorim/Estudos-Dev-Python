import socket

HOST = "127.0.0.1"
PORT = 9000
print("INICIANDO O SOCKET")
s = socket.socket()
s.bind((HOST, PORT))
print("ESCUTANDO")
s.listen()
conexao, endereco = s.accept()
with conexao:
    print(f'Nova conexão {endereco}')
    while True:
        dados = conexao.recv(1024)
        if not dados:
            break
        texto = dados.decode('utf-8')
        print(f'Servidor: Recebi {texto}')
        conexao.sandall(texto.encode('uf-8'))
s.close()
