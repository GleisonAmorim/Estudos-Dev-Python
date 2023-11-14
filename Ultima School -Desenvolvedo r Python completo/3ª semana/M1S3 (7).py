'''Crie uma função que permita contar o número de vezes que aparece uma determinada letra em uma frase. 
A letra desejada e a frase a ser verificada serão passadas por parâmetro para a função, 
que retornará a quantidade da letra na frase.'''


def contar_letra_na_frase(frase, letra):   
    contador = 0
    for letraa in frase:
        if letraa == letra:
            contador += 1
    return contador

frase = input('Digite a frase: ')
letra = input('Digite qual letra você deseja contar: ')

quantidade = contar_letra_na_frase(frase, letra)

print(f'O total de letras {letra} é {quantidade}')

