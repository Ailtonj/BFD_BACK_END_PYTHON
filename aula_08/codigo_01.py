# Pense no seguinte cenario: voce precisa armazenar os dados de uma pessoa


# Formas de criar um dicionario no python

# vazio
dicionario = {}
# com dados dentro dela
dicionario = {"Nome": "Ailton",
              "Idade": 28,
              "Tem_carro": True,
              "Qtd_Carro": ["Corolla", "Porshe"]}

# acessando elementos
print(dicionario["Nome"])

# modificar
dicionario["Nome"] = "Thiago"
print(dicionario["Nome"])

dicionario.update({"Nome": "Maria L"})
print(dicionario["Nome"])


dicionario.update({"Renda_mensal": 5000})
print(dicionario["Renda_mensal"])

dicionario.update({"Tem_passaport": True})
print(dicionario["Tem_passaport"])


del dicionario["Tem_passaport"]
print(dicionario)

dicionario.pop("Qtd_Carro")
print(dicionario)

# keys
print(dicionario.keys())

# value
print(str(dicionario.values()))
# item
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")
