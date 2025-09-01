# 6. Problema - Identificação de Arquivos
# Crie um arquivo .py. Escreva um código que vai armazenar os seguintes
# dados de uma sequência de arquivos 'documento.pdf', 'foto.jpg',
# 'relatorio.pdf', 'planilha.xlsx' em uma tupla chamada arquivos. Você precisa
# contar quantas vezes a extensão .pdf aparece dentro da tupla e mostra o
# resultado na tela para os usuários.


arquivos = ('documento.pdf', 'foto.jpg', 'relatorio.pdf', 'planilha.xlsx')
quantidade = 0
for x in arquivos:
    if x.find(".pdf") != -1:
        quantidade += 1


print(quantidade, " vezes.")
