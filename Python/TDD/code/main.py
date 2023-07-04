from bytebank import Funcionario

# ian = Funcionario('Ian', '19/03/1998', 6000)
# print(ian.idade())


def teste_idade():
    funcionario_teste = Funcionario('Ian', '19/03/1998', 6000)
    print(f'Teste = {funcionario_teste.idade()}')


teste_idade()
