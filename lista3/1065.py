i = 1
pares = 0
impar = 0
positivo = 0
negativo = 0
while i <= 5:
    valor = int(input())
    if valor % 2 == 0:
        pares += 1
    if valor % 2 != 0:
        impar += 1
    if valor > 0:
        positivo += 1
    if valor < 0:
        negativo += 1
    i += 1
else:
    print(f"{pares} valor(es) par(es)")
    print(f"{impar} valor(es) impar(es)")
    print(f"{positivo} valor(es) positivo(s)")
    print(f"{negativo} valor(es) negativo(s)")