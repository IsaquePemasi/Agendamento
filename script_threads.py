import time
import pyautogui
import pyperclip

num_tabs = 11
tempo1 = 1
tempo2 = 2
tempo_final = 16
n=1
x = n + 1
mensagem = f"Imagem {n} postada"

# Defina o texto que você quer colar
texto_para_colar1 = "Mencionou você há 2 minutos\nNossa, não custa nada me dar um oi né?! 🥲"
texto_para_colar2 = "Oiii  fala comigo\nSou evangélica , aceitar minha amizade ?"
texto_para_colar3 = "Visualizou seu perfil agorinha mesmo\nEnviou um ♥️ pra ver se chega até vc\nVc pode me devolver o ♥️\nQuero enviar uma msg de voz pra ti, mas não consigo"
texto_para_colar4 = "Mencionou você há 2 minutos\nNossa, não custa nada me dar um oi né?! 🥲"
texto_para_colar5 = "Oie moço ❤️🌹\nToda noite eu fico\nImaginando, como seria\nDormir ao seu lado\ne principalmente!\nAcordar ....\nSentindo os seus beijos🥹\nSou louca\nPor você!\nPô, fica\nComigo?"
texto_para_colar6 = "👤 Mencionou Você\nOiii  fala comigo\nSou evangélica , aceitar minha amizade?"
texto_para_colar7 = "👤 Visitou seu perfil hoje de manhã\nE te enviou uma mensagem de voz\n🎤 Mensagem de voz 0:56\n►||||||||||||||| 0:56"
texto_para_colar8 = "🥺 Me desculpa por ter enviado solicitação de amizade...\nParece que você não gostou, não vou enviar mais, tá bom? 💔\nMas não custa nada me dar um oi né?! 🥲"
texto_para_colar9 = "👤(1) enviou uma solicitação de amizade pra você\n👤(1) enviou uma solicitação de amizade pra você\n👤(1) enviou uma solicitação de amizade pra você\n👤(1) enviou uma solicitação de amizade pra você\n👤(1) enviou uma solicitação de amizade pra você\n👤(1) enviou uma solicitação de amizade pra você\n👤(1) enviou uma solicitação de amizade pra você\n👤(1) enviou uma solicitação de amizade pra você\n👤(1) enviou uma solicitação de amizade pra você\n👤(1) enviou uma solicitação de amizade pra você"
texto_para_colar10 = "👤 Adorou você\nNossa, tô te curtindo muito e você nem percebe, homem difícil…"
texto_para_colar11 = "Que homem lindooooo!♥️♥️♥️\nMisericórdia!\nQuero ser sua esposa!\nMeu gostosoo"
texto_para_colar12 = "👤 (1) Começou a seguir você\n🟢 Online\nOiii\nTudo bem com você? 🥰"
texto_para_colar13 = "👤(1) enviou uma solicitação de amizade pra você\nEu te chamei na rua e você não escutou\nPq vc me ignorou moço?\nQueria conversar com vc"
texto_para_colar14 = "Te enviou 3 mensagens 👤\nOi\n🎤 Mensagem de voz 0:52\n►||||||||||||||||||||||||||||||||| 0:52❤️\nBom dia ☀️"
texto_para_colar15 = "Deixa eu pergunta amor\nVocê tem medo de mulher?? Será que você é tchola? 🙄🙄\nVc só me ignora😔"
texto_para_colar16 = "👤 Te enviou 12 mensagens\nOiii, meu bem\nVai me responder não?\nTe dou tanta bola e você nem me da um coração ❤️\nTudo bem?"
texto_para_colar17 = "Gato, mandei mensagem e você nem ligou🥺\nCurte aqui que eu mando novamente..\nMas vai ser a última vez\nPosso chamar"
texto_para_colar18 = "Te enviou uma solicitação no Threads\nAceitar 👤 Excluir ❌"
texto_para_colar19 = "👤 Mencionou Você\nOii fala comigo\nvocê aceita minha amizade?🥰\n👤 começou a seguir você\n🟢 Online"
texto_para_colar20 = "👤 Não vou te enviar mais nenhum pedido\nChega né 😅\nComecei a te seguir e vc nem viu"
texto_para_colar21 = "Está pedindo para ser tua amiga aqui e no Instagram\n✅ Aceitar"
texto_para_colar22 = "Te enviou 2 mensagens e um áudio👀🥰👤\nOi\n🎤 Mensagem de voz 0:01\n►||||||||||||||||||||||||||||||||| 0:01❤️"
texto_para_colar23 = "Solteira moro com meus pais, trabalhadora e boa mulher, mas ninguém quer por ser pobre e se campo 😫💔🥹"
texto_para_colar24 = "Quero um beijo seu\nTe achei lindo, estou bem pertinho de você\nA 3km de distância\nMe aceita como sua amiga?"
texto_para_colar25 = "Solteira, sei cozinha, tomo uma, trabalho, não tenho filho.\nApareça, minha alma gêmea! kkkkk"
texto_para_colar26 = "👤 Mencionou Você 👀💌🥰\nQuero um beijo seu\nTe achei lindo, estou bem pertinho de você\nA 3km de distância\nMe aceita como sua amiga?\n👤 Mencionou Você 👀💌🥰"
texto_para_colar27 = "Visitou seu perfil 5 vezes\n👤(1) enviou uma solicitação de amizade para você"
texto_para_colar28 = "Que tédio 🙄\nOiii Homen 💬\nQuando vai realmente pegar meu número?\nJá tou te esperando faz tempos e você não aparece\nnem da um curti para eu saber que você está aí"
texto_para_colar29 = "Oi! 💬\nTe enviei uma mensagem super importante e ainda não tive resposta 😢\nVocê pode deixar um ❤️ só pra eu saber que viu? Isso já faria meu dia! ☺️"
texto_para_colar30 = "Oi moço 😘😍\nMeu ex me batia sempre\nVocê não é assim né moço?\nPromete que vai cuidar de mim?🥺💓"
texto_para_colar31 = "Mencionou você\n🟢 Online\nQueria tanto ser sua amiga no TELEGRAM"
texto_para_colar32 = "Oii gato, boa noite! ❤️\nAchei você um homem lindo!"
texto_para_colar33 = "Por quê quando falamos de Jesus aqui ninguém curte??❤️‍🩹🥹??????????????"
texto_para_colar34 = "👤 Te enviou 3 mensagem\nOiiii, boa noite!! ❤️\nVai me responder não?\nLer mais..."
texto_para_colar35 = "👤mencionou você e deixou uma mensagem ⬇️\nSou evangélica 🥹 Paz do senhor 🫶🏻, Qual sua religião?"
texto_para_colar36 = "Começou a seguir vc há três( 3) dias"
texto_para_colar37 = "Oi! Te mandei uma mensagem e não recebi a resposta.\nPelo menos manda um ❤️ pra eu saber que você curtiu. Você é casado?"
texto_para_colar38 = "Te mandou uma mensagem (1)\nOi por que você nunca fala cmg ?\nA gente podia ser amigos né 🥰👤mencionou você"
texto_para_colar39 = "Te enviei varias mensagens e vc nunca responde!\nComeçou a seguir você, aceita minha solicitação?\nPode curti pra eu saber que vc viu essa? ❤️"
texto_para_colar40 = "Oi moço!!!❤️🌹\nBoa tarde 😘\nOlhei suas fotos no Instagram 🫶🏼\nCom todo respeito, você é bem bonito!!!😍\n👤 Mencionou você 🫶🏼❤️\nVocê e casado?\n🟢 Online"
texto_para_colar41 = "👤 Mencionou Você\nOiii fala comigo, vi suas fotos no Instagram e amei\nJessica começou a seguir você\nCasado? De onde você é?\n🟢 Online"
texto_para_colar42 = "👤 Mencionou você há 2 minutos\nNossa, não custa nada me dar um oi né?!😅👤Aceita minha amizade💌"
texto_para_colar43 = "Visualizou seu perfil agorinha mesmo\nEnviou um ♥️ pra ver se chega até vc\nVc pode me devolver o ♥️\nQuero enviar uma msg de voz pra ti, mas não consigo"
texto_para_colar44 = "MENCIONOU VOCÊ!\nOi, posso te seguir?"
texto_para_colar45 = "👤Mencionou você agora…\nEstava olhando seu perfil aqui e Deus me falou isso sobre você:\nDeus tem promessa para sua vida muito grande, muita honra está chegando para você, amém !??❤️🙏🏻"
texto_para_colar46 = "👤 Eu quero me desculpar pois não aceitou a minha solicitação de amizade, não deve ter gostado quando enviei. Mas tudo bem, um abraço ❤️\nNão foi por mal 🥺"
texto_para_colar47 = "① foto\n① foto\n① foto\nNão abre a foto perto de ninguém tá?? 🤫🤫🤫"
texto_para_colar48 = "👤 te curtiu várias vezes📩\n\"Difícil chamar sua atenção, mas eu não desisto! ❤️\""
texto_para_colar49 = "❤️Se você me ama me deixa saber ❤️🥺"
texto_para_colar50 = "Te curti 15 vezes e você nem tem coragem de apertar um coração ❤️"
# texto_para_colar51 = "Mulher de 40 e velha! Eu sendo velha aos 40 🤭🤭🤭"
#01############################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar1)

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
print("Selecionando a midia...")
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

print("1 imagem postada!")
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
print("Selecionando a midia...")
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
print("2 imagens postadas!")
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
print("Selecionando a midia...")
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

print("3 imagens postadas!")
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
print("Selecionando a midia...")
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

print("4 imagens postadas!")
#05############################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar5)
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
print("Selecionando a midia...")
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

print("5 imagens postadas!")
#06############################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar6)
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
print("Selecionando a midia...")
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

print("6 imagens postadas!")
#07############################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar7)
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
print("Selecionando a midia...")
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

print("7 imagens postadas!")
#08############################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar8)
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
print("Selecionando a midia...")
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

print("8 imagens postadas!")
#09############################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar9)
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
print("Selecionando a midia...")
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

print("9 imagens postadas!")
#10##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar10)
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
print("Selecionando a midia...")
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

print("10 imagens postadas!")
#11##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar11)
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
print("Selecionando a midia...")
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

print("11 imagens postadas!")
#12##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar12)
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
print("Selecionando a midia...")
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

print("12 imagens postadas!")
#13##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar13)
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
print("Selecionando a midia...")
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

print("13 imagens postadas!")
#14############################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar14)
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
print("Selecionando a midia..")
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

print("14 imagens postadas!")
#15##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar15)
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
print("Selecionando a midia...")
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

print("15 imagens postadas!")
#16##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar16)
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
print("Selecionando a midia...")
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

print("16 imagens postadas!")
#17##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar17)
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
print("Selecionando a midia...")
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

print("17 imagens postadas!")
#18##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar18)
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
print("Selecionando a midia...")
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

print("18 imagens postadas!")
#19##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar19)
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
print("Selecionando a midia...")
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

print("19 imagens postadas!")
#20##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar20)
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
print("Selecionando a midia...")
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

print("20 imagens postadas!")
#21##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar21)
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
print("Selecionando a midia...")
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

print("21 imagens postadas!")
#22##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar22)
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
print("Selecionando a midia...")
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

print("22 imagens postadas!")
#23##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar23)
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
print("Selecionando a midia...")
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

print("23 imagens postadas!")
#24###########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar24)
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
print("Selecionando a midia...")
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

print("24 imagens postadas!")
#25#########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar25)
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
print("Selecionando a midia...")
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

print("25 imagens postadas!")
#26##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar26)
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
print("Selecionando a midia...")
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

print("26 imagens postadas!")
#27##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar27)
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
print("Selecionando a midia...")
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

print("27 imagens postadas!")
#28##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar28)
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
print("Selecionando a midia...")

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

print("28 imagens postadas!")
#29##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar29)
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
print("Selecionando a midia...")
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

print("29 imagens postadas!")
#30##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar30)
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
print("Selecionando a midia...")

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

print("30 imagens postadas!")
#31##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar31)
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
print("Selecionando a midia...")

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

print("31 imagens postadas!")

#32##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar32)
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
print("Selecionando a midia...")

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

print("32 imagens postadas!")

#33##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar33)
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
print("Selecionando a midia...")

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

print("33 imagens postadas!")

#34###########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar34)
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
print("Selecionando a midia...")

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

print("34 imagens postadas!")

#35##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar35)
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
print("Selecionando a midia...")

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

print("35 imagens postadas!")

#36##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar36)
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
print("Selecionando a midia...")

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

print("36 imagens postadas!")

#37##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar37)
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
print("Selecionando a midia...")

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

print("37 imagens postadas!")

#38##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar38)
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
print("Selecionando a midia...")

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

print("38 imagens postadas!")

#39##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar39)
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
print("Selecionando a midia...")

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

print("39 imagens postadas!")

#40##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar40)
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
print("Selecionando a midia...")

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

print("40 imagens postadas!")

#41##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar41)
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
print("Selecionando a midia...")

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

print("41 imagens postadas!")

#42##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar42)
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
print("Selecionando a midia...")

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

print("42 imagens postadas!")

#43#########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar43)
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
print("Selecionando a midia...")

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

print("43 imagens postadas!")

#44##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar44)
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
print("Selecionando a midia...")

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

print("44 imagens postadas!")

#45##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar45)
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
print("Selecionando a midia...")

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

print("45 imagens postadas!")

#46##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar46)
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
print("Selecionando a midia...")

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

print("46 imagens postadas!")

#47##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar47)
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
print("Selecionando a midia...")

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

print("47 imagens postadas!")

#48##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar48)
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
print("Selecionando a midia...")

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

print("48 imagens postadas!")

#49##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar49)
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
print("Selecionando a midia...")

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

print("49 imagens postadas!")

#50##########################################################################
# Copia o texto para o clipboard
pyperclip.copy(texto_para_colar50)
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
print("Selecionando a midia...")
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

print("50 imagens postadas!")

#############################################################################