vendas_semana = [1200, 1500, 1100, 2000, 2500, 1800, 1300]
# calculando a soma 
soma = sum(vendas_semana)

# iniciando uma variavelcom o primeiro valor da lista
menor = vendas_semana[0]

# percorrendo a lista e mudando o valor da variavel menor se encontrar um valor menor
for x in vendas_semana:
    if x <= menor:
        menor = x

# pegando o index do menor valor
dia = vendas_semana.index(menor)

# fazendo uma comparação do index e seu dia correspondente
match dia:
    case 0:
        print("Domingo")
    case 1:
        print("Segunda-feira")
    case 2:
        print("Terça-feira")
    case 3:
        print("Quarta-feira")
    case 4:
        print("Quinta-feira")
    case 5:
        print("Sexta-feira")
    case 6:
        print("Sábado")
