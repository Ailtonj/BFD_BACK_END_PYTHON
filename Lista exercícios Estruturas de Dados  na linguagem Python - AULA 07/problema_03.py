# Problema 3
# 3. Problema - Registro de Vendas
# Crie um arquivo .py .Escreva um código que vai armazenar a sequência 1200,
# 1500, 1100, 2000, 2500, 1800, 1300 de vendas de cada dia da semana em
# uma estrutura de dados do tipo lista chamada vendas semana. Pense no
# seguinte cenário, você precisa saber o valor total de vendas durante a
# semana e além disso, você precisa descobrir qual dia da semana com o
# menor valor de venda.

vendas_semana = [1200, 1500, 1100, 2000, 2500, 1800, 1300]
# calculando a soma
soma = sum(vendas_semana)
print(f"Total de vendas na semana: {soma}")
# iniciando uma variavelcom o primeiro valor da lista
menor = vendas_semana[0]
# menor = min(vendas_semana);
# percorrendo a lista e mudando o valor da variavel menor se encontrar um valor menor
for x in vendas_semana:
    if x <= menor:
        menor = x

# pegando o index do menor valor
dia = vendas_semana.index(menor)


# fazendo uma comparação do index e seu dia correspondente
match dia:
    case 0:
        print("Dia menos vendido: Domingo")
    case 1:
        print("Dia menos vendido: Segunda-feira")
    case 2:
        print("Dia menos vendido: Terça-feira")
    case 3:
        print("Dia menos vendido: Quarta-feira")
    case 4:
        print("Dia menos vendido: Quinta-feira")
    case 5:
        print("Dia menos vendido: Sexta-feira")
    case 6:
        print("Dia menos vendido: Sábado")
