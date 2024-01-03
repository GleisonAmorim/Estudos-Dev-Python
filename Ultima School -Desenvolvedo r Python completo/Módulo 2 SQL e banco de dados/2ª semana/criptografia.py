import hashlib

senha = '123'

senha.encode('utf-8')

hashlib.sha256(senha.encode('utf-8')).hexdigest()

senha_codificada = hashlib.sha256(senha.encode('utf-8')).hexdigest()
print(senha_codificada)
senha = input('Digite sua senha: ')

if senha_codificada == hashlib.sha256(senha.encode('utf-8')).hexdigest():
    print("senha correta")
else:
    print("senha incorreta")



