from codigo.bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_13_03_2000_retornar_22(self):
        entrada = '13/03/2000'  # Given-Contexto
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)

        resultado = funcionario_teste.idade()  # When-ação

        assert resultado == esperado  # Then-desfecho

    def test_quando_sobrenome_recebe_Ian_Zimmermann_retornar_Zimmermann(self):
        entrada = 'Ian Zimmermann'  # Given-Contexto
        esperado = 'Zimmermann'

        funcionario_teste = Funcionario(entrada, 25, 1111)

        resultado = funcionario_teste.sobrenome()  # When-ação

        assert resultado == esperado  # Then-desfecho

    def test_quando_decrescimo_salario_recebe_100000_retornar_90000(self):
        entrada_salario = 100000  # Given-Contexto
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)

        funcionario_teste.decrescimo_salario()  # When-ação
        resultado = funcionario_teste.salario

        assert resultado == esperado  # Then-desfecho

    def test_quando_calcular_bonus_recebe_1000_retornar_100(self):
        entrada_salario = 1000  # Given-Contexto
        esperado = 100

        funcionario_teste = Funcionario('Teste', '11/11/2000', entrada_salario)

        resultado = funcionario_teste.calcular_bonus()  # When-ação

        assert resultado == esperado  # Then-desfecho
