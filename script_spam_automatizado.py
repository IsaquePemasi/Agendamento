import pyautogui
import time

# Move o mouse para a posição (x, y) na tela
xAgendamento = 1207  # Coordenada X desejada
yAgendamento = 742  # Coordenada Y desejada

# Faz o scroll para baixo X "cliques"
# pyautogui.scroll(-1000)
###############################################################################################################
# Espera 2 segundos
time.sleep(2)

# Move o mouse para a posição (x, y) na tela
x1 = 566  # Coordenada X desejada
y1 = 213  # Coordenada Y desejada
pyautogui.moveTo(x1, y1)

# Realiza um clique na posição atual do mouse
pyautogui.click()

# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xAgendamento, yAgendamento)

# Realiza um clique na posição atual do mouse
pyautogui.click()

# quero que execute o script_definitivo.py aqui