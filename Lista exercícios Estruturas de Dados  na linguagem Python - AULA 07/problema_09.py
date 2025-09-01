# 9. Problema - Ficha Médica
# Crie um arquivo .py e defina um dicionário chamado meus_dados para
# armazenar dados pessoais de um usuário, contendo as chaves e valores
# 'nome': 'Alice', 'idade': 35 e 'cidade': 'Nova York'. Em seguida, adicione ao
# dicionário um novo par chave-valor 'profissao': 'Médica', modifique o valor da
# chave 'idade' para 40, acesse e imprima o valor associado à chave 'cidade' e,
# por fim, exiba o dicionário completo após todas as operações.

meus_dados = {'nome': 'Alice', 'idade': 35, 'cidade': 'Nova York'}


meus_dados["Profissão"] = "Médica"
meus_dados.update({"idade": 40})

print("Cidade: ", meus_dados["cidade"])
print(meus_dados)
