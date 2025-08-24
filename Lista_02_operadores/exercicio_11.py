# Exercicio 11
# Crie um arquivo .py. Escreva um programa que receba do usuário a quantidade de Km 
# percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado. 
# Obs: Por agora, evite o uso das estruturas condicionais, foque em utilizar os operadores 
# aritméticos(+, -, *, /, //, %, **). Além disso, lembre-se de utilizar as funções de conversão int() 
# ou float() para converter o valor de texto para numérico. 
# ● variavel_inteira = int(input("Digite um valor: ")) 
# ● variavel_decimal = float(input("Digite outro valor: "))

PRECO_DIA = 60
PRECO_KM = 0.15

distancia_percorrida = float(input("Informe a distância percorrida em km: "))
qtd_dias = int(input("Informe a quantidade de dias que o carro ficou alugado: "))

total_a_pagar = distancia_percorrida * PRECO_KM + qtd_dias * PRECO_DIA

print(f"O total a ser pago é R$ {total_a_pagar:.2f}")