import pyautogui
import time

# Espera alguns segundos para que você possa posicionar o cursor onde deseja clicar
time.sleep(5)

# Obtém as coordenadas atuais do cursor
x, y = pyautogui.position()

# Imprime as coordenadas
print(f"Coordenadas do mouse: X = {x}, Y = {y}")