# # Problema 09
# 9. Problema - Busca de livro 
# Crie um arquivo .py. Dentro do seu arquivo, construa um código que define 
# uma função chamada buscar_livro que aceite um título obrigatório e kwargs 
# como filtros de busca (por exemplo, autor="Machado de Assis", ano=1899). 
# Imprima o título e todos os filtros aplicados.

def buscar_livro (titulo, **filtro):
    print(f"Título: {titulo}")
    for chave,valor in filtro.items():
        print(f"{chave}: {valor}")
    
        
buscar_livro("titulo",autor="Machado de Assis", ano=1899)
