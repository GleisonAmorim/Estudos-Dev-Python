#apenas com lista e dicionário
clientes = []  # lista vazia para armazenar os clientes

for i in range(5):
    cliente = {}  # dicionário vazio para armazenar os dados do cliente

    nome = input("Digite o nome do cliente: ")  # informações do cliente
    cpf = input("Digite o CPF do cliente: ")  # informações do cliente
    idade = int(input("Digite a idade do cliente: "))  # informações do cliente

    cliente["Nome"] = nome  # preenchendo o dicionário do cliente com as informações coletadas
    cliente["CPF"] = cpf  # preenchendo o dicionário do cliente com as informações coletadas
    cliente["Idade"] = idade  # preenchendo o dicionário do cliente com as informações coletadas

    clientes.append(cliente)  # adicionando o dicionário do cliente à lista de clientes

# imprimindo as informações formatadas
for cliente in clientes:
    print("Cliente:", cliente["Nome"], "CPF:", cliente["CPF"], "Idade:", cliente["Idade"])
    
    
#Classes

class Cliente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

# lista vazia para armazenar os clientes
clientes = []

# loop para coletar informações de 5 clientes
for i in range(5):
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    idade = int(input("Digite a idade do cliente: "))
    
    #  Objeto Cliente com as informações coletadas
    cliente = Cliente(nome, cpf, idade)
    
    # Adicionando o objeto cliente à lista de clientes
    clientes.append(cliente)

# Imprimindo as informações formatadas
for cliente in clientes:
    print("Cliente:", cliente.nome, "CPF:", cliente.cpf, "Idade:", cliente.idade)