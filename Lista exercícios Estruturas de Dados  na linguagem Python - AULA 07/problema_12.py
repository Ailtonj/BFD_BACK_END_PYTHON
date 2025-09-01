# 12. Problema - Registro de Vendas  
# Crie um arquivo .py . Escreva um código que vai conter uma variável que vai 
# armazenar alguma frase qualquer. Seu objetivo é contar o número de 
# palavras únicas na frase fornecida.  
# Obs: Você pode utilizar os conceitos de lista e conjunto para concluir esse 
# objetivo. Além disso, você pode utilizar a função split() para dividir uma 
# string em frases. 

frase = input("Informe uma frase: ")

palavras = frase.split()
conjunto_palavras = set(palavras)

print(f"Quantidade de palavras únicas: {len(conjunto_palavras)}")
