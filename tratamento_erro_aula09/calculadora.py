
# declarando as funções
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
except ValueError:
    # Caso usuario degite uma letra no lugar do numero
    print("Erro: Valor inválido.")
else:
    try:
        num2 = float(input("Informe o segundo número: "))
    except ValueError:
        # caso usuario digite uma letra no ligar do numero
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
                    # caso o usuario digitou alguma operação invalida
                    raise ValueError("Operacao Inválida")
        except ZeroDivisionError:
            # Caso o usuario digitou o segundo numero 0 e escolheu a divisão
            print("Erro: Divisão por zero")
        except ValueError:
            # Caso o usuario informou uma operacao inválida
            print("Erro: Operacao inválida.")
        else:
            # Imprimindo o resultado
            print(f"{num1} {operacao} {num2} = {resultado:.2f}")
finally:
    # finalizando o programa
    print("Fim do programa")
