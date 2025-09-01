# 15. Problema - Cadastro de Produtos
# Crie um arquivo .py. Escreva um código que vai armazenar a sequência
# 'Teclado', 'Mouse' em uma lista chamada nomes e armazene a sequência 250,
# 120 em uma lista chamada precos e armazene a sequência 10, 25 em uma
# lista chamada estoques. Você precisa mesclar os elementos de cada uma
# das listas em uma única sequência, você pode fazer isso utilizando a zip() e
# mostre na tela o resultado dos valores.


nomes = ['Teclados', 'Mouse']
precos = [250, 120]
estoques = [10, 25]

lista = list(zip(nomes,precos,estoques))
for nome, preco, estoque in lista:
    print(f"Produto: {nome} -> R$ {preco:.2f} -> {estoque} Unidade")