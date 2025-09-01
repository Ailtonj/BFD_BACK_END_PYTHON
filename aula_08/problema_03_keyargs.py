

def contar_vogais(*palavras):
    texto = ""
    vogais = 0
    for x in palavras:
        texto += x
    vogais += texto.count('a')
    vogais += texto.count('e')
    vogais += texto.count('i')
    vogais += texto.count('o')
    vogais += texto.count('u')
    return vogais


m = contar_vogais("ola mundo", "aeiou")
print(m)
