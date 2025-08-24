# # Exercicio 3
# Crie um arquivo .py.Escreva um código que receba do usuário quanto ele ganha por hora
# e o número de horas que ele trabalha no mês, armazenando esses valores em duas
# variáveis diferentes. Calcule e mostre na tela o total do salário do usuário no referido mês.
# Obs: Lembre-se de quais são os operadores aritméticos(+, -, *, /, //, %, **) e como eles
# devem ser utilizados. Além disso, lembre-se de utilizar as funções de conversão int() ou
# float() para converter o valor de texto que vai ser enviado pelo usuário para numérico:
# ● variavel_inteira = int(input("Digite um valor: "))
# ● variavel_decimal = float(input("Digite outro valor: "))

salario_por_hora = float(input("Informe quanto você ganha por hora: "))
horas_trabalhadas_mes = int(input("Informe quantas horas você trabalha no mês: "))

total_salario_mes = salario_por_hora * horas_trabalhadas_mes

print(f"Seu salario total no mês é de R$ {total_salario_mes:.2f} ")
