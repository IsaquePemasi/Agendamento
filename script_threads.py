import pyautogui# Pressionar ESC três vezes
#vai até a postagem
for _ in range(4):
    pyautogui.press('tab')
# Pressionar ENTER
pyautogui.press('enter')
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'v')
#vai até a opção de envio de imagem
pyautogui.press('tab')
pyautogui.press('enter')    

# Parte pnde vai percorrer as imagens

# Pressionar ENTER
pyautogui.press('enter')

for _ in range(6):
    pyautogui.press('tab')

# Pressionar ENTER
pyautogui.press('enter')

pyautogui.hotkey('ctrl', 'r')