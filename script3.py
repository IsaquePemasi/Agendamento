import pyautogui
import time

# Aguardar 2 segundos antes de começar para dar tempo de colocar o foco na janela correta
time.sleep(2)

# Definir o horário inicial e final
start_hour = 1
start_minute = 0
end_hour = 23
end_minute = 30

# Função para formatar a hora como string
def format_time(hour, minute):
    return f"{hour:02}{minute:02}"

# Loop até atingir o horário final
while start_hour < end_hour or (start_hour == end_hour and start_minute <= end_minute):
    # Pressionar CTRL + V
    pyautogui.hotkey('ctrl', 'v')

    # Pressionar ENTER
    pyautogui.press('enter')

    # Pressionar BACKSPACE seis vezes
    for _ in range(5):
        pyautogui.press('backspace')

    # Digitar o horário atual
    pyautogui.write(format_time(start_hour, start_minute))

    # Pressionar ENTER
    pyautogui.press('enter')

    # Incrementar o horário em 30 minutos
    start_minute += 30
    if start_minute >= 60:
        start_minute -= 60
        start_hour += 1

    # Pequena pausa entre as iterações (opcional)
    time.sleep(1)