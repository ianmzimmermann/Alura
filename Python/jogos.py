import forca
import adivinhacao

print("*_Escolha seu jogo_*\n")
print("************************************\n")

print("(1) Forca  (2) Adivinhação")

jogo = int(input("Qual o Jogo?"))

if (jogo == 1):
    print("Jogo Forca")
    forca.jogo_forca()
elif (jogo == 2):
    print("Jogo Forca")
    adivinhacao.jogo_adivinhacao()
