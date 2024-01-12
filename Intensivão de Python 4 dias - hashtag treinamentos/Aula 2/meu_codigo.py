'''CASE - CANCELAMENTOS

VocÊ foi contratado por uma empresa com mais de 800 mil clientes para um projeto de Dados.
Recentemente a empresa percebeu que da sua base total de clientes, a maioria são clientes inativos,
ou seja, que já cancelaram o serviço.

Precisando melhorar seus resultados ela quer conseguir entender os principais motivos desses cancelamentos
e quais as ações mais eficientes para resuzir esse número'''

# Passo a Passo
# Passo 1: Importar a base de dados
import pandas as pd

tabela = pd.read_csv("cancelamentos.csv")

# Passo 2: Vizualizar a base de dados
tabela = tabela.drop(columns="CustomerID")

# Passo 3: Corrigir a base de dados

tabela = tabela.dropna() #valores vazios - excluir as linhas que têm valores vazios

# Passo 4: Análise inicial dos cancelamentos

# Quantas pessoas cancelaram e quantas não cancelaram
print(tabela["cancelou"].value_counts())

# Em percentual
print(tabela["cancelou"].value_counts(normalize=True))
# para mostrar em porcentagem Vira texto e não tem mis como somar, melhor deixar para o final 
# display(tabela["cancelou"].value_counts(normalize=True).map("{:.2%}".format))

# Passo 5: Análise das causas dos cancelamentos
# gráficos / dashboards
import plotly.express as px

# criar  gráficos
#for coluna in tabela.columns:
    #grafico = px.histogram(tabela, x=coluna, color="cancelou")
    # exibe um gráfico
    #grafico.show()
    
#Análise
# clientes do contrato mensal TODOS cancelam
    # oferecer desconto os anos anuais e trimestrais
    
# clientes que ligam mais do que 4 vezes, cancelam
    # criar um processo para resolver o problema do cliente em no máximo 3 ligações
    
# clientes em atraso a partir de 20 dias, cancelam
    # política de resolver atrasos com atrasos em até 10 dias (equipe financeira)
    
    
    # clientes do contrato mensal TODOS cancelam
    # oferecer desconto os anos anuais e trimestrais
    
# clientes que ligam mais do que 4 vezes, cancelam
    # criar um processo para resolver o problema do cliente em no máximo 3 ligações
    
# clientes em atraso a partir de 20 dias, cancelam
    # política de resolver atrasos com atrasos em até 10 dias (equipe financeira)

tabela = tabela[tabela["duracao_contrato"]!="Monthly"]
tabela = tabela[tabela["ligacoes_callcenter"]<=4]
tabela = tabela[tabela["dias_atraso"]<=20]
print(tabela["cancelou"].value_counts())
# Em percentual
print(tabela["cancelou"].value_counts(normalize=True))

