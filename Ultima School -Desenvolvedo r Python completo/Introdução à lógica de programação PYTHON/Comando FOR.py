"""print("iniciando a contagem")
for x in range(1, 11, 1):
    print(x)
print("fim do progrma")   """

pagamento_total = 0
for valor in range(5):
    salario_atual = float (input("Digite o salario: "))
    pagamento_total += salario_atual
print("A folha de pagamento é: ", pagamento_total)