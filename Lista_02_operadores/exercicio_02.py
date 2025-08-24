# Exercicio 2
# Crie um arquivo .py. Escreva um código que receba dois números do usuário e guarde nas
# variáveis A e B. Em seguida, calcule a soma, a subtração, a multiplicação e divisão de A por
# B. Mostre na tela cada um dos resultados na tela.
# Obs: Lembre-se de quais são os operadores aritméticos(+, -, *, /, //, %, **) e como eles
# devem ser utilizados. Além disso, lembre-se de utilizar as funções de conversão int() ou
# float() para converter o valor de texto que vai ser enviado pelo usuário para numérico:
# ● variavel_inteira = int(input("Digite um valor: "))
# ● variavel_decimal = float(input("Digite outro valor: "))

a = float(input("Informe um número: "))
b = float(input("Informe outro numero:"))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b

print(f"A + B = {soma:.2f}")
print(f"A - B = {subtracao:.2f}")
print(f"A * B = {multiplicacao:.2f}")
print(f"A / B ={divisao:.2f}")
