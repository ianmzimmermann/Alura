url = "bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
print(url)


url_base = url[0:19]
print(url_base)

url_parametros = url[20:len(url)]
print(url_parametros)
