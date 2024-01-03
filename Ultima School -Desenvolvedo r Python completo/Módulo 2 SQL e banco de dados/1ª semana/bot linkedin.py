import pyautogui
import time

# Número de repetições desejado
num_repeticoes = 50

# Espera alguns segundos para que você possa posicionar o cursor onde deseja clicar
time.sleep(2)

# Loop para repetir o bloco de código
for _ in range(num_repeticoes):
    # Clicando na vaga
    pyautogui.click(370, 422)

    # Descendo 4 vezes
    for _ in range(4):
        pyautogui.click(745, 994)

    # Clicando em aplicar
    pyautogui.click(857, 658)

    # Voltando para a página do LinkedIn
    pyautogui.hotkey('ctrl', 'pageup')

    # Clicando em sim
    pyautogui.click(1364, 810)

    # Espera um pouco entre cada repetição (opcional)
    time.sleep(1)