# pip install pyautogui

import random
import pyautogui
import time

###############################################################################################################
# Aguardar 2 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(2)

# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'o')
# Número de vezes que você deseja pressionar 'Tab'
num_tabs = 10

for _ in range(num_tabs):
    time.sleep(0.4)  # Pausa
    pyautogui.press('tab')  # Pressiona 'Tab'

pyautogui.press('right')
pyautogui.press('left')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.4)
pyautogui.press('enter')

# Pressionar ESC várias vezes
for _ in range(6):
    pyautogui.press('backspace')


pyautogui.write('0')
pyautogui.write('5')
pyautogui.write('3')
pyautogui.write(str(random.randint(0, 9)))

pyautogui.press('enter')
###############################################################################################################