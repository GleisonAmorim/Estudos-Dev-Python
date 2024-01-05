import socket

HOST = "127.0.0.1"
PORT = 9000
print("INICIANDO O SOCKET")
s = socket.socket()
print("CONECTANDO COM O SERVIDOR")
s.connect((HOST, PORT))
texto = 'olá mundo'
print("ENVIANDO O TEXTO")
s.sendall(texto.encode("utf-8"))
dados = s.recv(1024)
s.close()
texto=dados.decode('utf-8')
print(f"Cliente: Recebi {texto}")