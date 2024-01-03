pode_parcelar = True
valor = input('Digie o valor do produto: ')
limite = input('Digie o limite do cartão: ')

if (pode_parcelar or valor < 2000) and limite >= valor:
    print('Compra aprovada')
else:
    print('Compra recusada')