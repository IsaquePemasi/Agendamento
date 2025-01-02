import time
import pyautogui
import pyperclip

num_tabs = 11
tempo1 = 1
tempo2 = 2
tempo_final = 20
n=1
# Defina o texto que você quer colar
texto_para_colar = "Mencionou você há 2 minutos\nNossa, não custa nada me dar um oi né?! 🥲"
texto_para_colar2 = "Visualizou seu perfil agorinha mesmo\nEnviou um ♥️ pra ver se chega até vc\nVc pode me devolver o ♥️\nQuero enviar uma msg de voz pra ti, mas não consigo"
texto_para_colar3 = "👤 Mencionou Você\n\nOiii  fala comigo\n\nSou evangélica , aceita minha amizade?"
texto_para_colar4 = "👤 Visitou seu perfil hoje de manhã\nE te enviou uma mensagem de voz\n🎤 Mensagem de voz 0:56\n►||||||||||||||| 0:56"
texto_para_colar5 = ""
#01############################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar)

time.sleep(2) 

pyautogui.hotkey('ctrl', 'r')

time.sleep(2) 

#vai até a postagem
for _ in range(4):
    pyautogui.press('tab')
# Pressionar ENTER
pyautogui.press('enter')

time.sleep(tempo1) 
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'v')
time.sleep(tempo1)
#vai até a opção de envio de imagem
pyautogui.press('tab')
pyautogui.press('enter')    
time.sleep(tempo1)
# Parte onde vai percorrer as imagens
print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4) 
    pyautogui.press('tab') 

time.sleep(0.4)
pyautogui.press('down')
time.sleep(0.4)
pyautogui.press('up')
# Pressionar ENTER
pyautogui.press('enter')
time.sleep(tempo1)
# percorrer até a postagem
for _ in range(6):
    pyautogui.press('tab')

# Postar ENTER
pyautogui.press('enter')
time.sleep(tempo1)
time.sleep(tempo_final) 
pyautogui.hotkey('ctrl', 'r')
#02############################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar2)

time.sleep(2) 

#vai até a postagem
for _ in range(4):
    pyautogui.press('tab')
# Pressionar ENTER
pyautogui.press('enter')

time.sleep(tempo1) 
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'v')
time.sleep(tempo1)
#vai até a opção de envio de imagem
pyautogui.press('tab')
pyautogui.press('enter')    
time.sleep(tempo1)
# Parte onde vai percorrer as imagens
print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4) 
    pyautogui.press('tab') 

time.sleep(0.4)
pyautogui.press('down')
time.sleep(0.4)
pyautogui.press('up')

for _ in range(n):
    time.sleep(0.4) 
    pyautogui.press('down') 

# Pressionar ENTER
pyautogui.press('enter')
time.sleep(tempo1)
# percorrer até a postagem
for _ in range(6):
    pyautogui.press('tab')

# Postar ENTER
pyautogui.press('enter')
time.sleep(tempo1)
time.sleep(tempo_final) 
pyautogui.hotkey('ctrl', 'r')
#03############################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar3)
n = n + 1
time.sleep(2) 

#vai até a postagem
for _ in range(4):
    pyautogui.press('tab')
# Pressionar ENTER
pyautogui.press('enter')

time.sleep(tempo1) 
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'v')
time.sleep(tempo1)
#vai até a opção de envio de imagem
pyautogui.press('tab')
pyautogui.press('enter')    
time.sleep(tempo1)
# Parte onde vai percorrer as imagens
print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4) 
    pyautogui.press('tab') 

time.sleep(0.4)
pyautogui.press('down')
time.sleep(0.4)
pyautogui.press('up')

for _ in range(n):
    time.sleep(0.4) 
    pyautogui.press('down') 

# Pressionar ENTER
pyautogui.press('enter')
time.sleep(tempo1)
# percorrer até a postagem
for _ in range(6):
    pyautogui.press('tab')

# Postar ENTER
pyautogui.press('enter')
time.sleep(tempo1)
time.sleep(tempo_final) 
pyautogui.hotkey('ctrl', 'r')
#04############################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar4)
n = n + 1
time.sleep(2) 

#vai até a postagem
for _ in range(4):
    pyautogui.press('tab')
# Pressionar ENTER
pyautogui.press('enter')

time.sleep(tempo1) 
# Pressionar CTRL + V
pyautogui.hotkey('ctrl', 'v')
time.sleep(tempo1)
#vai até a opção de envio de imagem
pyautogui.press('tab')
pyautogui.press('enter')    
time.sleep(tempo1)
# Parte onde vai percorrer as imagens
print("Selecionando a midia!")
for _ in range(num_tabs):
    time.sleep(0.4) 
    pyautogui.press('tab') 

time.sleep(0.4)
pyautogui.press('down')
time.sleep(0.4)
pyautogui.press('up')

for _ in range(n):
    time.sleep(0.4) 
    pyautogui.press('down') 

# Pressionar ENTER
pyautogui.press('enter')
time.sleep(tempo1)
# percorrer até a postagem
for _ in range(6):
    pyautogui.press('tab')

# Postar ENTER
pyautogui.press('enter')
time.sleep(tempo1)
time.sleep(tempo_final) 
pyautogui.hotkey('ctrl', 'r')