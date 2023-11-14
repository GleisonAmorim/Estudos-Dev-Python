"""Arrays e indexação"""
"""
#indices   0        1        2
nomes = ["José", "Maria", "João"]
print(nomes[0])
print(nomes[1])
print(nomes[2])
"""
#indices   0        1        2       3          4        5        6      7 
nomes = ["José", "Maria", "João", "Sherlon","Isadora","José", "Maria", "João", "Sherlon","Isadora","José", "Maria", "João", "Sherlon","Isadora","José", "Maria", "João", "Sherlon","Isadora"]
tamanho = len(nomes)
for i in range(tamanho):
    print(i, nomes[i])
