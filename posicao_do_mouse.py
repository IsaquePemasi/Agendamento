import pyautogui
import time

# Espera 5 segundos para você mover o mouse para a posição desejada
print("Mova o mouse para a posição desejada na tela. Você tem 5 segundos.")
time.sleep(5)

# Obtém a posição atual do mouse
x, y = pyautogui.position()
print(f"A posição atual do mouse é: ({x}, {y})")