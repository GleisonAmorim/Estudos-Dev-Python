''' '''

def somar_numeros():
    total = 0
    while True:
        numero = int(input('Digite um número (ou -1 para sair): '))
        if numero == -1:
            break
        total += numero
    return total

soma = somar_numeros()
print('A soma dos números inseridos é:', soma)