def jogar():
    print("*_Bem vindo ao jogo de Forca_*\n")
    print("************************************\n")

    palavra_secreta = "python"
    letras_acertadas = []

    for i in palavra_secreta:
        letras_acertadas.append("_")

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


if (__name__ == "__main__"):
    jogar()
