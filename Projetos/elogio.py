#Aula - Funções 01/11

def elogio_professor_programacao(nome_professor):
    elogio = f"O {nome_professor} é como um compilador perfeito - ele transforma códigos bagunçados em obras-primas de programação!"
    return elogio

professor = "Sherlon"
elogio_sherlon = elogio_professor_programacao(professor)
print(elogio_sherlon)