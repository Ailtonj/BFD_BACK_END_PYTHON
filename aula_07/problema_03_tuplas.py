arquivos = ('documento.pdf', 'foto.jpg', 'relatorio.pdf', 'planilha.xlsx')
quantidade = 0
for x in arquivos:
    if x.find(".pdf")==-1 :
        quantidade+=1
    
print(quantidade)

