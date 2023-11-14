'''Crie uma função que recebe um número inteiro por parâmetro e então imprime na tela do número recebido até o zero.'''

def contar_ate_zero(numero):
    while numero >= 0:
        print(numero),
        numero -= 1

numero = int(input("Digite um número inteiro: "))

contar_ate_zero(numero)