def concatenar(*palavras):
    texto = ""
    for x in palavras:
        texto += f"{x} "
    return texto
print(concatenar("Ola", "Mundo", "!"))
