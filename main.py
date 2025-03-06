import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import subprocess
import os
import pyautogui
from datetime import datetime, timedelta  # Mudança aqui

# Configurar o tkinter para alta DPI
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# Caminho base comum
base_path = r"C:\Users\a925216\OneDrive - ATOS\Desktop\Agendamento\spam_automatizado\perfis\A"
base_pathB = r"C:\Users\USUARIO\Desktop\Agendamento\spam_automatizado\perfis\B"
base_pathC = r"C:\Users\Isaque\Desktop\Agendamento\Agendamento\spam_automatizado\perfis\C"

# Dicionário para mapear personagens aos seus scripts
character_scripts = {
    "edward": os.path.join(base_path, "edward.py"),
    "eren": os.path.join(base_path, "eren.py"),
    "ichigo": os.path.join(base_path, "ichigo.py"),
    "isabel": os.path.join(base_path, "isabel.py"),
    "tenten": os.path.join(base_path, "tenten.py"),
    "hinata": os.path.join(base_path, "hinata.py"),
    "nami": os.path.join(base_path, "nami.py"),
    "misato": os.path.join(base_path, "misato.py"),
    "tsunade": os.path.join(base_path, "tsunade.py"),
    "suporte": os.path.join(base_pathB, "suporte.py"),
    "lara": os.path.join(base_pathB, "lara.py"),
    "naruto": os.path.join(base_pathB, "naruto.py"),
    "rias": os.path.join(base_pathB, "rias.py"),
    "bulma": os.path.join(base_pathB, "bulma.py"),
    "goku": os.path.join(base_pathB, "goku.py"),  
    "yuno": os.path.join(base_pathB, "yuno.py"),    
    "saitama": os.path.join(base_pathB, "saitama.py"),
    "luffy": os.path.join(base_pathB, "luffy.py"),
    "winry": os.path.join(base_pathB, "winry.py"),
    "yoruichi": os.path.join(base_pathB, "yoruichi.py"),
    "docinho": os.path.join(base_pathC, "docinho.py"),
    "sailor": os.path.join(base_pathC, "sailor.py"),
    "itachi": os.path.join(base_pathC, "itachi.py"),  
    "light": os.path.join(base_pathC, "light.py"),
    "spike": os.path.join(base_pathC, "spike.py"),
    "temari": os.path.join(base_pathC, "temari.py"), 
    "mikasa": os.path.join(base_pathC, "mikasa.py"),
    "jill": os.path.join(base_pathC, "jill.py"),
    "misa": os.path.join(base_pathC, "misa.py"),
    "ada": os.path.join(base_pathC, "ada.py"), 
}

# Função para obter o tamanho ideal da imagem com base na largura da tela
def get_image_size(screen_width):
    if screen_width < 1920:
        return 227, 227
    else:
        return 335, 335

# Função para executar o script Python
def run_script(character):
    script_path = character_scripts.get(character)
    
    # Simular Alt + Tab
    pyautogui.hotkey('alt', 'tab')
    
    if script_path and os.path.exists(script_path):
        start_time = datetime.now()
        try:
            subprocess.run(["python", script_path], check=True)
            end_time = datetime.now()
            duration = end_time - start_time
            duration_str = str(duration).split('.')[0]  # Remover milissegundos
            messagebox.showinfo("Sucesso", f"Script de {character} executado com sucesso!\n"
                                           f"Início: {start_time.strftime('%H:%M:%S')}\n"
                                           f"Término: {end_time.strftime('%H:%M:%S')}\n"
                                           f"Duração: {duration_str}")  # Mudança aqui
        except subprocess.CalledProcessError as e:
            end_time = datetime.now()
            duration = end_time - start_time
            duration_str = str(duration).split('.')[0]  # Remover milissegundos
            messagebox.showerror("Erro", f"Falha ao executar o script de {character}.\n"
                                         f"Início: {start_time.strftime('%H:%M:%S')}\n"
                                         f"Término: {end_time.strftime('%H:%M:%S')}\n"
                                         f"Duração: {duration_str}\n"  # Mudança aqui
                                         f"Erro: {e}")
    else:
        messagebox.showerror("Erro", f"Script de {character} não encontrado.")

# Função para criar botões com imagens e textos
def create_button(frame, character, row, col, image_size):
    image_path = os.path.join("images", f"{character}.png")
    print(f"Tentando carregar a imagem de: {image_path}")  # Adiciona depuração
    character_frame = tk.Frame(frame, padx=10, pady=10, bg='#f0f0f0')
    if os.path.exists(image_path):
        image = Image.open(image_path)
        image = image.resize(image_size, Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        button = tk.Button(character_frame, image=photo, command=lambda: run_script(character), bg='#f0f0f0', bd=0)
        button.image = photo  # Manter referência da imagem para evitar garbage collection
        button.pack(side=tk.TOP, pady=(0, 5))
    else:
        print(f"Imagem não encontrada para o personagem: {character}")  # Adiciona depuração
        button = tk.Button(character_frame, text=character, command=lambda: run_script(character), bg='#f0f0f0', bd=0)
        button.pack(side=tk.TOP, pady=(0, 5))

    label_text = tk.Label(character_frame, text=character, bg='#f0f0f0', font=('Arial', 12))
    label_text.pack(side=tk.TOP)
    character_frame.grid(row=row, column=col, padx=10, pady=10)

# Configurar a janela principal
root = tk.Tk()
root.title("TeleSpam")
root.configure(bg='#ffffff')

# Obter largura da tela
screen_width = root.winfo_screenwidth()

# Obter tamanho da imagem com base na largura da tela
image_size = get_image_size(screen_width)

# Adicionar ícone à janela principal
icon_path = os.path.join("images", "app_icon.ico")  # Caminho do ícone
root.iconbitmap(icon_path)

# Canvas e barra de rolagem
canvas = tk.Canvas(root, borderwidth=0, bg='#ffffff')
scroll_y = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)

# Frame que conterá todos os widgets
frame = tk.Frame(canvas, bg='#ffffff')

# Configurar o canvas e a barra de rolagem
frame_id = canvas.create_window((0, 0), window=frame, anchor='nw')
canvas.configure(yscrollcommand=scroll_y.set)

# Atualizar o tamanho do canvas para caber os widgets
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", on_frame_configure)

# Função para rolar com o mouse
def on_mouse_wheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

# Bind do evento do mouse wheel ao canvas
canvas.bind_all("<MouseWheel>", on_mouse_wheel)

canvas.pack(side="left", fill="both", expand=True)
scroll_y.pack(side="right", fill="y")

# Criar botões para cada personagem
row = 0
col = 0
for i, character in enumerate(character_scripts.keys()):
    create_button(frame, character, row, col, image_size)
    col += 1
    if col >= 5:  # Ajustado para fazer 5 colunas em vez de 7, para acomodar o tamanho maior dos botões
        col = 0
        row += 1

# Ajustar o canvas para redimensionar corretamente
def on_canvas_configure(event):
    canvas.itemconfig(frame_id, width=canvas.winfo_width())

canvas.bind('<Configure>', on_canvas_configure)

# Iniciar o loop principal do tkinter
root.mainloop()