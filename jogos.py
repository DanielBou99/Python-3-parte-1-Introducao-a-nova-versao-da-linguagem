import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("Escolha o seu jogo!")
    print("*********************************")

    print("(1) forca (2) Adivinhação")

    jogo = int(input(">> "))

    if (jogo == 1):
        forca.jogar()
    else:
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()