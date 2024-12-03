# pip install pyautogui

import pyautogui
import time

# Aguardar 2 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(2)

# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'v')

# Pressionar ENTER
pyautogui.press('enter')

# Pressionar ESC três vezes
for _ in range(3):
    pyautogui.press('esc')

# Digitar 2030
pyautogui.write('2030')

# Pressionar ENTER
pyautogui.press('enter')