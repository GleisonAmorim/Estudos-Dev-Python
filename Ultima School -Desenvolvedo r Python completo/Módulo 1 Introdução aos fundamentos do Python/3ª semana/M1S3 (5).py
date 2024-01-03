'''5. Faça um programa com uma função que necessite de um parâmetro. A função deve retornar “Positivo”, 
se seu o número for maior que zero, “Negativo” se o número for menor que zero, e “Zero” se o número for igual a zero.'''

def verificar_numeros(numero):
    if numero   < 0:
        return ('Negativo')
    elif numero == 0:
        return('Zero')
    else:
        return('Positivo')
    
numero = int(input("Digite um número inteiro: "))
resultado = verificar_numeros(numero)
print(resultado)

