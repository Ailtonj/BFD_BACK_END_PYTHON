# Crie um arquivo .py. Comece declarando uma variável saldo_bancario com o valor 1000.
# Peça ao usuário para inserir três valores: um valor de depósito, um valor de saque e um fator de juros.

# Utilize o operador de atribuição de adição (+=) para adicionar o depósito ao saldo_bancario.
# Utilize input() para capturar dados numéricos decimais do usuário, convertendo-os para float(), 
# e use print() para exibir os resultados na tela.

# Utilize o operador de atribuição de subtração (-=) para subtrair o saque do saldo_bancario.
# Utilize o operador de atribuição de multiplicação (*=) para aplicar o fator de juros ao saldo_bancario.
# variavel_decimal = float(input("Digite um valor: "))

#saldo inicial
saldo_bancario = 1000
print(f"Saldo inicial: {saldo_bancario:.2f}\n")

#Fazendo depósito
valor_deposito = float(input("Informe o valor de deposito; "))
saldo_bancario += valor_deposito
print(f"Saldo após o depósito: {saldo_bancario:.2f}\n")

#fazendo um saque
valor_de_saque = float(input("Informe o valor de saque: "))
saldo_bancario -= valor_de_saque
print(f"Saldo após o saque: {saldo_bancario:.2f}\n")

#aplicando juros
fator_de_juros = float(input("Informe o fator de juros: "))
saldo_bancario *= fator_de_juros
print(f"Saldo após ser aplicado o Juros: {saldo_bancario:.2f}\n")




