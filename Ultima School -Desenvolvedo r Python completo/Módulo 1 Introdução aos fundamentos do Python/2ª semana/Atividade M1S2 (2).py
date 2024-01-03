'''Uma nave espacial recebe as pessoas com uma mensagem de boas vindas de acordo com o nome que elas forneceram ao fazer o cadastro na recepção.
Crie uma aplicação que imprima a mensagem de boas vindas de acordo com os nomes na lista: nomes = [“Elysson“, “Giulia“, “Willian“, “Gileno“], 
com a seguinte mensagem: “Olá, NOME_PESSOA! Seja bem vindo à nave Imperial dos Siths.”. 
Crie um programa que faça a interpolação da string de boas vindas, substituindo o NOME_PESSOA pelo nome lido na lista e imprimindo a frase de boas vindas com o nome substituído.'''

nomes = ['Elysson', 'Giulia', 'Willian', 'Gileno']
nome_pessoa = input('Digite seu nome: ')

if nome_pessoa in nomes:
    mensagem_boas_vindas = f'Olá {nome_pessoa}! Seja bem vindo à nave Imperial dos Siths'
    print(mensagem_boas_vindas)