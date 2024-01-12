import pyautogui
# clicar = pyautogui.click
# escrever = pyautogui.write
# apertar uma tecla = pyautogui.press ex: 
# atalho = pyautogui.hotkey
# scroll (rolar) = pyautogui.scroll

# import time #biblioteca time
# time.sleep(5) exemplo de como fazer pausa de um tempo específico em um comando específico

# Passo a passo
# 1 Entrar no sistema da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/login
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" #definindo a variável link
user = "pythonimpressionador@gmail.com" #definindo a variável user
psw = "minha senha"
pyautogui.PAUSE = 0.5 # espera meio segundo a cada comando
pyautogui.press("win") # aperta a tecla do windoes (comand + barra de espaço)
pyautogui.write("chrome") # digita o nome do programa (chrome)
pyautogui.press("enter") # aperta a tecla enter
pyautogui.write(link) # cola o link no navegador
pyautogui.press("enter") # aperta a tecla enter
pyautogui.press("tab") # aperta a tecla tab 1 vez
    
# 2 Fazer login
pyautogui.write(user) # digita o usuário
pyautogui.press("tab") # aperta a tecla tab 1 vez e passa para o campo de senha
pyautogui.write(psw) # digita a senha
pyautogui.press("tab") # aperta a tecla tab 1 vez para selecionar o botão "logar"
pyautogui.press("enter") # aperta a tecla enter

# 3 Importar base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index: # repete os comandos indentados para cada linha da tabela

    # 4 Cadastrar um produto
    pyautogui.click(x=789, y=258)

    #codigo
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")

    #marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    #tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    #preco_unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    #obs
    
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs): # tratando situações onde não tem nada escrito em OBS
        pyautogui.write(obs)
        
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000) #colocando números positivos rola para cima, números negativos rola para baixo

# 5 Repetir isso até a acabar a base

