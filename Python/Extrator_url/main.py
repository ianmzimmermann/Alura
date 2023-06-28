url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
# print(url)

indice_base = url.find('?')

url_base = url[0:indice_base]
# print(url_base)

# if (indice_base):
url_parametros = url[indice_base + 1:len(url)]
print(url_parametros)

param_moeda_origem = 'moedaOrigem'
indice_origem = url_parametros.find(param_moeda_origem)
indice_moeda_origem = indice_origem + len(param_moeda_origem) + 1

moeda_origem = url_parametros[indice_moeda_origem:]
