from requests_html import HTMLSession # aqui fazemos a importação da biblioteca
url = 'https://www.google.com.br/' # aqui definimos a variável url que recebe o link que desejamos acessar
sessao = HTMLSession() # Aqui iniciamos uma sessão, como se fosse abrindo o navegador
resposta = sessao.get(url) # usamos a função get da sessao, aberta anteriormente, para fazer uma requisição HTTP do tipo GET
print(resposta.text) # em seguida fazemos o print do conteúdo retornado, que no caso é o HTML
print(resposta.status_code) # por fim fazemos o print do código de retorno HTTP, que no caso foi 200
