# Exercicio 1

IDADE_MINIMA = 18
idade_usuario = int(input("Informe a sua idade: "))
if idade_usuario >= IDADE_MINIMA:
    print("O usuario é maior de idade.")
elif idade_usuario >= 16 and idade_usuario <= 17:
    print(f"O Usuario é menor e tem 16 ou 17 anos.")
else:
    print("O usuario é menor de idade")
