# pip install pyautogui

import random
import pyautogui
import time

# Aguardar 2 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(2)

# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
# Número de vezes que você deseja pressionar 'Tab'
num_tabs = 10

for _ in range(num_tabs):
    time.sleep(0.5)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'


time.sleep(0.1)
pyautogui.press('right')
time.sleep(0.1)
pyautogui.press('left')
time.sleep(0.1)
pyautogui.press('enter')
time.sleep(0.1)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.1)
pyautogui.press('enter')
# Pressionar ESC três vezes
for _ in range(6):
    pyautogui.press('backspace')

pyautogui.write('0')
pyautogui.write('5')
pyautogui.write('3')
pyautogui.write(str(random.randint(0, 9)))

# Pressionar ENTER
pyautogui.press('enter')
