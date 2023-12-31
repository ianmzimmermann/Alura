import random


def jogar():
    abertura()

    palavra_secreta = palavra()

    letras_acertadas = inicializando(palavra_secreta)

    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 6

    acertou = jogando(palavra_secreta, letras_acertadas,
                      enforcou, acertou, tentativas)

    print_final(acertou, palavra_secreta)


def abertura():
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


def inicializando(palavra):
    return ["_" for i in palavra]


def chute_correto(palavra_secreta, letras_acertadas, chute):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
            print("Acertou")
        index += 1


def jogando(palavra_secreta, letras_acertadas, enforcou, acertou, tentativas):
    while (not enforcou and not acertou):
        chute = input("Qual letra? ").lower().strip()

        if (chute in palavra_secreta):
            chute_correto(palavra_secreta, letras_acertadas, chute)
        else:
            tentativas -= 1
            print(f"{tentativas} Tentativas restantes\n")

        enforcou = tentativas == 0
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)
        print("\n")
    return acertou


def print_final(acertou, palavra_secreta):
    if (acertou):
        imprime_mensagem_vencedor()
    else:
        mensagem_perdedor(palavra_secreta)

    print("Fim de Jogo")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if (__name__ == "__main__"):
    jogar()
