import random

print("*********************************")
print("Bem-vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 3

for rodada in range(1,total_de_tentativas+1):
    print("Tentativas: {} de {} ".format(rodada, total_de_tentativas))
    chute = int(input("Digite um número entre 0 e 100: "))
    print("Você digitou", chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    elif (maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    else:
        print("Você errou! O seu chute foi menor que o número secreto.")

print('Fim do jogo :( O número secreto era o ', numero_secreto)
