def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"

numero = int(input("Digite um número inteiro: "))

resultado = verificar_par_ou_impar(numero)
print(resultado)