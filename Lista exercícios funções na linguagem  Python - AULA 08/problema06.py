# # Problema 06
# 6. Problema - Contador de vogais 
# Crie um arquivo .py. Dentro do seu arquivo, construa um código que define 
# uma função que receba um texto qualquer como argumento. A função deve 
# retornar a quantidade de vogais (a, e, i, o, u) do valor informado e esse 
# resultado deve ser mostrado na tela. 

def contador_de_vogais (*textos):
    texto = ""
    for x in textos:
        texto+= f"{x} "
    texto = texto.lower()
    print(texto)
    qtd_vogais = 0
    qtd_vogais += texto.count('a')
    qtd_vogais += texto.count('e')
    qtd_vogais += texto.count('i')
    qtd_vogais += texto.count('o')
    qtd_vogais += texto.count('u')
    qtd_vogais += texto.count('á')
    qtd_vogais += texto.count('é')
    qtd_vogais += texto.count('í')
    qtd_vogais += texto.count('ó')
    qtd_vogais += texto.count('ú')
    qtd_vogais += texto.count('â')
    qtd_vogais += texto.count('ê')
    qtd_vogais += texto.count('î')
    qtd_vogais += texto.count('ô')
    qtd_vogais += texto.count('û')
    qtd_vogais += texto.count('ã')
    qtd_vogais += texto.count('à')
    qtd_vogais += texto.count('õ')
    return qtd_vogais

print(contador_de_vogais("Olá Mundo", "Ailton", "Não"))
