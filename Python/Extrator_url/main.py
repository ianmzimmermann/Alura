url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
# print(url)

indice_base = url.find('?')

url_base = url[0:indice_base]
# print(url_base)

# if (indice_base):
url_parametros = url[indice_base + 1:len(url)]
print(url_parametros)

param_busca = 'moedaOrigem'
indice_param = url_parametros.find(param_busca)
indice_moeda = indice_param + len(param_busca) + 1
indice_divisao = url_parametros.find('&', indice_moeda)
if (indice_divisao == -1):
    moeda_origem = url_parametros[indice_moeda:]
else:
    moeda_origem = url_parametros[indice_moeda:indice_divisao]

print(moeda_origem)
