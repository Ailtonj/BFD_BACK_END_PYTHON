# Problema 04
# 4. Problema - Concatenador de strings 
# Crie um arquivo .py. Dentro do seu arquivo, construa um código que define 
# uma função que receba um número variável de strings (*args). A função deve 
# concatená-las, mesclá-las em um único valor de texto string e retorná-la. 
# Exemplo de uso: juntar_strings("Olá", " ", "mundo", "!") deve retornar "Olá 
# mundo!". 
def concatenar_string (*palavras):
    '''Concatena Strings'''
    texto = ""
    for x in palavras:
        texto += f"{x} "
    return texto
print(concatenar_string("Ola", "Ailton", "!"))