# Exercicio 5
opcao = int(input(
    "Escolha um dia da semana: "
    "\nOpção 1 -> Domingo"
    "\nOpção 2 -> Segunda-feira"
    "\nOpção 3 -> Terça-feira"
    "\nOpção 4 -> Quarta-feira"
    "\nOpção 5 -> Quinta-feira"
    "\nOpção 6 -> Sexta-feira"
    "\nOpção 7 -> Sábado"
    "\nOpção: "))


match(opcao):
    case 1:
        dia = 'Domingo'
    case 2:
        dia = 'Segunda-feira'
    case 3:
        dia = 'Terça-feira'
    case 4:
        dia = 'Quarta-feira'
    case 5:
        dia = 'Quinta-feira'
    case 6:
        dia = 'Sexta-feira'
    case 7:
        dia = 'Sábado-feira'
    case _:
        dia = 'Opção inválida'
print(dia)
