import random
import pyautogui
import time

n=1
# Número de vezes que você deseja pressionar 'Tab'
num_tabs = 10
# tempo (segundos) de aguardo para o CTRL + C, talvez precise de mais por conta de caracteres especiais 
tempo_control_v = 2
# Aguardar 2 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(3)

# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(2)
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

#######################################################################################
# Aguardar 2 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)

# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n): 
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
# Aguardar 1 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(1)
n = n + 1
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
time.sleep(2)

print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

time.sleep(0.5)
pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('left')
print("midia selecionada!")

for _ in range(n):
    pyautogui.press('right') 

time.sleep(0.5)
pyautogui.press('enter')
print("copy selecionada!")

time.sleep(tempo_control_v)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
print("escolhendo o horario!")
# Pressionar tab
pyautogui.press('tab')
time.sleep(1)
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
#######################################################################################
