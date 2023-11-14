'''
idade = int(input ('Digite sua idade: '))

if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')
'''

'''FOR'''

'''
nomes = ['Bruno', 'Ana', 'ANAMA', 'ZeCa','paula','andré']
idades = ['14', '15', '16', '17','18','26']
lista_de_tuplas = zip(nomes, idades)
for nome, idade in lista_de_tuplas:
    print(f'{nome} tem {idade} anos'.capitalize())
    
    '''
    '''
    
nomes = ['Bruno', 'Ana', 'ANAMA', 'ZeCa','paula','andré']
idades = [14, 15, 16, 17,18,26]

for indice, idade in enumerate(idades):
    if idade >= 18:
        print(f'Indice: {indice} é maior de idade.')
        '''