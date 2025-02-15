import pyautogui
import time

# Espera 5 segundos antes de executar o scroll
time.sleep(5)

# Faz o scroll para baixo 10 "cliques"
pyautogui.scroll(-10)

# Espera 5 segundos antes de mover o mouse
time.sleep(5)

# Move o mouse para a posição (x, y) na tela
x = 500  # Coordenada X desejada
y = 300  # Coordenada Y desejada
pyautogui.moveTo(x, y)