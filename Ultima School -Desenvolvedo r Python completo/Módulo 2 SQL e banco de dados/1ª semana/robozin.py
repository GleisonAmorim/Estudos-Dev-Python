import pyautogui
import time

# Espera alguns segundos para que você possa posicionar o cursor onde deseja clicar
time.sleep(2)

# Obtém as coordenadas atuais do cursor
x, y = pyautogui.position()

# Clica na posição atual do cursor
pyautogui.click(x, y)

# Simula a tecla Ctrl pressionada
pyautogui.keyDown('ctrl')

# Simula a tecla Page Up pressionada
pyautogui.press('pageup')

# Libera a tecla Ctrl
pyautogui.keyUp('ctrl')