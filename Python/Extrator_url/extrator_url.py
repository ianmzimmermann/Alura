class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitizacao(url)
        self.validacao()

    def sanitizacao(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def validacao(self):
        if not (self.url):
            raise ValueError("Url está vazia")

    def get_indice_base(self):
        indice_base = self.url.find('?')
        return indice_base

    def get_url_base(self):
        url_base = self.url[self.get_indice_base()]
        return url_base

    def get_url_param(self):
        url_parametros = self.url[self.get_indice_base() + 1:]
        return url_parametros

    def get_valor_param(self, param_busca):
        indice_param = self.get_url_param().find(param_busca)
        indice_moeda = indice_param + len(param_busca) + 1
        indice_divisao = self.get_url_param().find('&', indice_moeda)

        if (indice_divisao == -1):
            valor = self.get_url_param()[indice_moeda:]
        else:
            valor = self.get_url_param()[indice_moeda:indice_divisao]
        return valor


# extrator_url = ExtratorURL("https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")

extrator_url = ExtratorURL(None)
valor = extrator_url.get_valor_param("quantidade")
print(valor)
