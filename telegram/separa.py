import os
import shutil

def dividir_arquivos_em_pastas(origem, destino_base):
    # Criar subpastas
    subpastas = [os.path.join(destino_base, f'pasta_{i+1}') for i in range(4)]
    for subpasta in subpastas:
        os.makedirs(subpasta, exist_ok=True)
    
    # Listar todos os arquivos na pasta de origem
    arquivos = [f for f in os.listdir(origem) if os.path.isfile(os.path.join(origem, f))]
    
    # Dividir os arquivos em quatro partes aproximadamente iguais
    total_arquivos = len(arquivos)
    tamanho_parte = total_arquivos // 4
    
    # Distribuir os arquivos nas subpastas
    for i, arquivo in enumerate(arquivos):
        subpasta_index = i // tamanho_parte
        if subpasta_index >= 4:
            subpasta_index = 3
        shutil.move(os.path.join(origem, arquivo), os.path.join(subpastas[subpasta_index], arquivo))

# Exemplo de uso
origem = r"C:\Users\a925216\OneDrive - ATOS\Desktop\TransVIP2\photos\pasta_1"
destino_base = r"C:\Users\a925216\OneDrive - ATOS\Desktop\TransVIP2\photos\pasta_1"
dividir_arquivos_em_pastas(origem, destino_base)