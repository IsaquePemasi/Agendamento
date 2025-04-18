import pyautogui
import time
import subprocess
import random
xAgendamento = 1208  # Coordenada X desejada
yAgendamento = 741  # Coordenada Y desejada
xAgendamentoDireita = 1254  # Coordenada X desejada
yAgendamentoDireita = 743  # Coordenada Y desejada
xVoltar = 162
yVoltar = 50
tempo_minimo = 1 #1 #3 esta funcionando
tempo_medio = 1 #2.5 #3 esta funcionando
xDia = 827
yDia = 353
x_central = 1072
y_central = 351
x1 = 314  # Coordenada X desejada
y1 = 153  # Coordenada Y desejada
x2 = 325  # Coordenada X desejada
y2 = 213  # Coordenada Y desejada
x3 = 313  # Coordenada X desejada
y3 = 269  # Coordenada Y desejada
x4 = 308  # Coordenada X desejada
y4 = 259  # Coordenada Y desejada
x5 = 312  # Coordenada X desejada
y5 = 246  # Coordenada Y desejada
x6 = 300  # Coordenada X desejada
y6 = 232  # Coordenada Y desejada
x7 = 304  # Coordenada X desejada
y7 = 222  # Coordenada Y desejada
x8 = 295  # Coordenada X desejada
y8 = 210  # Coordenada Y desejada
x9 = 314  # Coordenada X desejada
y9 = 199  # Coordenada Y desejada
x10 = 312  # Coordenada X desejada
y10 = 186  # Coordenada Y desejada
x11 = 308  # Coordenada X desejada
y11 = 172  # Coordenada Y desejada
x12 = 322  # Coordenada X desejada
y12 = 161  # Coordenada Y desejada
x13 = 315  # Coordenada X desejada
y13 = 148  # Coordenada Y desejada
x14 = 313  # Coordenada X desejada
y14 = 136  # Coordenada Y desejada
x15 = 333  # Coordenada X desejada
y15 = 124  # Coordenada Y desejada
x16 = 398  # Coordenada X desejada
y16 = 171  # Coordenada Y desejada
x17 = 343  # Coordenada X desejada
y17 = 285  # Coordenada Y desejada
x18 = 287  # Coordenada X desejada
y18 = 410  # Coordenada Y desejada
x19 = 444  # Coordenada X desejada
y19 = 526  # Coordenada Y desejada
x20 = 305  # Coordenada X desejada
y20 = 665  # Coordenada Y desejada
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