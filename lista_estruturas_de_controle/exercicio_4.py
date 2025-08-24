# Exercicio 4
num1 = float(input("Informe o primeiro número: "))
num2 = float(input("informe o segundo número: "))
op = input("informe a operação desejada (+, -, /, *, //, %): ")

match op:
    case '+':
        resultado = num1 + num2
    case '-':
        resultado = num1 - num2
    case '/':
        resultado = num1 / num2
    case '*':
        resultado = num1 * num2
    case '//':
        resultado = num1 // num2
    case '%':
        resultado = num1 % num2
    case _:
        resultado = "operação inválida"
        print(resultado)
        exit()


print(f"{num1:.2f} {op} {num2} = {resultado:.2f}")
