import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import os
import pyautogui

# Caminho base comum
base_path = r"C:\Users\a925216\OneDrive - ATOS\Desktop\Agendamento\spam_automatizado\perfis\A"
base_pathB = r"C:\Users\USUARIO\Desktop\Agendamento\spam_automatizado\perfis\B"
base_pathC = r"C:\Users\Isaque\Desktop\Agendamento\Agendamento\spam_automatizado\perfis\C"

# Dicionário para mapear personagens aos seus scripts
character_scripts = {
    "edward": os.path.join(base_path, "edward.py"),
    "eren": os.path.join(base_path, "eren.py"),
    "hinata": os.path.join(base_path, "hinata.py"),
    "ichigo": os.path.join(base_path, "ichigo.py"),
    "isabel": os.path.join(base_path, "isabel.py"),
    "misato": os.path.join(base_path, "misato.py"),
    "nami": os.path.join(base_path, "nami.py"),
    "tenten": os.path.join(base_path, "tenten.py"),
    "tsunade": os.path.join(base_path, "tsunade.py"),
    "bulma": os.path.join(base_pathB, "bulma.py"),
    "goku": os.path.join(base_pathB, "goku.py"),        
    "lara": os.path.join(base_pathB, "lara.py"),
    "luffy": os.path.join(base_pathB, "luffy.py"),
    "naruto": os.path.join(base_pathB, "naruto.py"),
    "rias": os.path.join(base_pathB, "rias.py"),
    "saitama": os.path.join(base_pathB, "saitama.py"),
    "suporte": os.path.join(base_pathB, "suporte.py"),
    "winry": os.path.join(base_pathB, "winry.py"),
    "yoruichi": os.path.join(base_pathB, "yoruichi.py"),
    "yuno": os.path.join(base_pathB, "yuno.py"),
    "ada": os.path.join(base_pathC, "ada.py"), 
    "docinho": os.path.join(base_pathC, "docinho.py"),
    "itachi": os.path.join(base_pathC, "itachi.py"),        
    "jill": os.path.join(base_pathC, "jill.py"),
    "light": os.path.join(base_pathC, "light.py"),
    "mikasa": os.path.join(base_pathC, "mikasa.py"),
    "misa": os.path.join(base_pathC, "misa.py"),
    "sailor": os.path.join(base_pathC, "sailor.py"),
    "spike": os.path.join(base_pathC, "spike.py"),
    "temari": os.path.join(base_pathC, "temari.py"), 
}

# Função para executar o script Python
def run_script(character):
    script_path = character_scripts.get(character)
    
    # Simular Alt + Tab
    pyautogui.hotkey('alt', 'tab')
    
    if script_path and os.path.exists(script_path):
        try:
            subprocess.run(["python", script_path], check=True)
            messagebox.showinfo("Success", f"Executed {character}'s script successfully!")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to execute {character}'s script.\nError: {e}")
    else:
        messagebox.showerror("Error", f"Script for {character} not found.")

# Função para criar botões com imagens e textos
def create_button(frame, character, row, col):
    image_path = os.path.join("images", f"{character}.png")
    print(f"Trying to load image from: {image_path}")  # Adiciona depuração
    character_frame = tk.Frame(frame)
    if os.path.exists(image_path):
        image = Image.open(image_path)
        image = image.resize((100, 100), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        button = tk.Button(character_frame, image=photo, command=lambda: run_script(character))
        button.image = photo  # Manter referência da imagem para evitar garbage collection
        button.pack(side=tk.TOP)
    else:
        print(f"Image not found for character: {character}")  # Adiciona depuração
        button = tk.Button(character_frame, text=character, command=lambda: run_script(character))
        button.pack(side=tk.TOP)

    label_text = tk.Label(character_frame, text=character)
    label_text.pack(side=tk.TOP)
    character_frame.grid(row=row, column=col, padx=10, pady=10)

# Configurar a janela principal
root = tk.Tk()
root.title("Character Scripts Executor")

# Canvas e barra de rolagem
canvas = tk.Canvas(root, borderwidth=0)
scroll_y = tk.Scrollbar(root, orient="vertical", command=canvas.yview)

# Frame que conterá todos os widgets
frame = tk.Frame(canvas)

# Configurar o canvas e a barra de rolagem
frame_id = canvas.create_window((0, 0), window=frame, anchor='nw')
canvas.configure(yscrollcommand=scroll_y.set)

# Atualizar o tamanho do canvas para caber os widgets
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", on_frame_configure)

canvas.pack(side="left", fill="both", expand=True)
scroll_y.pack(side="right", fill="y")

# Criar botões para cada personagem
row = 0
col = 0
for i, character in enumerate(character_scripts.keys()):
    create_button(frame, character, row, col)
    col += 1
    if col >= 7:
        col = 0
        row += 1

# Ajustar o canvas para redimensionar corretamente
def on_canvas_configure(event):
    canvas.itemconfig(frame_id, width=canvas.winfo_width())

canvas.bind('<Configure>', on_canvas_configure)

# Iniciar o loop principal do tkinter
root.mainloop()