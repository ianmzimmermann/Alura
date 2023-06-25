print("┏━━━┓\t┏━━━┓\t┏━━━┓\t┏━━━┓\t┏━━━┓")
print("┃┏━┓┃\t┃┏━┓┃\t┃┏━┓┃\t┃┏━┓┃\t┃┏━┓┃")
print("┗┛┏┛┃\t┗┛┏┛┃\t┗┛┏┛┃\t┗┛┏┛┃\t┗┛┏┛┃")
print("╋╋┃┏┛\t╋╋┃┏┛\t╋╋┃┏┛\t╋╋┃┏┛\t╋╋┃┏┛")
print("╋╋┏┓\t╋╋┏┓\t╋╋┏┓\t╋╋┏┓\t╋╋┏┓")
print("╋╋┗┛\t╋╋┗┛\t╋╋┗┛\t╋╋┗┛\t╋╋┗┛\n")

print("*_Bem vindo ao jogo de Adivinhação_*\n")
print("************************************\n")

numero_secreto = 67
tentativas = 3

print("Dica, o número está entre {} e {}".format(
    numero_secreto - 15, numero_secreto + 15))

for i in range(1, tentativas + 1):

    if (tentativas == 1):
        print("Dica, o número está entre {} e {}".format(
            numero_secreto - 3, numero_secreto + 3))

    tentativas -= 1

    chute = int(input("Digite o seu numero:"))
    print("Você digitou", chute)

    if (numero_secreto == chute):
        print("\nVocê acertou\n")
        break
    elif (numero_secreto < chute):
        print("Você errou, seu chute foi acima")
        print(f"\n{tentativas} Tentativa(s) restante(s)\n")
    else:
        print("Você errou, seu chute foi abaixo")
        print(f"\n{tentativas} Tentativa(s) restante(s)\n")

print("\nFim de Jogo\n")
