import time
import schedule
from telethon import TelegramClient
#pip install telethon schedule
# Substitua pelos seus próprios valores
api_id = '26644897' # YOUR_API_ID
api_hash = '32468ba28dd454c3b21ff003f4fa2262' #'YOUR_API_HASH'
phone_number =  '+5511912363604'#'YOUR_PHONE_NUMBER'
group_username = '-2045671705' #
message = 'testando'

# Crie o cliente do Telegram
client = TelegramClient('session_name', api_id, api_hash)

async def send_message():
    async with client:
        await client.send_message(group_username, message)
        print(f"Mensagem enviada para {group_username} às {time.strftime('%Y-%m-%d %H:%M:%S')}")

def schedule_message(hour, minute):
    schedule_time = f"{hour:02d}:{minute:02d}"
    schedule.every().day.at(schedule_time).do(lambda: client.loop.run_until_complete(send_message()))
    print(f"Mensagem agendada para {schedule_time}")

if __name__ == "__main__":
    # Conecte ao cliente do Telegram
    client.start(phone=phone_number)

    # Defina o horário e minutos para agendar a mensagem
    hour = 23  # Exemplo: 14 horas
    minute = 50  # Exemplo: 30 minutos

    # Agende a mensagem
    schedule_message(hour, minute)

    # Mantenha o script rodando
    while True:
        schedule.run_pending()
        time.sleep(1)