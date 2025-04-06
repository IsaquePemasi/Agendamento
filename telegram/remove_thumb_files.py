import os

def remove_thumb_files(directory):
    try:
        # Verifica se o diretório existe
        if not os.path.exists(directory):
            print(f"O diretório {directory} não existe.")
            return

        # Lista todos os arquivos no diretório
        files = os.listdir(directory)

        # Itera sobre os arquivos
        for file in files:
            # Separa o nome do arquivo e a extensão
            filename, file_extension = os.path.splitext(file)
            # Verifica se o nome do arquivo termina com "thumb"
            if filename.endswith("thumb"):
                file_path = os.path.join(directory, file)
                # Remove o arquivo
                os.remove(file_path)
                print(f"Arquivo removido: {file_path}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Substitua 'seu_diretorio' pelo caminho do diretório onde deseja remover os arquivos
seu_diretorio = 'seu_diretorio'
remove_thumb_files(seu_diretorio)