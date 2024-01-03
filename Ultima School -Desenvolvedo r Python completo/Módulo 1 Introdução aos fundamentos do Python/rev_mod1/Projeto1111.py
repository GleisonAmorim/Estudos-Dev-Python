import json

# Inicialize um dicionário vazio para armazenar as carteiras
carteiras = {}
carteira_atual = None

# Função para criar ou selecionar uma carteira
def selecionar_carteira():
    global carteira_atual
    nome_carteira = input("Bem vindo, para começar digite o nome da sua carteira (Pode ser o seu nome): ")
    if nome_carteira in carteiras:
        print(f"Carteira '{nome_carteira}' selecionada.")
    else:
        carteiras[nome_carteira] = {"contas": {"Salário": []}}
        print(f"Você criou a carteira {nome_carteira}")
    carteira_atual = nome_carteira

# Função para cadastrar o salário
def cadastrar_salario():
    if carteira_atual is not None:
        salario = float(input("Informe o valor do seu salário: "))
        carteiras[carteira_atual]["contas"]["Salário"].append({"valor": salario})
        print(f"Salário de R${salario:.2f} cadastrado com sucesso!")

# Função para calcular e exibir o saldo atual da carteira
def mostrar_saldo():
    saldo = 0
    if carteira_atual is not None:
        for movimento in carteiras[carteira_atual]["contas"]["Salário"]:
            saldo += movimento["valor"]
        for conta, movimentos in carteiras[carteira_atual]["contas"].items():
            if conta != "Salário":
                for movimento in movimentos:
                    saldo += movimento["valor"]
    print(f"Saldo atual da carteira '{carteira_atual}': R${saldo:.2f}")

# Função para cadastrar débito
def cadastrar_debito():
    while True:
        if carteira_atual is not None:
            nome_debito = input("Nome do débito: ")
            valor_input = input("Valor do débito: ")
            data_debito = input("Data do débito (DD/MM/AAAA): ")

            # Substituir vírgulas por pontos (caso existam)
            valor_input = valor_input.replace(',', '.')

            try:
                valor = float(valor_input)
            except ValueError:
                print("Valor do débito inválido. Certifique-se de usar ponto (.) como separador decimal.")
                continue

            if nome_debito in carteiras[carteira_atual]["contas"]:
                carteiras[carteira_atual]["contas"][nome_debito].append({"valor": -valor, "data": data_debito})
            else:
                carteiras[carteira_atual]["contas"][nome_debito] = [{"valor": -valor, "data": data_debito}]
            print("Débito cadastrado com sucesso!")
            mostrar_saldo()
        else:
            print("Selecione ou crie uma carteira antes de cadastrar um débito.")

        continuar = input("Deseja cadastrar mais um débito? (S para Sim, qualquer outra tecla para Não): ")
        if continuar.lower() != 's':
            break

# Função para exibir o menu principal
def exibir_menu():
    print("Escolha uma opção:")
    print("1 - Cadastrar salário")
    print("2 - Cadastrar débito")
    print("3 - Ver saldo atual")
    print("4 - Sair")

# Função para salvar o histórico em um arquivo
def salvar_historico():
    if carteira_atual is not None:
        with open(f"{carteira_atual}_historico.json", "w") as arquivo:
            json.dump(carteiras, arquivo)

# Função para carregar o histórico de um arquivo
def carregar_historico(nome_carteira):
    try:
        with open(f"{nome_carteira}_historico.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}

# Pergunte ao usuário o nome da carteira e selecione ou crie
selecionar_carteira()

# Antes de entrar no loop principal, carregue o histórico se ele existir
carteiras = carregar_historico(carteira_atual)

# Loop principal
while True:
    exibir_menu()
    opcao = input("Opção: ")

    if opcao == '1':
        cadastrar_salario()
    elif opcao == '2':
        cadastrar_debito()
    elif opcao == '3':
        mostrar_saldo()
    elif opcao == '4':
        # No final do loop, salve o histórico antes de sair
        salvar_historico()
        print("Obrigado por utilizar nossos serviços, até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha de 1 a 4.")