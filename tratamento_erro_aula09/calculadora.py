
# funções
def adicao(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    return a / b


# recebendo os numeros
try:
    num1 = float(input("Informe o primeiro número: "))
except:
    print("Erro: Valor inválido.")
else:
    try:
        num2 = float(input("Informe o segundo número: "))
    except:
        print("Erro: valor inválido.")

    # recebendo a operação
    else:
        operacao = input("Informe a operação ('+' , '-', '/', '*'): ")

        # Calculando a operação desejada
        try:
            match operacao:

                case '-':
                    resultado = subtracao(num1, num2)
                case '+':
                    resultado = adicao(num1, num2)
                case '*':
                    resultado = multiplicacao(num1, num2)
                case '/':
                    resultado = divisao(num1, num2)
                case _:
                    print("Erro: Operação inválida")
        except ZeroDivisionError:
            print("Erro: Divisão por zero")
        else:
            print(f"{num1} {operacao} {num2} = {resultado:.2f}")
finally:
    print("Fim do programa")
