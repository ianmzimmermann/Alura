from validate_docbr import CPF


class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_valid(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def cpf_valid(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de dígitos inválida!")

    def cpf_format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.cpf_format()
