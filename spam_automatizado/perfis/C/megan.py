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
xDia = 827
yDia = 329
x_central = 1072
y_central = 351
x1 = 342  # Coordenada X desejada
y1 = 156  # Coordenada Y desejada
x2 = 318  # Coordenada X desejada
y2 = 211  # Coordenada Y desejada
x3 = 321  # Coordenada X desejada
y3 = 269  # Coordenada Y desejada
x4 = 313  # Coordenada X desejada
y4 = 259  # Coordenada Y desejada
x5 = 312  # Coordenada X desejada
y5 = 247  # Coordenada Y desejada
x6 = 308  # Coordenada X desejada
y6 = 233  # Coordenada Y desejada
x7 = 306  # Coordenada X desejada
y7 = 221  # Coordenada Y desejada
x8 = 309  # Coordenada X desejada
y8 = 209  # Coordenada Y desejada
x9 = 306  # Coordenada X desejada
y9 = 194  # Coordenada Y desejada
x10 = 301  # Coordenada X desejada
y10 = 185  # Coordenada Y desejada
x11 = 313  # Coordenada X desejada
y11 = 174  # Coordenada Y desejada
x12 = 327  # Coordenada X desejada
y12 = 162  # Coordenada Y desejada
x13 = 321  # Coordenada X desejada
y13 = 150  # Coordenada Y desejada
x14 = 311  # Coordenada X desejada
y14 = 138  # Coordenada Y desejada
x15 = 318  # Coordenada X desejada
y15 = 124  # Coordenada Y desejada
x16 = 388  # Coordenada X desejada
y16 = 183  # Coordenada Y desejada
x17 = 338  # Coordenada X desejada
y17 = 289  # Coordenada Y desejada
x18 = 336  # Coordenada X desejada
y18 = 362  # Coordenada Y desejada
x19 = 391  # Coordenada X desejada
y19 = 473  # Coordenada Y desejada
x20 = 308  # Coordenada X desejada
y20 = 618  # Coordenada Y desejada
###################################################################################################
def script_definitivo_click():
    tempo_de_espera = 0.2  

    # Aguardar 2 segundos antes de começar para dar tempo de colocar o foco na janela correta
    time.sleep(1)

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
    pyautogui.write('1')
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
    pyautogui.write('4')
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
    pyautogui.write('1')
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
    pyautogui.write('4')
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
    pyautogui.write('1')
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
    pyautogui.write('4')
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
    pyautogui.write('1')
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
    pyautogui.write('4')
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
    pyautogui.write('1')
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
    pyautogui.write('4')
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
    pyautogui.write('1')
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
    pyautogui.write('4')
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
    pyautogui.write('1')
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
    pyautogui.write('4')
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
    pyautogui.write('1')
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
    pyautogui.write('4')
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
    pyautogui.write('1')
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
    pyautogui.write('4')
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
    pyautogui.write('1')
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
    pyautogui.write('4')
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
    pyautogui.write('1')
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
    pyautogui.write('4')
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
    pyautogui.write('1')
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
    pyautogui.write('4')
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
    pyautogui.write('1')
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
    pyautogui.write('4')
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
    pyautogui.write('1')
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
    pyautogui.write('4')
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
    pyautogui.write('1')
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
    pyautogui.write('4')
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
    pyautogui.write('1')
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
    pyautogui.write('4')
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
    pyautogui.write('1')
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
    pyautogui.write('4')
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
    pyautogui.write('1')
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
    pyautogui.write('4')
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
    pyautogui.write('1')
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
    pyautogui.write('4')
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
    pyautogui.write('1')
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
    pyautogui.write('4')
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
    pyautogui.write('1')
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
    pyautogui.write('4')
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
    pyautogui.write('1')
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
    pyautogui.write('4')
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
    pyautogui.write('1')
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
    pyautogui.write('4')
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
    pyautogui.write('1')
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
    pyautogui.write('4')
    pyautogui.write(str(random.randint(0, 9)))
        
    # Pressionar ENTER
    pyautogui.press('enter')

########################################################
###############################################################
# Espera 2 segundos
time.sleep(1)
# Move o mouse para a posição (x, y) na tela
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
script_definitivo_click()
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
pyautogui.scroll(-10)
###################################################################################################
# Espera 2 segundos
time.sleep(1)
# Move o mouse para a posição (x, y) na tela
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
script_definitivo_click()
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
pyautogui.scroll(-10)
# ###################################################################################################
# Espera 2 segundos
time.sleep(1)
# Move o mouse para a posição (x, y) na tela
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
script_definitivo_click()
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
time.sleep(1)
# Move o mouse para a posição (x, y) na tela
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
script_definitivo_click()
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
time.sleep(1)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(x5, y5, duration = 1)
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
script_definitivo_click()
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
time.sleep(1)
# Move o mouse para a posição (x, y) na tela
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
script_definitivo_click()
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
time.sleep(1)
# Move o mouse para a posição (x, y) na tela
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
script_definitivo_click()
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
time.sleep(1)
# Move o mouse para a posição (x, y) na tela
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
script_definitivo_click()
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
time.sleep(1)
# Move o mouse para a posição (x, y) na tela
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
script_definitivo_click()
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
time.sleep(1)
# Move o mouse para a posição (x, y) na tela
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
script_definitivo_click()
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
time.sleep(1)
# Move o mouse para a posição (x, y) na tela
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
script_definitivo_click()
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
time.sleep(1)
# Move o mouse para a posição (x, y) na tela
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
script_definitivo_click()
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
time.sleep(1)
# Move o mouse para a posição (x, y) na tela
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
script_definitivo_click()
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
time.sleep(1)
# Move o mouse para a posição (x, y) na tela
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
script_definitivo_click()
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
time.sleep(1)
# Move o mouse para a posição (x, y) na tela
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
script_definitivo_click()
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
time.sleep(1)
# Move o mouse para a posição (x, y) na tela
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
script_definitivo_click()
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
time.sleep(1)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(x17, y17, duration = 1)
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
script_definitivo_click()
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
time.sleep(1)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(x18, y18, duration = 1)
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
script_definitivo_click()
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
time.sleep(1)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(x19, y19, duration = 1)
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
script_definitivo_click()
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
time.sleep(1)
# Move o mouse para a posição (x, y) na tela
pyautogui.moveTo(x20, y20, duration = 1)
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
script_definitivo_click()
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