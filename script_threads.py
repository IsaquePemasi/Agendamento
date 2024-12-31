import time
import pyautogui

num_tabs = 10
tempo = 2

# Defina o texto que você quer colar
texto_para_colar = "Seu texto aqui"

# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar)

time.sleep(2) 

#vai até a postagem
for _ in range(4):
    pyautogui.press('tab')
# Pressionar ENTER
pyautogui.press('enter')

time.sleep(tempo) 
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
