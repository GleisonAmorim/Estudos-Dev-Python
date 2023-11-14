import json
import pandas as pd
import matplotlib.pyplot as plt

# Inicialize um dicionário vazio para armazenar as carteiras
carteiras = {}
carteira_atual = None
pagamento_cadastrado = False  # Variável para controlar se um pagamento foi cadastrado

# Função para criar ou selecionar uma carteira
def selecionar_carteira():
    global carteira_atual
    nome_carteira = input("Bem vind@, para começar digite o nome da sua carteira (Pode ser o seu nome): ")
    if nome_carteira in carteiras:
        print(f"Carteira '{nome_carteira}' selecionada.")
    else:
        carteiras[nome_carteira] = {"contas": {}}
        print(f"Você criou a carteira {nome_carteira}")
    carteira_atual = nome_carteira

# Função para calcular e exibir o saldo atual da carteira
def mostrar_saldo():
    saldo = 0
    if carteira_atual is not None:
        for conta, movimentos in carteiras[carteira_atual]["contas"].items():
            for movimento in movimentos:
                saldo += movimento["valor"]
        print(f"Saldo atual da carteira '{carteira_atual}': R${saldo:.2f}")

# Função para ver o histórico
def ver_historico():
    if carteira_atual is not None:
        historico = carteiras[carteira_atual]["contas"]
        for conta, movimentos in historico.items():
            print(f"Histórico da conta '{conta}':")
            for movimento in movimentos:
                print(f"Data: {movimento['data']}, Valor: R${movimento['valor']:.2f}")
    else:
        print("Selecione ou crie uma carteira antes de ver o histórico.")

# Função para realizar análise de dados por data
def analisar_por_data():
    if carteira_atual is not None:
        data = {"Data": [], "Valor": []}
        for conta, movimentos in carteiras[carteira_atual]["contas"].items():
            for movimento in movimentos:
                data["Data"].append(movimento["data"])
                data["Valor"].append(movimento["valor"])
        df = pd.DataFrame(data)

        # Solicita ao usuário o período
        data_inicial = input("Digite a data inicial (DD/MM/AAAA): ")
        data_final = input("Digite a data final (DD/MM/AAAA): ")

        # Filtra os dados com base no período
        df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')
        mask = (df['Data'] >= data_inicial) & (df['Data'] <= data_final)
        df_filtrado = df.loc[mask]

        if not df_filtrado.empty:
            plt.figure(figsize=(10, 6))
            plt.plot(df_filtrado['Data'], df_filtrado['Valor'])
            plt.xlabel('Data')
            plt.ylabel('Valor')
            plt.title('Análise de Dados por Data')
            plt.show()
        else:
            print("Nenhum dado encontrado para o período especificado.")
    else:
        print("Selecione ou crie uma carteira antes de realizar a análise.")

# Função para realizar análise de dados por palavra-chave
def analisar_por_palavra_chave():
    if carteira_atual is not None:
        palavra_chave = input("Digite a palavra-chave para pesquisa: ")
        data = {"Conta": [], "Data": [], "Valor": []}
        for conta, movimentos in carteiras[carteira_atual]["contas"].items():
            for movimento in movimentos:
                if palavra_chave in conta:
                    data["Conta"].append(conta)
                    data["Data"].append(movimento["data"])
                    data["Valor"].append(movimento["valor"])
        df = pd.DataFrame(data)

        # Solicita ao usuário o período
        data_inicial = input("Digite a data inicial (DD/MM/AAAA): ")
        data_final = input("Digite a data final (DD/MM/AAAA): ")

        # Filtra os dados com base no período
        df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')
        mask = (df['Data'] >= data_inicial) & (df['Data'] <= data_final)
        df_filtrado = df.loc[mask]

        if not df_filtrado.empty:
            plt.figure(figsize=(10, 6))
            plt.bar(df_filtrado['Conta'], df_filtrado['Valor'])
            plt.xlabel('Conta')
            plt.ylabel('Valor')
            plt.title('Análise de Dados por Palavra-chave')
            plt.xticks(rotation=45, ha='right')
            plt.show()
        else:
            print("Nenhum dado encontrado para a palavra-chave e período especificados.")
    else:
        print("Selecione ou crie uma carteira antes de realizar a análise.")

# Função para cadastrar pagamento
def cadastrar_pagamento():
    global pagamento_cadastrado
    nome_conta = input("Nome do pagamento (ex: Salário): ")
    valor_input = input("Valor do pagamento: ")
    data_pagamento = input("Data de recebimento (DD/MM/AAAA): ")

    # Substituir vírgulas por pontos (caso existam)
    valor_input = valor_input.replace(',', '.')

    try:
        valor = float(valor_input)
    except ValueError:
        print("Valor do pagamento inválido. Certifique-se de usar ponto (.) como separador decimal.")
        return

    # Armazenar os dados do pagamento na carteira atual
    if carteira_atual is not None:
        pagamento = {"valor": valor, "data": data_pagamento}
        if nome_conta in carteiras[carteira_atual]["contas"]:
            carteiras[carteira_atual]["contas"][nome_conta].append(pagamento)
        else:
            carteiras[carteira_atual]["contas"][nome_conta] = [pagamento]
        print("Pagamento cadastrado com sucesso!")
        pagamento_cadastrado = True  # Marca que um pagamento foi cadastrado
        mostrar_saldo()

# Função para cadastrar débito
def cadastrar_debito():
    if pagamento_cadastrado:
        while True:
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

            # Armazenar os dados do débito na carteira atual
            if carteira_atual is not None:
                debito = {"valor": -valor, "data": data_debito}  # Valor do débito é negativo
                if nome_debito in carteiras[carteira_atual]["contas"]:
                    carteiras[carteira_atual]["contas"][nome_debito].append(debito)
                else:
                    carteiras[carteira_atual]["contas"][nome_debito] = [debito]
                print("Débito cadastrado com sucesso!")
                mostrar_saldo()
            else:
                print("Selecione ou crie uma carteira antes de cadastrar um débito.")

            continuar = input("Deseja cadastrar mais um débito? (S para Sim, qualquer outra tecla para Não): ")
            if continuar.lower() != 's':
                break
    else:
        print("Você precisa cadastrar pelo menos um pagamento antes de adicionar um débito.")

# Função para exibir o menu principal
def exibir_menu():
    print("Escolha uma opção:")
    print("1 - Cadastrar pagamento")
    print("2 - Cadastrar débito")
    print("3 - Ver saldo atual")
    print("4 - Ver histórico")
    print("5 - Análise de dados por data")
    print("6 - Análise de dados por palavra-chave")
    print("7 - Sair")

# Pergunte ao usuário o nome da carteira e selecione ou crie
selecionar_carteira()

# Loop principal
while True:
    exibir_menu()
    opcao = input("Opção: ")

    if opcao == '1':
        cadastrar_pagamento()
    elif opcao == '2':
        cadastrar_debito()
    elif opcao == '3':
        mostrar_saldo()
    elif opcao == '4':
        ver_historico()
    elif opcao == '5':
        analisar_por_data()
    elif opcao == '6':
        analisar_por_palavra_chave()
    elif opcao == '7':
        print("Obrigado por utilizar nossos serviços, até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha de 1 a 7.")