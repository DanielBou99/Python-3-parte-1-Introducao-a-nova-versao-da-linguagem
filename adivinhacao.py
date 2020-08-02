import random

print("*********************************")
print("Bem-vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
pontos = 1000

print("""Qual nível de dificuldade?
(1) Fácil 
(2) Médio
(3) Difícil
""")

nivel = int(input(">> "))

if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1,total_de_tentativas+1):
    print("Tentativas: {} de {} ".format(rodada, total_de_tentativas))
    chute = int(input("Digite um número entre 0 e 100: "))
    print("Você digitou", chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto

    if (acertou):
        print("Você acertou!")
        print("Total de pontos: ", pontos)
        break
    else:
        pontos_perdidos = numero_secreto - chute
        pontos -= abs(pontos_perdidos)
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        else:
            print("Você errou! O seu chute foi menor que o número secreto.")

print('Fim do jogo. O número secreto era o ', numero_secreto)
