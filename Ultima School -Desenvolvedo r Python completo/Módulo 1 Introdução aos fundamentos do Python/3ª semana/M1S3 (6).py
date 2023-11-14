'''Escreva uma função que, dado o valor da conta de um restaurante e um percentual de taxa de serviço, 
calcule e exiba a gorjeta do garçom, considerando o percentual do valor da conta.'''

def soma_gorjeta (valor_conta, valor_tx_servico):
    gorjeta = (valor_conta * valor_tx_servico) /100
    return gorjeta

valor_conta = float(input('Digite o valor da conta: '))
valor_tx_servico = int(input('Digite o valor da taxa de serviço (em porcentagem): '))

gorjeta = soma_gorjeta(valor_conta, valor_tx_servico)
print(f'O valor da gorjeta é de: R$ {gorjeta:.2f}')