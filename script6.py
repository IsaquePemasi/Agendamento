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
for _ in range(6):
    pyautogui.press('backspace')

# Digitar 2130
    pyautogui.write('2')
    pyautogui.write('3')
    pyautogui.write('3')
    pyautogui.write('0')

# Pressionar ENTER
pyautogui.press('enter')

# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'v')

# Pressionar ENTER
pyautogui.press('enter')

# Pressionar ESC três vezes
for _ in range(6):
    pyautogui.press('backspace')

# Digitar 2130
    pyautogui.write('2')
    pyautogui.write('3')
    pyautogui.write('3')
    pyautogui.write('2')

# Pressionar ENTER
pyautogui.press('enter')