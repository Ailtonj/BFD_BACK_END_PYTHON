# # Exercicio 6
# Crie um arquivo .py utilizando o vscode e Replique o código do programa abaixo, rode ele 
# no seu vscode e verifique onde está o erro, ao encontrar o erro, conserte-o. 
# Obs: Lembre-se de como são utilizados os operadores de atribuição matemáticos. 
# Código: 
# total_cliques = 0  
# total_cliques + = 1  
# print(f'O total de cliques e de: {total_cliques}') 
# total_cliques =+ 1  
# print(f'O total de cliques e de: {total_cliques}') 
# Saída esperada: 
# O total de cliques e de: 1 
# O total de cliques e de: 2 

total_cliques = 0  
# erro abaixo corrigido: foi tirado um espaço entre '+='
total_cliques += 1  
print(f'O total de cliques e de: {total_cliques}') 

# Possível erro corrigido abaixo: está invertido o sinal de '+' com o sinal de '='
# desinverti 
# O código estava funcionando, mas ele está atribuindo  exatamente 1 ao total_cliques e não somando + 1 ao valor. 
total_cliques += 1  

# erro abaixo corrigido: foi colocadoi ') no final.
print(f'O total de cliques e de: {total_cliques}')