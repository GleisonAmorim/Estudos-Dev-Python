combinacoes = [ 
    (True, True),
    (True, False ),   
    ( False, True ),   
    (False , False ),
]

for x , y in combinacoes:
    print(f'{x} AND {y} -> {x == y}')