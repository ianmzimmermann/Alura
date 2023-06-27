import random


def inicializando(palavra):

    return ["_" for i in palavra]


def jogar():

    init()

    palavra_secreta = palavra()

    letras_acertadas = inicializando(palavra_secreta)

    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 6

    while (not enforcou and not acertou):
        chute = input("Qual letra? ").lower().strip()
        index = 0

        if (chute in palavra_secreta):
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                    print("Acertou")
                index += 1
        else:
            tentativas -= 1
            print(f"{tentativas} Tentativas restantes\n")

        enforcou = tentativas == 0
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)
        print("\n")

    if (acertou):
        print("Parabéns, você descobriu\n")
    else:
        print("Você perdeu, que tal tentar outra vez?\n")

    print("Fim de Jogo")


def init():

    print("************************************\n", end="")
    print("****_Bem vindo ao jogo de Forca_****\n", end="")
    print("************************************\n")


def palavra():

    palavras = []

    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    palavra_secreta = palavras[random.randrange(0, len(palavras))]

    return palavra_secreta


if (__name__ == "__main__"):

    jogar()
