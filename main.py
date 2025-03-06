import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import os

# Caminho base comum
base_path = r"C:\Users\a925216\OneDrive - ATOS\Desktop\Agendamento\spam_automatizado\perfis\A"

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
}

# Função para executar o script Python
def run_script(character):
    script_path = character_scripts.get(character)
    if script_path and os.path.exists(script_path):
        try:
            subprocess.run(["python", script_path], check=True)
            messagebox.showinfo("Success", f"Executed {character}'s script successfully!")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to execute {character}'s script.\nError: {e}")
    else:
        messagebox.showerror("Error", f"Script for {character} not found.")

# Função para criar botões com imagens
def create_button(frame, character):
    image_path = os.path.join("images", f"{character}.png")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        image = image.resize((100, 100), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        button = tk.Button(frame, image=photo, command=lambda: run_script(character))
        button.image = photo  # Manter referência da imagem para evitar garbage collection
        button.pack(side=tk.LEFT, padx=10, pady=10)
    else:
        button = tk.Button(frame, text=character, command=lambda: run_script(character))
        button.pack(side=tk.LEFT, padx=10, pady=10)

# Configurar a janela principal
root = tk.Tk()
root.title("Character Scripts Executor")

# Frame para conter os botões
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Criar botões para cada personagem
for character in character_scripts.keys():
    create_button(frame, character)

# Iniciar o loop principal do tkinter
root.mainloop()