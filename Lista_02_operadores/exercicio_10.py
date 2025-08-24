# Exercicio 10
# Crie um arquivo .py. Escreva um código que leia um número inteiro qualquer que vai ser
# passado pelo usuário e mostre na tela o seu sucessor e seu antecessor.
# Obs: Por agora, evite o uso das estruturas condicionais, foque em utilizar os operadores
# aritméticos(+, -, *, /, //, %, **). Além disso, lembre-se de utilizar as funções de conversão int()
# ou float() para converter o valor de texto para numérico.
# ● variavel_inteira = int(input("Digite um valor: "))
# ● variavel_decimal = float(input("Digite outro valor: "))

num = int(input("Informe um número: "))
antecessor = num - 1
sucessor = num + 1
print(f"O sucessor de {num} é {sucessor}\nO antecessor de {num} é {antecessor}")
