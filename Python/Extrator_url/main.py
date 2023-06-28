url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
print(url)

indice_base = url.find('?')

url_base = url[0:indice_base]
print(url_base)

url_parametros = url[indice_base + 1:len(url)]
print(url_parametros)
