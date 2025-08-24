# Exercicio 2
NOTA_MINIMA = 7
nota_final = float(input("Informe a nota final: "))
if nota_final >= 7:
    print("Aprovado.")

elif nota_final >= 4 and nota_final <= 6:
    print(f"Você não foi muito bem, mas consegue recuperar.")
else:
    print("Reprovado!")
