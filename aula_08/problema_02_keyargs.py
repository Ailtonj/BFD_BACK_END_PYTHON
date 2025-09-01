def calcular_media(*notas):
    media = sum(notas)/len(notas)
    return media
m = calcular_media(2,4,6)
print(m)