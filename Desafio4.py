import time

def descobrir_interruptores():

    print("Ligando o primeiro interruptor...")
    time.sleep(2)
    print("Desligando o primeiro interruptor e ligando o segundo interruptor...")

    time.sleep(2) 
    print("Entre na sala das lâmpadas e observe:")
    # Simulando as observações
    observacao = input("Está acesa a primeira, segunda ou terceira lâmpada? (1/2/3): ")
    if observacao == "1":
        print("O primeiro interruptor controla a primeira lâmpada.")
        print("O segundo interruptor controla a segunda lâmpada.")
        print("O terceiro interruptor controla a terceira lâmpada.")
    elif observacao == "2":
        print("O primeiro interruptor controla a segunda lâmpada.")
        print("O segundo interruptor controla a terceira lâmpada.")
        print("O terceiro interruptor controla a primeira lâmpada.")
    elif observacao == "3":
        print("O primeiro interruptor controla a terceira lâmpada.")
        print("O segundo interruptor controla a primeira lâmpada.")
        print("O terceiro interruptor controla a segunda lâmpada.")
    else:
        print("Entrada inválida. Por favor, responda apenas com 1, 2 ou 3.")

descobrir_interruptores()
