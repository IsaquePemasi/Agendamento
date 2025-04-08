import pyautogui
import time

# Função para atualizar variáveis no arquivo
def atualizar_variaveis_arquivo(caminho_arquivo, x, y):
    try:
        with open(caminho_arquivo, 'r') as file:
            linhas = file.readlines()

        with open(caminho_arquivo, 'w') as file:
            for linha in linhas:
                if linha.strip().startswith("xDia ="):
                    file.write(f"xDia = {x}\n")
                elif linha.strip().startswith("yDia ="):
                    file.write(f"yDia = {y}\n")
                else:
                    file.write(linha)
        print(f"Atualizado {caminho_arquivo}")
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_arquivo}")

# Recebe a escolha do usuário
escolha = input("Digite A, B ou C para selecionar o conjunto de arquivos: ").strip().upper()

# Define as listas de arquivos
arquivosA = [
    r"C:\Users\a925216\OneDrive - ATOS\Desktop\Agendamento\spam_automatizado\perfis\A\edward.py",
    r"C:\Users\a925216\OneDrive - ATOS\Desktop\Agendamento\spam_automatizado\perfis\A\eren.py",
    r"C:\Users\a925216\OneDrive - ATOS\Desktop\Agendamento\spam_automatizado\perfis\A\hinata.py",
    r"C:\Users\a925216\OneDrive - ATOS\Desktop\Agendamento\spam_automatizado\perfis\A\ichigo.py",
    r"C:\Users\a925216\OneDrive - ATOS\Desktop\Agendamento\spam_automatizado\perfis\A\isabel.py",
    r"C:\Users\a925216\OneDrive - ATOS\Desktop\Agendamento\spam_automatizado\perfis\A\misato.py",
    r"C:\Users\a925216\OneDrive - ATOS\Desktop\Agendamento\spam_automatizado\perfis\A\nami.py",
    r"C:\Users\a925216\OneDrive - ATOS\Desktop\Agendamento\spam_automatizado\perfis\A\tenten.py",
    r"C:\Users\a925216\OneDrive - ATOS\Desktop\Agendamento\spam_automatizado\perfis\A\tsunade.py"
]

arquivosB = [
    r"C:\Users\USUARIO\Desktop\Agendamento\spam_automatizado\perfis\B\18.py",
    r"C:\Users\USUARIO\Desktop\Agendamento\spam_automatizado\perfis\B\bulma.py",
    r"C:\Users\USUARIO\Desktop\Agendamento\spam_automatizado\perfis\B\goku.py",
    r"C:\Users\USUARIO\Desktop\Agendamento\spam_automatizado\perfis\B\lara.py",
    r"C:\Users\USUARIO\Desktop\Agendamento\spam_automatizado\perfis\B\luffy.py",
    r"C:\Users\USUARIO\Desktop\Agendamento\spam_automatizado\perfis\B\Naruto.py",
    r"C:\Users\USUARIO\Desktop\Agendamento\spam_automatizado\perfis\B\rias.py",
    r"C:\Users\USUARIO\Desktop\Agendamento\spam_automatizado\perfis\B\saitama.py",
    r"C:\Users\USUARIO\Desktop\Agendamento\spam_automatizado\perfis\B\suporte.py",
    r"C:\Users\USUARIO\Desktop\Agendamento\spam_automatizado\perfis\B\winry.py",
    r"C:\Users\USUARIO\Desktop\Agendamento\spam_automatizado\perfis\B\yoruichi.py",
    r"C:\Users\USUARIO\Desktop\Agendamento\spam_automatizado\perfis\B\yuno.py"
    r"C:\Users\USUARIO\Desktop\Agendamento\spam_automatizado\perfis\B\BA\edward.py"
    r"C:\Users\USUARIO\Desktop\Agendamento\spam_automatizado\perfis\B\BA\eren.py"
    r"C:\Users\USUARIO\Desktop\Agendamento\spam_automatizado\perfis\B\BA\hinata.py"
    r"C:\Users\USUARIO\Desktop\Agendamento\spam_automatizado\perfis\B\BA\ichigo.py"
    r"C:\Users\USUARIO\Desktop\Agendamento\spam_automatizado\perfis\B\BA\isabel.py"
    r"C:\Users\USUARIO\Desktop\Agendamento\spam_automatizado\perfis\B\BA\misato.py"
    r"C:\Users\USUARIO\Desktop\Agendamento\spam_automatizado\perfis\B\BA\nami.py"
    r"C:\Users\USUARIO\Desktop\Agendamento\spam_automatizado\perfis\B\BA\tenten.py"
    r"C:\Users\USUARIO\Desktop\Agendamento\spam_automatizado\perfis\B\BA\tsunade.py"    
]

arquivosC = [
    r"C:\Users\Isaque\Desktop\Agendamento\Agendamento\spam_automatizado\perfis\C\ada.py",
    r"C:\Users\Isaque\Desktop\Agendamento\Agendamento\spam_automatizado\perfis\C\docinho.py",
    r"C:\Users\Isaque\Desktop\Agendamento\Agendamento\spam_automatizado\perfis\C\itachi.py",
    r"C:\Users\Isaque\Desktop\Agendamento\Agendamento\spam_automatizado\perfis\C\jill.py",
    r"C:\Users\Isaque\Desktop\Agendamento\Agendamento\spam_automatizado\perfis\C\light.py",
    r"C:\Users\Isaque\Desktop\Agendamento\Agendamento\spam_automatizado\perfis\C\misa.py",
    r"C:\Users\Isaque\Desktop\Agendamento\Agendamento\spam_automatizado\perfis\C\mikasa.py",
    r"C:\Users\Isaque\Desktop\Agendamento\Agendamento\spam_automatizado\perfis\C\sailor.py",
    r"C:\Users\Isaque\Desktop\Agendamento\Agendamento\spam_automatizado\perfis\C\spike.py",
    r"C:\Users\Isaque\Desktop\Agendamento\Agendamento\spam_automatizado\perfis\C\temari.py",
    r"C:\Users\Isaque\Desktop\Agendamento\Agendamento\spam_automatizado\perfis\C\ana.py",
    r"C:\Users\Isaque\Desktop\Agendamento\Agendamento\spam_automatizado\perfis\C\marilyn.py",
    r"C:\Users\Isaque\Desktop\Agendamento\Agendamento\spam_automatizado\perfis\C\julia.py",
    r"C:\Users\Isaque\Desktop\Agendamento\Agendamento\spam_automatizado\perfis\C\jodie.py",
    r"C:\Users\Isaque\Desktop\Agendamento\Agendamento\spam_automatizado\perfis\C\jennifer.py",
    r"C:\Users\Isaque\Desktop\Agendamento\Agendamento\spam_automatizado\perfis\C\megan.py",
    r"C:\Users\Isaque\Desktop\Agendamento\Agendamento\spam_automatizado\perfis\C\margot.py",
    r"C:\Users\Isaque\Desktop\Agendamento\Agendamento\spam_automatizado\perfis\C\alexandra.py",
    r"C:\Users\Isaque\Desktop\Agendamento\Agendamento\spam_automatizado\perfis\C\nicole.py"
]

# Escolhe a lista de arquivos com base na escolha do usuário
if escolha == 'A':
    arquivos = arquivosA
elif escolha == 'B':
    arquivos = arquivosB
elif escolha == 'C':
    arquivos = arquivosC
else:
    print("Escolha inválida. Por favor, execute o script novamente e digite A, B ou C.")
    exit()

# Realiza o ALT + TAB
pyautogui.hotkey('alt', 'tab')
time.sleep(1)  # Pequena espera para garantir que a mudança de janela ocorra

# Espera 5 segundos para você mover o mouse para a posição desejada
print("Mova o mouse para a posição desejada na tela. Você tem 5 segundos.")
time.sleep(5)

# Obtém a posição atual do mouse
x, y = pyautogui.position()
print(f"xDia = {x}")
print(f"yDia = {y}")

# Atualiza todos os arquivos
for arquivo in arquivos:
    atualizar_variaveis_arquivo(arquivo, x, y)

print("Processo concluído.")

# Realiza o ALT + TAB novamente após a execução
pyautogui.hotkey('alt', 'tab')