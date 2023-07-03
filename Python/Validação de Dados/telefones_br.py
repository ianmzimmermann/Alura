import re


class telefones_br:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.nuemro = telefone
        else:
            raise ValueError("Numero incorreto")

    def valida_telefone(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, telefone)

        if resposta:
            return True
        else:
            return False
