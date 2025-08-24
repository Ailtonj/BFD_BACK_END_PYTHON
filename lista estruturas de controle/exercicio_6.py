# Exercicio 6

nota = int(input("Informe uma nota de 1 a 5: "))
match nota:
    case 1:
        print("Muito ruim")
    case 2:
        print("Ruim")
    case 3:
        print("Média")
    case 4:
        print("Boa")
    case 5:
        print("Muito Boa")
    case _:
        print("Nota inválida")
