import random

# 1. Configuração Inicial: Escolhe um número secreto de 1 a 100

numero_secreto = random.randint(1, 100)
tentativas =  0 
acertou = False 

print("--- Jogo de adivinhação ---")
print("Tente advinhar o número secreto entre 1 e 100!")

while not acertou:
    try:
        palpite = int(input("\n Seu palpite: "))
        tentativas += 1

    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros.")
        continue
    if palpite == numero_secreto:
        acertou = True
        print(f"\n PARÁBENS!  Você acertou o número {numero_secreto}!")
        print(f"Você precisou de {tentativas} tentativas.")
    
    elif palpite < numero_secreto:
        print("Dica: O número secreto é MAIOR.")

    else:
        print("Dica: O número secreto é MENOR.")
    
print("Fim do jogo.")