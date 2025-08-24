numeros = [10, -5, 20, 0, -1, 30]
soma=0
for x in numeros:
    if(x<=0):
        continue
    soma+=x
print(soma)

# soma = sum([x for x in numeros if x>0])
# print(soma)