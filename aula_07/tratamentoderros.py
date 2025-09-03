

try:
    a = int(input("Informe um número: "))
    b = input("Informe um numero")
    resultado = 10/a
    resultado2 = a + b
except ZeroDivisionError:
    print("Impossível dividir por 0")
except ValueError:
    print("Letra digitada no lugar no número")
except TypeError:
    print("Você tentou somar um string com um inteiro")
else:
    print(resultado)
    print(resultado2)
finally:
    print("Encerrando...")
