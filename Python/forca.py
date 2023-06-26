def jogar():
    print("*_Bem vindo ao jogo de Forca_*\n")
    print("************************************\n")

    palavra_secreta = "python"

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        chute = input("Qual letra? ").lower().strip()
        index = 0

        for letra in palavra_secreta:
            if (chute == letra):
                print(letra, end=' ')
            else:
                print("_", end=' ')
            index += 1

        print("\n")

    print("\nFim de Jogo")


if (__name__ == "__main__"):
    jogar()
