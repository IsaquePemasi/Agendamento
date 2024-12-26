import pyautogui
num_tabs = 10

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

# Parte onde vai percorrer as imagens
print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4) 
    pyautogui.press('tab') 

# Pressionar ENTER
pyautogui.press('enter')

# percorrer até a postagem
for _ in range(6):
    pyautogui.press('tab')

# Postar ENTER
#pyautogui.press('enter')

pyautogui.hotkey('ctrl', 'r')
#############################################################################
