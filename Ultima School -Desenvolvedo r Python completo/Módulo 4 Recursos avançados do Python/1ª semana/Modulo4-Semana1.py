import requests

class FipeIterator:
    def __init__(self, marca_id):
        self.marca_id = marca_id
        self.modelos = None
        self.current_index = 0

    def fetch_modelos(self):
        # URL da API para obter os modelos da marca específica
        url = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{self.marca_id}/modelos'
        # Headers necessários para a API da FIPE
        headers = {'user-agent': 'MyStudyApp'}

        # Faz uma requisição GET para obter os modelos da marca
        response = requests.get(url, headers=headers)

        # Verifica se a requisição foi bem-sucedida (código de status 200)
        if response.status_code == 200:
            # Converte a resposta para formato JSON
            data = response.json()
            # Obtém a lista de modelos da marca
            self.modelos = data['modelos']
        else:
            # Lança uma exceção em caso de erro na requisição
            raise Exception(f"Erro ao obter modelos da marca {self.marca_id}")

    def __iter__(self):
        # Ao iniciar a iteração, obtém os modelos da marca
        self.fetch_modelos()
        return self

    def __next__(self):
        # Verifica se já iterou por todos os modelos
        if self.modelos is None or self.current_index >= len(self.modelos):
            # Lança StopIteration para indicar o fim da iteração
            raise StopIteration

        # Obtém o modelo atual
        modelo = self.modelos[self.current_index]
        self.current_index += 1

        # Retorna o nome e o código do veículo atual
        return modelo['nome'], modelo['codigo']

# Exemplo de uso
marca_id_selecionada = 1  # Substitua pelo ID da marca desejada
iterator = FipeIterator(marca_id_selecionada)

# Itera sobre os modelos e imprime nome e ID de cada veículo
for nome, codigo in iterator:
    print(f"Nome do Veículo: {nome}, ID: {codigo}")
