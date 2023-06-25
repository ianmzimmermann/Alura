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

while (tentativas > 0):

    tentativas -= 1
    chute = int(input("Digite o seu numero:"))
    print("Você digitou", chute)

    if (numero_secreto == chute):
        print("Você acertou")
    elif (numero_secreto < chute):
        print("Você errou, seu chute foi acima")
        print(tentativas, "Tentativa(s) restante(s)", "\n")
    else:
        print("Você errou, seu chute foi abaixo")
        print(tentativas, "Tentativa(s) restante(s)", "\n")\

print("\n\nFim de Jogo\n\n")
