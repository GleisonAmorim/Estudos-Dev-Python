# Classe 
'''Classes - São as formas como esses objetos serão representados, e cada objeto representa uma “instância” de uma classe, isto é, uma representação real de uma classe. E são nas classes que definimos quais são os atributos (características) e as ações que aquela classe tem.
- Trazendo esses exemplos para o mundo real, vamos imaginar a classe Cachorro. Os cachorros possuem características como nome, raça, comprimento, peso, entre outras. Mas os cachorros também realizam ações como latir, morder, dormir, brincar, comer, entre outras.      '''
# Objeto 
'''Objetos - são representações de entidades físicas ou lógicas do mundo real, e entidades que possamos identificar e representar através de características e/ou ações.
- Exemplos de objetos são: cachorro; cadeira; computador; geladeira; matérias da faculdade; um e-mail. Já exemplo de coisas que não são objetos: o tempo; o amor; a velocidade etc.'''

class Cachorro:
    def __init__ (self, nome: str, raca: str, comprimento: float, peso: float):
        self.nome = nome
        self.raca = raca
        self.comprimento = comprimento
        self.peso = peso
        
    def latir(self):
        print(f'Au au! Eu sou o (a) {self.nome}')
    
    def morder(self):
        print(f'O(a) cachorro (a) {self.nome} me mordeu!')
        
    def dormir(self):
        print('ZZZZzzzzzz...')
        
    def brincar(self):
        print('Eu gosto de brincar de bolinha!')
        
    def brincar(self):
        print (f'Eu peso {self.peso} kg e preciso comer {self.peso * 1000 * 0.01} de comida para ficar satisfeito(a)!')
        
becca = Cachorro("Becca", 'West', 65 , 7)

becca

becca.nome
