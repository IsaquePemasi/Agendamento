# pip install pyautogui

import random
import pyautogui
import time

# Aguardar 2 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(2)

# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'v')

# Pressionar ENTER
pyautogui.press('enter')
# Pressionar tab
pyautogui.press('tab')
time.sleep(3)
# Simula um clique na posição atual do mouse
pyautogui.click()
print("Mouse travado na posição:", (x, y))
print("Pressione Ctrl+C para sair.")

# Loop para manter o mouse na posição
try:
    while True:
        current_x, current_y = pyautogui.position()
        if (current_x, current_y) != (x, y):
            # Move o mouse de volta para a posição original
            pyautogui.moveTo(x, y)
except KeyboardInterrupt:
    print("Saindo...")

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
########################################################