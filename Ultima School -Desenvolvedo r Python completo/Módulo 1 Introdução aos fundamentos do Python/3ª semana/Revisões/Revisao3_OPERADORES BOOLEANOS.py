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

combinacoes = [ 
    (True, True),
    (True, False ),   
    (False, True ),   
    (False , False ),
]

for x, y in combinacoes:
    print(f'{x} OR {y} -> {x or y}')
               