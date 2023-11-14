def verifica_prefixo(palavra1, palavra2):#definindo nome e argumentos da função
    if palavra1 in palavra2: #se a palavra 1 estíver dentro da palavra 2 é verdadero
        return True
    else:
        return False #caso contrário é faso( tirar dúvida na aula )

#coletando as palavras e armazenando nas variáveis
palavra1 = input("Digite a primeira palavra: ") 
palavra2 = input("Digite a segunda palavra: ")
#exibindo o resultado
resultado = verifica_prefixo(palavra1, palavra2)
print(resultado)