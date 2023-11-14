"""Pensando em um jogo onde existe um assassino um sobrevivente e um item

- Assassino = Altura, velocidade, duas hailidades especiais (sempre mais fortes que o sobrevivente)
- Sobrevivente = Altura, velocidade, duas habilidades especials
- Item = nome, tamanho, efeito. Vai ser utilizado pelo sobrevivente contra o assassino

No jogo o sobrevivente tem que encontrar a saída que fica escondida pelo mapa sem que o assassino o encontre"""
class Killer:
    def __init__(self, nome, altura, velocidade, habilidade1, habilidade2):
        self.nome = nome
        self.altura = altura
        self.velocidade = velocidade
        self.habilidade1 = habilidade1
        self.habilidade2 = habilidade2       
killer1 = Killer("Espirito", "174", "4.5", "congelar", "ir para o mundo sombrio")
print(killer1.nome)
print(killer1.altura)
print(killer1.velocidade)
print(killer1.habilidade1)
print(killer1.habilidade2)

class Survivor:
    def __init__(self, nome, altura, velocidade, habilidade1, habilidade2):
        self.nome = nome
        self.altura = altura
        self.velocidade = velocidade
        self.habilidade1 = habilidade1
        self.habilidade2 = habilidade2       
survivor1 = Survivor("Anna", "1.65", "4.3", "agilizar", "autocurar")
print(survivor1.nome)
print(survivor1.altura)
print(survivor1.velocidade)
print(survivor1.altura)
print(survivor1.habilidade1)
print(survivor1.habilidade2)

class Item:
    def __init__(self, nome_item, tamanho, efeito_especial):
        self.nome_item = nome_item
        self.tamanho = tamanho
        self.efeito_especial = efeito_especial     
item1 = Item("Lanterna mágica", "13x5", "Cegar Killer")
print(item1.nome_item)
print(item1.tamanho)
print(item1.efeito_especial)