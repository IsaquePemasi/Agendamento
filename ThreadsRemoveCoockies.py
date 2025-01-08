import os

def remover_json(diretorio):
    # Verifica se o diretório existe
    if not os.path.exists(diretorio):
        print(f"O diretório {diretorio} não existe.")
        return

    # Itera sobre todos os arquivos no diretório
    for arquivo in os.listdir(diretorio):
        # Verifica se o arquivo tem extensão .json
        if arquivo.endswith('.json'):
            caminho_arquivo = os.path.join(diretorio, arquivo)
            os.remove(caminho_arquivo)  # Remove o arquivo
            print(f"Arquivo removido: {caminho_arquivo}")

# Exemplo de uso
diretorio = r'C:\posti'  # Usando uma string bruta para evitar problemas com caracteres de escape
remover_json(diretorio)