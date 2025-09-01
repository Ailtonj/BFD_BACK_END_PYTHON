#  Problema - Análise de Dados de Vendas  
# Crie um arquivo .py. Escreva um código que vai armazenar os seguintes 
# dados de uma venda de produto e a quantidade dele  'Caderno', 15 em uma 
# tupla chamada venda. Você precisa calcular o valor total da venda, nesse 
# caso imagine que o preço unitário do produto é R$ 25,00. Mostre o resultado 
# na tela para o usuário.  


venda_produto = ('Caderno', 15)
preço_produto = 25.00

print(f"valor da venda: R$ {venda_produto[1]*preço_produto:.2f}")
