import pyautogui
import time
import subprocess
import random
xAgendamento = 1207  # Coordenada X desejada
yAgendamento = 695  # Coordenada Y desejada
xAgendamentoDireita = 1250  # Coordenada X desejada
yAgendamentoDireita = 694  # Coordenada Y desejada
xVoltar = 167
yVoltar = 47
tempo_minimo = 2 #1
tempo_medio = 2 #2.5
xDia = 539
yDia = 396
x_central = 1072
y_central = 351
###################################################################################################
def script_definitivo_click():
    tempo_de_espera = 0.2  

    # Aguardar 2 segundos antes de começar para dar tempo de colocar o foco na janela correta
    time.sleep(2)

    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)
    # Pressionar tab
    pyautogui.press('tab')
    time.sleep(1)
    # Move o mouse para a posição (x, y) na tela
    pyautogui.moveTo(xDia, yDia, duration = 1)
    # Simula um clique na posição atual do mouse
    pyautogui.click()

    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('0')
    pyautogui.write('0')
    pyautogui.write('0')
    pyautogui.write(str(random.randint(0, 9)))

    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################

    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)
    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('0')
    pyautogui.write('0')
    pyautogui.write('3')
    pyautogui.write(str(random.randint(0, 9)))

    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)
    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()

    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('0')
    pyautogui.write('1')
    pyautogui.write('0')
    pyautogui.write(str(random.randint(0, 9)))

    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('0')
    pyautogui.write('1')
    pyautogui.write('3')
    pyautogui.write(str(random.randint(0, 9)))

    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('0')
    pyautogui.write('2')
    pyautogui.write('0')
    pyautogui.write(str(random.randint(0, 9)))

    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('0')
    pyautogui.write('2')
    pyautogui.write('3')
    pyautogui.write(str(random.randint(0, 9)))

    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('0')
    pyautogui.write('3')
    pyautogui.write('0')
    pyautogui.write(str(random.randint(0, 9)))

    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('0')
    pyautogui.write('3')
    pyautogui.write('3')
    pyautogui.write(str(random.randint(0, 9)))

    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('0')
    pyautogui.write('4')
    pyautogui.write('0')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('0')
    pyautogui.write('4')
    pyautogui.write('3')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('0')
    pyautogui.write('5')
    pyautogui.write('0')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('0')
    pyautogui.write('5')
    pyautogui.write('3')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('0')
    pyautogui.write('6')
    pyautogui.write('0')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('0')
    pyautogui.write('6')
    pyautogui.write('3')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('0')
    pyautogui.write('7')
    pyautogui.write('0')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('0')
    pyautogui.write('7')
    pyautogui.write('3')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('0')
    pyautogui.write('8')
    pyautogui.write('0')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('0')
    pyautogui.write('8')
    pyautogui.write('3')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('0')
    pyautogui.write('9')
    pyautogui.write('0')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('0')
    pyautogui.write('9')
    pyautogui.write('3')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('1')
    pyautogui.write('0')
    pyautogui.write('0')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('1')
    pyautogui.write('0')
    pyautogui.write('3')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('1')
    pyautogui.write('1')
    pyautogui.write('0')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('1')
    pyautogui.write('1')
    pyautogui.write('3')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('1')
    pyautogui.write('2')
    pyautogui.write('0')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('1')
    pyautogui.write('2')
    pyautogui.write('3')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('1')
    pyautogui.write('3')
    pyautogui.write('0')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('1')
    pyautogui.write('3')
    pyautogui.write('3')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('1')
    pyautogui.write('4')
    pyautogui.write('0')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('1')
    pyautogui.write('4')
    pyautogui.write('3')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('1')
    pyautogui.write('5')
    pyautogui.write('0')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('1')
    pyautogui.write('5')
    pyautogui.write('3')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('1')
    pyautogui.write('6')
    pyautogui.write('0')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('1')
    pyautogui.write('6')
    pyautogui.write('3')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('1')
    pyautogui.write('7')
    pyautogui.write('0')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('1')
    pyautogui.write('7')
    pyautogui.write('3')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('1')
    pyautogui.write('8')
    pyautogui.write('0')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('1')
    pyautogui.write('8')
    pyautogui.write('3')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('1')
    pyautogui.write('9')
    pyautogui.write('0')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('1')
    pyautogui.write('9')
    pyautogui.write('3')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('2')
    pyautogui.write('0')
    pyautogui.write('0')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('2')
    pyautogui.write('0')
    pyautogui.write('3')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('2')
    pyautogui.write('1')
    pyautogui.write('0')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('2')
    pyautogui.write('1')
    pyautogui.write('3')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('2')
    pyautogui.write('2')
    pyautogui.write('0')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('2')
    pyautogui.write('2')
    pyautogui.write('3')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################

    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('2')
    pyautogui.write('3')
    pyautogui.write('0')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
    ########################################################
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')
    time.sleep(tempo_de_espera)

    # Pressionar tab
    pyautogui.press('tab')
    # Simula um clique na posição atual do mouse
    pyautogui.click()
    # Pressionar ESC três vezes
    for _ in range(6):
        pyautogui.press('backspace')

    # Digitar 2130
    pyautogui.write('2')
    pyautogui.write('3')
    pyautogui.write('3')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')
###################################################################################################
# Espera 2 segundos
time.sleep(3)
# Move o mouse para a posição (x, y) na tela
x1 = 333  # Coordenada X desejada
y1 = 151  # Coordenada Y desejada
pyautogui.moveTo(x1, y1, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_medio)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xAgendamento, yAgendamento, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Executa a função script_definitivo_click
# script_definitivo_click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xVoltar, yVoltar, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Realiza um clique na posição atual do mouse
pyautogui.click()
###################################################################################################
# Mova o ponteiro do mouse para o ponto central
pyautogui.moveTo(x_central, y_central, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Faz o scroll para baixo X "cliques"
pyautogui.scroll(-150)
# ###################################################################################################
# Espera 2 segundos
time.sleep(2)
# Move o mouse para a posição (x, y) na tela
x2 = 300  # Coordenada X desejada
y2 = 208  # Coordenada Y desejada
pyautogui.moveTo(x2, y2, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_medio)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xAgendamento, yAgendamento, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Executa a função script_definitivo_click
# script_definitivo_click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xVoltar, yVoltar, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Realiza um clique na posição atual do mouse
pyautogui.click()
##################################################################################################
# Mova o ponteiro do mouse para o ponto central
pyautogui.moveTo(x_central, y_central, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Faz o scroll para baixo X "cliques"
pyautogui.scroll(-250)
# ###################################################################################################
# Espera 2 segundos
time.sleep(2)
# Move o mouse para a posição (x, y) na tela
x3 = 343  # Coordenada X desejada
y3 = 277  # Coordenada Y desejada
pyautogui.moveTo(x3, y3, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_medio)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xAgendamento, yAgendamento, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Executa a função script_definitivo_click
# script_definitivo_click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xVoltar, yVoltar, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Realiza um clique na posição atual do mouse
pyautogui.click()
###################################################################################################
# Mova o ponteiro do mouse para o ponto central
pyautogui.moveTo(x_central, y_central, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Faz o scroll para baixo X "cliques"
pyautogui.scroll(-150)
###################################################################################################
# Espera 2 segundo
time.sleep(2)
# Move o mouse para a posição (x, y) na tela
x4 = 303  # Coordenada X desejada
y4 = 346  # Coordenada Y desejada
pyautogui.moveTo(x4, y4, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_medio)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xAgendamento, yAgendamento, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Executa a função script_definitivo_click
# script_definitivo_click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xVoltar, yVoltar, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Realiza um clique na posição atual do mouse
pyautogui.click()
###################################################################################################
# Mova o ponteiro do mouse para o ponto central
pyautogui.moveTo(x_central, y_central, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Faz o scroll para baixo X "cliques"
pyautogui.scroll(-150)
###################################################################################################
# Espera 2 segundo
time.sleep(2)
# Move o mouse para a posição (x, y) na tela
x5 = 312  # Coordenada X desejada
y5 = 335  # Coordenada Y desejada
pyautogui.moveTo(x5, y5, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_medio)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xAgendamentoDireita, yAgendamentoDireita, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Executa a função script_definitivo_click
# script_definitivo_click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xVoltar, yVoltar, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Realiza um clique na posição atual do mouse
pyautogui.click()
###################################################################################################
# Mova o ponteiro do mouse para o ponto central
pyautogui.moveTo(x_central, y_central, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Faz o scroll para baixo X "cliques"
pyautogui.scroll(-150)
###################################################################################################
# Espera 2 segundo
time.sleep(2)
# Move o mouse para a posição (x, y) na tela
x6 = 363  # Coordenada X desejada
y6 = 397  # Coordenada Y desejada
pyautogui.moveTo(x6, y6, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_medio)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xAgendamento, yAgendamento, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Executa a função script_definitivo_click
# script_definitivo_click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xVoltar, yVoltar, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Realiza um clique na posição atual do mouse
pyautogui.click()
###################################################################################################
# Mova o ponteiro do mouse para o ponto central
pyautogui.moveTo(x_central, y_central, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Faz o scroll para baixo X "cliques"
pyautogui.scroll(-150)
###################################################################################################
# Espera 2 segundo
time.sleep(2)
# Move o mouse para a posição (x, y) na tela
x7 = 441  # Coordenada X desejada
y7 = 520  # Coordenada Y desejada
pyautogui.moveTo(x7, y7, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_medio)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xAgendamento, yAgendamento, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Executa a função script_definitivo_click
# script_definitivo_click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xVoltar, yVoltar, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Realiza um clique na posição atual do mouse
pyautogui.click()
###################################################################################################
# Mova o ponteiro do mouse para o ponto central
pyautogui.moveTo(x_central, y_central, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Faz o scroll para baixo X "cliques"
pyautogui.scroll(-250)
###################################################################################################
# Espera 2 segundo
time.sleep(2)
# Move o mouse para a posição (x, y) na tela
x8 = 289  # Coordenada X desejada
y8 = 547  # Coordenada Y desejada
pyautogui.moveTo(x8, y8, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_medio)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xAgendamento, yAgendamento, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Executa a função script_definitivo_click
# script_definitivo_click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xVoltar, yVoltar, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Realiza um clique na posição atual do mouse
pyautogui.click()   
###################################################################################################
# Mova o ponteiro do mouse para o ponto central
pyautogui.moveTo(x_central, y_central, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Faz o scroll para baixo X "cliques"
pyautogui.scroll(-350)
###################################################################################################
# Espera 2 segundo
time.sleep(2)
# Move o mouse para a posição (x, y) na tela
x9 = 382  # Coordenada X desejada
y9 = 517  # Coordenada Y desejada
pyautogui.moveTo(x9, y9, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_medio)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xAgendamento, yAgendamento, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Executa a função script_definitivo_click
# script_definitivo_click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xVoltar, yVoltar, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Realiza um clique na posição atual do mouse
pyautogui.click()
###################################################################################################
# Mova o ponteiro do mouse para o ponto central
pyautogui.moveTo(x_central, y_central, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Faz o scroll para baixo X "cliques"
pyautogui.scroll(-350)
###################################################################################################
# Espera 2 segundo
time.sleep(2)
# Move o mouse para a posição (x, y) na tela
x10 = 298  # Coordenada X desejada
y10 = 467  # Coordenada Y desejada
pyautogui.moveTo(x10, y10, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_medio)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xAgendamento, yAgendamento, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Executa a função script_definitivo_click
# script_definitivo_click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xVoltar, yVoltar, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Realiza um clique na posição atual do mouse
pyautogui.click()
###################################################################################################
# Mova o ponteiro do mouse para o ponto central
pyautogui.moveTo(x_central, y_central, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Faz o scroll para baixo X "cliques"
pyautogui.scroll(-350)
###################################################################################################
# Espera 2 segundo
time.sleep(2)
# Move o mouse para a posição (x, y) na tela
x11 = 351  # Coordenada X desejada
y11 = 414  # Coordenada Y desejada
pyautogui.moveTo(x11, y11, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_medio)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xAgendamento, yAgendamento, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Executa a função script_definitivo_click
# script_definitivo_click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xVoltar, yVoltar, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Realiza um clique na posição atual do mouse
pyautogui.click()
###################################################################################################
# Mova o ponteiro do mouse para o ponto central
pyautogui.moveTo(x_central, y_central, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Faz o scroll para baixo X "cliques"
pyautogui.scroll(-350)
###################################################################################################
# Espera 2 segundo
time.sleep(2)
# Move o mouse para a posição (x, y) na tela
x12 = 276  # Coordenada X desejada
y12 = 364  # Coordenada Y desejada
pyautogui.moveTo(x12, y12, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_medio)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xAgendamento, yAgendamento, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Executa a função script_definitivo_click
# script_definitivo_click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xVoltar, yVoltar, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Realiza um clique na posição atual do mouse
pyautogui.click()
###################################################################################################
# Mova o ponteiro do mouse para o ponto central
pyautogui.moveTo(x_central, y_central, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Faz o scroll para baixo X "cliques"
pyautogui.scroll(-350)
###################################################################################################
# Espera 2 segundo
time.sleep(2)
# Move o mouse para a posição (x, y) na tela
x13 = 278  # Coordenada X desejada
y13 = 269  # Coordenada Y desejada
pyautogui.moveTo(x13, y13, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_medio)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xAgendamento, yAgendamento, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Executa a função script_definitivo_click
# script_definitivo_click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xVoltar, yVoltar, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Realiza um clique na posição atual do mouse
pyautogui.click()
###################################################################################################
# Mova o ponteiro do mouse para o ponto central
pyautogui.moveTo(x_central, y_central, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Faz o scroll para baixo X "cliques"
pyautogui.scroll(-350)
###################################################################################################
# Espera 2 segundo
time.sleep(2)
# Move o mouse para a posição (x, y) na tela
x14 = 288  # Coordenada X desejada
y14 = 420  # Coordenada Y desejada
pyautogui.moveTo(x14, y14, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_medio)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xAgendamento, yAgendamento, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Executa a função script_definitivo_click
# script_definitivo_click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xVoltar, yVoltar, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Realiza um clique na posição atual do mouse
pyautogui.click()
###################################################################################################
# Mova o ponteiro do mouse para o ponto central
pyautogui.moveTo(x_central, y_central, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Faz o scroll para baixo X "cliques"
pyautogui.scroll(-350)
###################################################################################################
# Espera 2 segundo
time.sleep(2)
# Move o mouse para a posição (x, y) na tela
x15 = 274  # Coordenada X desejada
y15 = 531  # Coordenada Y desejada
pyautogui.moveTo(x15, y15, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_medio)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xAgendamento, yAgendamento, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Executa a função script_definitivo_click
# script_definitivo_click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xVoltar, yVoltar, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Realiza um clique na posição atual do mouse
pyautogui.click()
###################################################################################################
# Mova o ponteiro do mouse para o ponto central
pyautogui.moveTo(x_central, y_central, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Faz o scroll para baixo X "cliques"
pyautogui.scroll(-350)
###################################################################################################
# Espera 2 segundo
time.sleep(2)
# Move o mouse para a posição (x, y) na tela
x16 = 302  # Coordenada X desejada
y16 = 619  # Coordenada Y desejada
pyautogui.moveTo(x16, y16, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_medio)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xAgendamento, yAgendamento, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Executa a função script_definitivo_click
# script_definitivo_click()
# Espera o tempo minimo
time.sleep(tempo_minimo)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(xVoltar, yVoltar, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Realiza um clique na posição atual do mouse
pyautogui.click()
###################################################################################################
# Mova o ponteiro do mouse para o ponto central
pyautogui.moveTo(x_central, y_central, duration = 1)
# Realiza um clique na posição atual do mouse
pyautogui.click()
# Faz o scroll para baixo X "cliques"
pyautogui.scroll(-350)
###################################################################################################