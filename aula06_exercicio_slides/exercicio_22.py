numeros = [10, -5, 20, 0, -1, 30]
soma = 0
for x in numeros:
    if x<=0:
        continue
    if x%2==0:
        pass
    soma +=x
print(soma)