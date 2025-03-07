from telethon import TelegramClient
import asyncio
import time
from tqdm import tqdm  # Biblioteca para a barra de progresso
from colorama import init, Fore, Back, Style  # Adicionei "Back" para fundo colorido

# Inicializa o Colorama
init(autoreset=True)

# Suas credenciais do Telegram
api_id = 1234  # Substitua pelo seu API ID
api_hash = '1234'  # Substitua pelo seu API Hash
phone_number = '+551199999'  # Substitua pelo seu número de telefone

# Cria o cliente do Telethon
client = TelegramClient('session_name', api_id, api_hash)

# Assinatura personalizada com destaque
signature = f"{Back.BLUE}{Fore.WHITE}Feito por @collorcollor{Style.RESET_ALL}"

async def get_chat_id(chat_identifier):
    """Obtém o ID do chat a partir de um ID, link ou @username."""
    try:
        chat = await client.get_entity(chat_identifier)
        return chat.id
    except Exception as e:
        print(f"Erro ao obter o chat: {e}")
        return None

async def countdown_timer(seconds):
    """Cronômetro colorido com contagem regressiva."""
    for i in tqdm(range(seconds), desc="Aguardando", bar_format="{l_bar}{bar} {remaining}s", ncols=80):
        await asyncio.sleep(1)

async def main():
    await client.start(phone_number)
    print("Conectado com sucesso!")

    # Exibe a assinatura no terminal com destaque
    print(signature)

    # Solicita IDs dos grupos de origem e destino
    group_origin_identifier = input("Digite o ID, link ou @ do grupo de origem: ")
    group_destination_identifier = input("Digite o ID, link ou @ do grupo de destino: ")

    # Obtém os IDs dos grupos
    group_origin_id = await get_chat_id(group_origin_identifier)
    group_destination_id = await get_chat_id(group_destination_identifier)

    if group_origin_id is None or group_destination_id is None:
        print("Não foi possível obter os IDs dos grupos. Verifique suas entradas.")
        return

    print("Carregando informações do grupo (mídias)...")

    # Contando o número total de mídias no grupo de origem
    total_media_count = 0
    async for message in client.iter_messages(group_origin_id):
        if message.photo or message.video:
            total_media_count += 1

    print(f"O grupo de origem contém {total_media_count} mídias.")

    # Pergunta ao usuário quantas mídias deseja enviar
    while True:
        max_media_to_send = int(input(f"Quantas mídias você deseja enviar (máximo {total_media_count})? "))
        if 0 < max_media_to_send <= total_media_count:
            break
        else:
            print(f"Por favor, escolha um número entre 1 e {total_media_count}.")

    # Pergunta se o usuário deseja editar as legendas
    edit_captions = input("Quer editar as legendas? (S/N): ").strip().upper()
    new_caption = input("Digite a legenda que deseja adicionar aos vídeos e fotos: ") if edit_captions == 'S' else None

    print("Estamos carregando as mídias...")
    total_media_sent = 0
    start_time = time.time()

    async for message in client.iter_messages(group_origin_id):
        if total_media_sent >= max_media_to_send:
            break

        if message.video or message.photo:
            # Define a legenda final com base na escolha do usuário
            caption_to_use = new_caption if new_caption else (message.message or "")

            await client.send_file(group_destination_id, message.media, caption=caption_to_use)
            total_media_sent += 1

        progress = (total_media_sent / max_media_to_send) * 100
        elapsed_time = time.time() - start_time
        print(f"Progresso: {progress:.2f}% - {total_media_sent} mídias enviadas. Tempo decorrido: {int(elapsed_time // 60)}m {int(elapsed_time % 60)}s.")

        if total_media_sent % 100 == 0 and total_media_sent != 0:
            print(f"Enviadas {total_media_sent} mídias. Aguardando 15 segundos pra evitar ban...")
            await countdown_timer(15)

    print(f"Envio completo! Enviadas {total_media_sent} mídias.")
    elapsed_time = time.time() - start_time
    print(f"Tempo total de envio: {int(elapsed_time // 60)}m {int(elapsed_time % 60)}s.")

# Inicia o cliente do Telethon
with client:
    client.loop.run_until_complete(main())