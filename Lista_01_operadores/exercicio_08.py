# Crie um arquivo .py. Comece declarando uma variável saldo_bancario com o valor 1000.
# Peça ao usuário para inserir três valores: um valor de depósito, um valor de saque e um
# fator de juros.

# ● Utilize o operador de atribuição de adição (+=) para adicionar o depósito ao
# saldo_bancario.
# ● Utilize o operador de atribuição de subtração (-=) para subtrair o saque do
# saldo_bancario.
# ● Utilize o operador de atribuição de multiplicação (*=) para aplicar o fator de juros ao
# saldo_bancario.
# ●
# Utilize input() para capturar dados numéricos decimais do usuário, convertendo-os para
# float(), e use print() para exibir os resultados na tela.

# ● variavel_decimal = float(input("Digite um valor: "))


# Saldo Inicial
saldo_bancario = 1000

# depósito
valor_deposito = float(input("Informe o valor de depósito:\n"))

# saque
valor_saque = float(input("Informe o valor de saque:\n"))

# aplicando Juros
fator_juros = float(input("Informe o fator de juros:\n"))

# saldo inicial
print(f"Saldo inicial: {saldo_bancario:.2f}")

# saldo após o depósito
saldo_bancario += valor_deposito
print(f"Saldo após o depósito: {saldo_bancario:.2f}")

# saldo apóso saque
saldo_bancario -= valor_saque
print(f"Saldo após o saque: {saldo_bancario:.2f}")

# saldo após aplicação de juros
saldo_bancario *= fator_juros
print(f"Saldo após aplicação de juros: {saldo_bancario:.2f}")


