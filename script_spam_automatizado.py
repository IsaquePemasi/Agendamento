import pyautogui
import time
import subprocess

# Move o mouse para a posição (x, y) na tela
xAgendamento = 1207  # Coordenada X desejada
yAgendamento = 742  # Coordenada Y desejada
xVoltar = 354
yVoltar = 46
tempo_minimo = 1
# Faz o scroll para baixo X "cliques"
# pyautogui.scroll(-1000)
####################################################################################################
# Espera 2 segundos
time.sleep(2)
# Move o mouse para a posição (x, y) na tela
x1 = 536  # Coordenada X desejada
y1 = 231  # Coordenada Y desejada
pyautogui.moveTo(x1, y1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xAgendamento, yAgendamento)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Executa o script_definitivo_click.py
subprocess.run(["python", "script_definitivo_click.py"])
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xVoltar, yVoltar)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Realiza um clique na posição atual do mouse
pyautogui.click()
####################################################################################################