# # Problema 05
# 5. Problema - Média notas
# Crie um arquivo .py. Dentro do seu arquivo, construa um código que define
# uma função calcular_media que aceita qualquer quantidade de notas (*args)
# e retorne a média delas.
# Exemplo de uso: calcular_media(8.5, 9.0, 7.5) deve retornar 8.33.

def calcular_media(*notas):
    return sum(notas)/len(notas)


print(calcular_media(8.5, 9.0, 7.5))
