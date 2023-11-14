'''Um freelancer está com dificuldade para calcular qual valor cobrar por um projeto que está estimado em 80 horas. 
Após pensar e revisitar o preço de alguns projetos que cobrou no passado, ele montou a seguinte fórmula: valor inicial + quantidade de horas estimadas * valor da hora + 15% do valor calculado. 
Crie um programa que faça essa conta para o freelancer. Considere que o valor inicial sempre será R$ 1000,00 e o valor da hora cobrada é de R$ 20,45. 
A aplicação deve imprimir o valor calculado pelo projeto considerando duas casas decimais na formatação do valor. Dica: Preste atenção na ordem que as operações da fórmula devem ser realizadas.'''

valor_inicial = 1000
valor_hora = 20.45
horas = float(input('Digite o total de horas: '))
valor_calculado = valor_hora * horas + valor_inicial
valor_total_com_quinze = valor_calculado * 1.15
print(f'O Valor total + 15% é de : {valor_total_com_quinze:.2f}')
