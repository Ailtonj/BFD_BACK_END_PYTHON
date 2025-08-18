# Crie um arquivo .py. Comece com uma variável tarefas com o valor 20 e 
# crie uma variável chamada numero_pessoas que receberá um número informado pelo usuário. 
# Utilize o operador de atribuição de divisão inteira (//=) para dividir 
# as tarefas igualmente entre as pessoas e atualizar a variável tarefas. 
# Mostre o número de tarefas que cada pessoa recebeu na tela.

# Obs: Utilize o operador de atribuição de divisão inteira [ //= ], 
# input() e print() para exibir os valores na tela do usuário e siga a estrutura abaixo para receber os dados do usuário:

# variavel_inteira = int(input("Digite um valor: "))
# variavel_inteira = int(input("Digite outro valor: "))

tarefas = 20
numero_pessoas = int(input("Informe o número de pessoas: "))
tarefas //= numero_pessoas

print(f"Cada pessoa recebeu {tarefas} tarefas.")

