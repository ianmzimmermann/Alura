class CPF:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido.")

    def __str__(self):
        return self.cpf_format()

    def cpf_valido(self, documento):
        if len(documento) == 11:
            return True
        else:
            return False

    def cpf_format(self):
        cpf_slice = []

        for i in range(0, len(self.cpf), 3):
            tupla_cpf = (self.cpf[i], self.cpf[i+1:i+2], self.cpf[i+2:i+3])
            cpf_slice.append(tupla_cpf)

        cpf_formatado = "{}{}{}.{}{}{}.{}{}{}-{}{}".format(
            cpf_slice[0][0],    cpf_slice[0][1],    cpf_slice[0][2],
            cpf_slice[1][0],    cpf_slice[1][1],    cpf_slice[1][2],
            cpf_slice[2][0],    cpf_slice[2][1],    cpf_slice[2][2],
            cpf_slice[3][0],    cpf_slice[3][1],
        )

        return cpf_formatado
