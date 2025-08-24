# Crie um arquivo .py e peça para o usuário inserir dois valores numéricos (podem ser inteiros
# ou decimais). Armazene-os nas variáveis num1 e num2. Crie uma variável
# MULTIPLICACAO e atribua a ela o valor da multiplicação entre num1 e num2, além disso
# crie uma variável DIVISAO e atribuir a ela o valor da divisão de num1 por num2. Mostre o
# resultado na tela no formato "num1 * num2 = resultado".
# Obs: Utilize os operadores de aritméticos de MULTIPLICACAO[ * ] e DIVISAO[ / ], use a
# função input() para capturar os dados, print() para exibir e siga a estrutura abaixo para
# receber os dados do usuário:

# ● variavel_inteira = int(input("Digite um valor: "))
# ● variavel_inteira = int(input("Digite outro valor: "))


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

multiplicacao = num1 * num2
divisao = num1 / num2

print(f"{num1} * {num2} = {multiplicacao}\n{num1} / {num2} = {divisao:.2f}")
