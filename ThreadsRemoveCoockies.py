import os
import json
import random
from datetime import datetime
import threading
from playwright.sync_api import sync_playwright

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

# Função para gerar um delay aleatório
def random_delay(min_seconds, max_seconds):
    return random.uniform(min_seconds, max_seconds) * 1000  # Converte para milissegundos

# Função para salvar os cookies
def save_cookies(page, account):
    cookies = page.context.cookies()
    cookies_file = os.path.join("C:", "posti", f"{account}__cookies.json")
    with open(cookies_file, 'w', encoding='utf-8') as f:
        json.dump(cookies, f)
    print(f"Cookies salvos para {account}")

# Função para carregar os cookies
def load_cookies(page, account):
    cookies_file = os.path.join("C:", "posti", f"{account}__cookies.json")
    if os.path.exists(cookies_file):
        with open(cookies_file, 'r', encoding='utf-8') as f:
            cookies = json.load(f)
            page.context.clear_cookies()  # Limpa cookies existentes
            page.context.add_cookies(cookies)
        print(f"Cookies carregados para {account}")
        page.goto('https://www.threads.net')  # A URL de destino
        page.wait_for_selector('div[role="button"]:has-text("Criar")')  # Aguarde o carregamento
    else:
        print(f"Cookies não encontrados para {account}, realizando login...")

def threads_post(account, pwd, base_delay, display=False):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not display)
        context = browser.new_context()
        page = context.new_page()

        try:
            # Tenta carregar os cookies antes de logar
            load_cookies(page, account)

            # Se os cookies não forem carregados, realiza o login
            cookies_file = os.path.join("C:", "posti", f"{account}__cookies.json")
            if not os.path.exists(cookies_file):
                page.goto('https://www.threads.net/login/?show_choice_screen=false')
                page.wait_for_timeout(random_delay(base_delay * 0.5, base_delay * 1.5))  # Delay aleatório

                # Digita o nome de usuário
                page.fill('input[autocomplete="username"]', account)
                page.wait_for_timeout(random_delay(base_delay * 0.5, base_delay * 1.5))  # Delay aleatório

                # Digita a senha
                page.fill('input[autocomplete="current-password"]', pwd)
                page.wait_for_timeout(random_delay(base_delay * 0.5, base_delay * 1.5))  # Delay aleatório

                # Clica no botão de login
                page.click('div[role="button"]:has-text("Entrar")')
                page.wait_for_timeout(random_delay(base_delay * 1, base_delay * 2))  # Delay aleatório

                # Salva os cookies após o login
                save_cookies(page, account)

            # Verifica se o login foi bem-sucedido
            try:
                page.wait_for_selector('div[role="button"]:has-text("Criar")', timeout=10000)
                print(f"Login bem-sucedido para {account}")
            except:
                print(f"Falha no login para {account}")
                return

            # Diretórios de textos e mídias
            text_directory = os.path.join("C:", "posti", "legendas")
            media_directory = os.path.join("C:", "posti", "midias")

            if not os.path.exists(text_directory) or not os.path.exists(media_directory):
                print(f"Diretórios de texto ou mídia não encontrados para {account}.")
                return

            text_files = [f for f in os.listdir(text_directory) if f.endswith('.txt')]
            media_files = [f for f in os.listdir(media_directory) if f.endswith(('.jpeg', '.jpg', '.png'))]
            combinations = [(txt, img) for txt in text_files for img in media_files]

            if len(combinations) < 60:
                print(f"Número insuficiente de combinações para {account}. Necessário: 60, Disponível: {len(combinations)}")
                return

            used_combinations = set()
            post_count = 0

            def get_next_combination():
                nonlocal used_combinations
                if len(used_combinations) == len(combinations):
                    used_combinations = set()
                available_combinations = [c for c in combinations if c not in used_combinations]
                next_combination = random.choice(available_combinations)
                used_combinations.add(next_combination)
                return next_combination

            while post_count < 60:
                try:
                    # Clica no botão de "Criar"
                    page.click('div[role="button"]:has-text("Criar")')
                    page.wait_for_timeout(random_delay(base_delay * 0.5, base_delay * 1.5))  # Delay aleatório

                    # Obtém a próxima combinação
                    selected_text_file, selected_media_file = get_next_combination()

                    # Lê o conteúdo do arquivo de texto
                    with open(os.path.join(text_directory, selected_text_file), 'r', encoding='utf-8') as file:
                        post = file.read()

                    # Preenche o campo de texto
                    page.fill('p.xdj266r.x11i5rnm.xat24cr.x1mh8g0r', post)
                    page.wait_for_timeout(random_delay(base_delay * 0.5, base_delay * 1.5))  # Delay aleatório

                    # Anexa a mídia
                    media_path = os.path.join(media_directory, selected_media_file)
                    file_input = page.locator('input[type="file"]')
                    file_input.set_input_files(media_path)
                    page.wait_for_timeout(random_delay(base_delay * 1, base_delay * 2))  # Delay aleatório

                    # Publica a postagem
                    page.keyboard.press('Control+Enter')
                    page.wait_for_timeout(random_delay(base_delay * 1, base_delay * 2))  # Delay aleatório

                    # Incrementa o contador e registra no log
                    post_count += 1
                    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    log_entry = f"{now} - Post {post_count}: {selected_text_file} + {selected_media_file} (Account: {account}) - Status: Sucesso\n"

                    with open("post_logs.txt", "a", encoding="utf-8") as log_file:
                        log_file.write(log_entry)

                    print(log_entry.strip())

                    # Aguarda um intervalo aleatório antes da próxima postagem
                    interval = random_delay(50, 70)  # Entre 50 e 70 segundos
                    page.wait_for_timeout(interval)

                except Exception as e:
                    print(f"Erro durante a postagem: {e}")
                    continue

            print(f"Postagens concluídas para {account}. Total: {post_count}")

        finally:
            browser.close()

# Função para iniciar uma instância de navegador por thread
def start_thread(account, pwd, base_delay, display):
    # Remove arquivos JSON antes de iniciar as postagens
    remover_json(os.path.join("C:", "posti"))
    threads_post(account, pwd, base_delay, display)

# Contas para login (com placeholders e delays personalizados)
accounts = [
    {"account": "larisinha_vieira", "pwd": "80471360011", "base_delay": 1.0}, 
    {"account": "belzinha_marques", "pwd": "80471360011", "base_delay": 1.0},
    {"account": "julinha_tezzei", "pwd": "80471360011", "base_delay": 1.0}, 
    {"account": "rafaela_haeitmann", "pwd": "80471360011", "base_delay": 1.0}, 
]

# Criar e iniciar threads
threads = []
for acc in accounts:
    thread = threading.Thread(target=start_thread, args=(acc["account"], acc["pwd"], acc["base_delay"], True))
    threads.append(thread)
    thread.start()

# Aguardar todas as threads concluírem
for thread in threads:
    thread.join()

print("Instâncias concluídas.")