# Crie um arquivo .py. Comece declarando uma variável numero com o valor 2 e uma variável
# expoente, que receberá um valor numérico informado pelo usuário. O valor atribuído à
# variável expoente deve ser usado para atualizar a variável numero, elevando-o a essa
# potência. Utilize o operador de atribuição de potência (**=) para realizar essa operação.
# Mostre o valor inicial de numero e o valor final na tela.
# Obs:Utilize input() para capturar um número inteiro, convertendo-o para int(), use o
# operador de atribuição de potência (**=) para atualizar a variável e, por fim, use print() para
# exibir os valores inicial e final."

# ● variavel_decimal = float(input("Digite um valor: "))

numero = 2
expoente = float(input("Digite o valor do expoente: "))
print(f"Numero inicial: {numero}")
numero **= expoente
print(f"Numero final: {numero:.0f}")
