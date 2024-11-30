# pip install telethon
import asyncio
from telethon import TelegramClient, events
from datetime import datetime, timedelta

# Substitua pelos seus valores
api_id = '29321295'
api_hash = 'bbc2110227aefbf6f0c30d6691366f78'
phone_number = '+5511912363604'
group_chat_id = '-2045671705'  # Substitua pelo chat_id do grupo

# Cria o cliente do Telegram
client = TelegramClient('session_name', api_id, api_hash)

# Função para enviar a mensagem
async def send_message(chat_id, message):
    await client.send_message(chat_id, message)

# Função para agendar a mensagem
async def schedule_message(chat_id, message, year, month, day, hour, minute):
    schedule_time = datetime(year, month, day, hour, minute)
    delay = (schedule_time - datetime.now()).total_seconds()
    await asyncio.sleep(delay)
    await send_message(chat_id, message)

# Função para processar comandos
@client.on(events.NewMessage(pattern='/agendar'))
async def handler(event):
    try:
        # Argumentos: mensagem, ano, mês, dia, hora, minuto
        args = event.message.text.split(' ', 6)
        message = args[1]
        year = int(args[2])
        month = int(args[3])
        day = int(args[4])
        hour = int(args[5])
        minute = int(args[6])

        chat_id = group_chat_id  # Use o chat_id do grupo
        asyncio.create_task(schedule_message(chat_id, message, year, month, day, hour, minute))
        await event.reply(f'Mensagem agendada para {year}-{month}-{day} {hour}:{minute}')
    except (IndexError, ValueError):
        await event.reply('Uso correto: /agendar <mensagem> <ano> <mês> <dia> <hora> <minuto>')

# Inicia o cliente
client.start(phone_number)
client.run_until_disconnected()