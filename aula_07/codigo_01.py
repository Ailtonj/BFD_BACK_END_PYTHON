produtos = ["Arroz", "Feijão", "Macarrão", "Óleo de Soja", "Sal",
            "Açúcar", "Café", "Leite", "Pão", "Manteiga", "Ovos",
            "Queijo", "Presunto", "Iogurte", "Frango", "Carne bovina",
            "Peixe", "Tomate", "Cebola", "Batata"]

# Acessando elementos de uma lista
print(produtos[0])

# Fatiando uma lista
print(produtos[0:4])

# formas de manipular uma lista
# adicionando novos valores

# append
print(produtos)
produtos.append("Biscoito")
print(produtos)
produtos.append(["Salgadinho", "Melão"])
print(produtos)

# Insert
produtos.insert(0, "Amendoim")
print(produtos)


# Removendo valores
# remove
produtos.remove(["Salgadinho", "Melão"])
print(produtos)

# pop
produtos.pop(0)
print(produtos)

# Ordenando valores
# sort
produtos.sort()
print(produtos)

# reverse
produtos.reverse()
print(produtos)

# count
produtos.append("Arroz")
produtos.append("Arroz")
produtos.append("Arroz")
print(produtos.count("Arroz"))

# index

print(produtos.index("Cebola"))

# len
print(len(produtos))

# del
del produtos[0:10]
print(produtos)

# clear
produtos.clear()
print(produtos)


# list comprehsion
preco = [2.00, 3.25, 5.45]

preco = [x*2 if x < 3 else x for x in preco]
print(preco)
