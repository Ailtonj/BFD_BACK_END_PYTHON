# 11. Problema - Gerenciamento de Estoque  
# Crie um arquivo .py. Crie um conjunto chamado frutas que vai armazenar as 
# seguintes informações  'maçã', 'banana', 'manga', 'laranja'. Agora adicione 
# uma nova fruta a esse conjunto 'uva', depois remova um dos elementos 
# existentes 'banana' e 'manga'. 

from random import choice

frutas = {'maçã', 'banana', 'manga', 'laranja'}
frutas.add("uva")
lista = ['banana', 'manga']
frutas.remove(choice(['banana','manga']))

print(frutas)



