# Crie um arquivo .py e peça para o usuário inserir dois valores inteiros. 
# Armazene-os nas variáveis dividendo e divisor. 
# Crie uma variável RESTO e atribua a ela o valor do resto da divisão de dividendo por divisor. 
# Mostre o resultado na tela no formato "divisor / dividendo = resultado | resto = resto".


dividendo = int(input("Informe o dividendo: "))
divisor = int(input("Informe o divisor: "))

quociente = dividendo // divisor
resto = dividendo % divisor

print(f"{dividendo} / {divisor} = {quociente} | Resto = {resto}")