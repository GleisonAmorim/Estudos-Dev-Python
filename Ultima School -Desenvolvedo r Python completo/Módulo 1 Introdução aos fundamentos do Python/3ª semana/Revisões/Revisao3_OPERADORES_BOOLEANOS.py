''' 
numero = 65

if numero > 60 and numero % 2 == 1:
    print('numero maior do que 60 e impar')
    
    (ok)

'''

'''
combinacoes = [ 
    (True, True),
    (True, False ),   
    (False, True ),   
    (False , False ),
]

for x , y in combinacoes:
    print(f'{x} AND {y} -> {x == y}')
    
    '''
    
'''Saída =  (Combinações)
True AND True -> True
True AND False -> False
False AND True -> False
False AND False -> True
(No CMD deu certo)'''



'''
O operador OR somente precisa que uma das expressões seja verdadeira para que ele retorne verdadeiro, ou seja, 
se tivermos um dos elementos de uma expressão Booleana verdadeira, essa expressão será verdadeira. 
O exemplo abaixo demonstra o uso do OR em suas combinações:
'''

'''
combinacoes = [ 
    (True, True),
    (True, False ),   
    (False, True ),   
    (False , False ),
]

for x, y in combinacoes:
    print(f'{x} OR {y} -> {x or y}')

'''
    
''' 
saída =      
True OR True -> True
True OR False -> True
False OR True -> True
False OR False -> False
'''

