from requests_html import HTMLSession

url = 'https://www.heroku.com/home'
sessao = HTMLSession()
resposta = sessao.get(url)
links = resposta.html.find("a.stretched-link")

for link in links:
    print(link.attrs['href'])