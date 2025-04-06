import pyautogui
import time

def main():
    try:
        # Pergunta quantas vezes o usuário quer clicar
        num_clicks = int(input("Quantas vezes você quer que o botão esquerdo do mouse clique? "))
        
        # Espera 3 segundos
        print("Esperando 3 segundos...")
        time.sleep(3)
        
        # Realiza os cliques
        print(f"Clicando {num_clicks} vezes...")
        for _ in range(num_clicks):
            pyautogui.click()
            time.sleep(0.1)  # Pequena pausa entre os cliques para evitar sobrecarregar o sistema

        print("Terminado!")
    except ValueError:
        print("Por favor, insira um número válido.")
    except KeyboardInterrupt:
        print("\nOperação interrompida pelo usuário.")

if __name__ == "__main__":
    main()