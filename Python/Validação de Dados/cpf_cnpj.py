from validate_docbr import CPF, CNPJ


class Documento:
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return doc_cpf(documento)
        elif len(documento) == 14:
            return doc_cnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos incorreto.")


class doc_cpf:
    def __init__(self, cpf):
        if self.valid(cpf):
            self.cpf = cpf
        else:
            raise ValueError("CPF inválido!")

    def __str__(self):
        return self.format()

    def valid(self, cpf):
        validador = CPF()
        return validador.validate(cpf)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class doc_cnpj:
    def __init__(self, cnpj):
        if self.valid(cnpj):
            self.cnpj = cnpj
        else:
            raise ValueError("CNPJ inválido!")

    def __str__(self):
        return self.format()

    def valid(self, cnpj):
        validador = CNPJ()
        return validador.validate(cnpj)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
