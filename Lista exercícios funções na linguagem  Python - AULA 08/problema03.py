# Problema 03
# 3. Problema - Contador de vogais
# Crie um arquivo .py. Dentro do seu arquivo, construa um código que define
# uma função que receba um texto qualquer como argumento. A função deve
# retornar a quantidade de vogais (a, e, i, o, u) do valor informado e esse
# resultado deve ser mostrado na tela.

def contador_vogais(texto):
    t = str(texto)
    t = t.lower()
    qtd_vogais = 0
    qtd_vogais += t.count('a')
    qtd_vogais += t.count('e')
    qtd_vogais += t.count('i')
    qtd_vogais += t.count('o')
    qtd_vogais += t.count('u')
    qtd_vogais += t.count('á')
    qtd_vogais += t.count('é')
    qtd_vogais += t.count('í')
    qtd_vogais += t.count('ó')
    qtd_vogais += t.count('ú')
    qtd_vogais += t.count('â')
    qtd_vogais += t.count('ê')
    qtd_vogais += t.count('î')
    qtd_vogais += t.count('ô')
    qtd_vogais += t.count('û')
    qtd_vogais += t.count('ã')
    qtd_vogais += t.count('à')
    qtd_vogais += t.count('õ')
    

    return qtd_vogais


print(contador_vogais("Olá Ailton!"))
