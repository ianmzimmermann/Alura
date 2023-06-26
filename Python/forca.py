def jogar():
    print("*_Bem vindo ao jogo de Forca_*\n")
    print("************************************\n")

    palavra_secreta = "python"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    index = 0
    # for i in palavra_secreta:
    #     letras_acertadas[index] = "_ "
    #     index += 1

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        chute = input("Qual letra? ").lower().strip()
        index = 0

        for letra in palavra_secreta:
            if (chute == letra):
                letras_acertadas[index] = letra
                print("Acertou")
            index += 1

        print(letras_acertadas)
        print("\n")

    print("\nFim de Jogo")


if (__name__ == "__main__"):
    jogar()
