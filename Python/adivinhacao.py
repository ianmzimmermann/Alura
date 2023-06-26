import random


def jogar():

    print("┏━━━┓\t┏━━━┓\t┏━━━┓\t┏━━━┓\t┏━━━┓")
    print("┃┏━┓┃\t┃┏━┓┃\t┃┏━┓┃\t┃┏━┓┃\t┃┏━┓┃")
    print("┗┛┏┛┃\t┗┛┏┛┃\t┗┛┏┛┃\t┗┛┏┛┃\t┗┛┏┛┃")
    print("╋╋┃┏┛\t╋╋┃┏┛\t╋╋┃┏┛\t╋╋┃┏┛\t╋╋┃┏┛")
    print("╋╋┏┓\t╋╋┏┓\t╋╋┏┓\t╋╋┏┓\t╋╋┏┓")
    print("╋╋┗┛\t╋╋┗┛\t╋╋┗┛\t╋╋┗┛\t╋╋┗┛\n")

    print("*_Bem vindo ao jogo de Adivinhação_*\n")
    print("************************************\n")

    print("Selecione o nível de dificuldade")
    print("3 Fácil \n2 Médio \n1 Difícil")

    tentativas = 3 * int(input("Digite o nível:"))

    pontos = 1000

    numero_secreto = random.randrange(1, 101)

    print("Dica, o número está entre {} e {}".format(
        numero_secreto - random.randrange(1, 30), numero_secreto + random.randrange(1, 30)))

    for i in range(1, tentativas + 1):

        if (tentativas == 1):
            print("Dica, o número está entre {} e {}".format(
                numero_secreto - random.randrange(1, 3), numero_secreto + random.randrange(1, 3)))

        tentativas -= 1

        chute = int(input("Digite o seu numero:"))
        print("Você digitou", chute)

        if (numero_secreto == chute):
            print("\n+ + + Você acertou + + +")
            break
        elif (numero_secreto < chute):
            print("- - -  Você errou, seu chute foi acima - - - ")
            print(f"\n{tentativas} Tentativa(s) restante(s)\n")
            pontos = abs(pontos - numero_secreto)
        else:
            print("- - - Você errou, seu chute foi abaixo - - - ")
            print(f"\n{tentativas} Tentativa(s) restante(s)\n")
            pontos = abs(pontos - numero_secreto)

    print("\nFim de Jogo")
    print(f"Total de pontos {pontos}\n")
    print(f"O número secreto era {numero_secreto}")
