i = 0
cont = 0
while i < 6:
    i += 1
    valor = float(input())
    if valor > 0:
        cont += 1
else:
    print(f"{cont} valores positivos")