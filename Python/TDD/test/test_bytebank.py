from codigo.bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_13_03_2000_retornar_22(self):
        entrada = '13/03/2000'  # Given-Contexto
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)

        resultado = funcionario_teste.idade()  # When-ação

        assert resultado == esperado  # Then-desfecho

    def test_quand0_sobrenome_recebe_Ian_Zimmermann_retornar_Zimmermann(self):
        entrada = 'Ian Zimmermann'  # Given-Contexto
        esperado = 'Zimmermann'

        funcionario_teste = Funcionario(entrada, 25, 1111)

        resultado = funcionario_teste.sobrenome()  # When-ação

        assert resultado == esperado  # Then-desfecho