# # Problema 02
# 2. Problema - Inversor de string
# Crie um arquivo .py. Dentro do seu arquivo, construa um código que define
# uma função que receba um texto qualquer como argumento. A função deve
# retornar o valor informado porém com a ordem inversa e esse valor deve ser
# mostrado na tela.


def funcao(texto):
    t = str(texto)
    print(t[::-1])
    return t[::-1]


funcao("Ailton notlia")
