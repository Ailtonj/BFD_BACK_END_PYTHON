nomes = ["Ana", "Pedro", "João", "Maria", "Carlos"]
nome = input("Informe o nome para buscar na lista: ")
for x in nomes:
    if x == nome:
        print("nome encontrado")
        break
else:
    print("nome não encontrado")
