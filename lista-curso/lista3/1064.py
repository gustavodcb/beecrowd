i = 0
positivos = 0
soma = 0
while i < 6:
    valor = float(input())
    if valor > 0:
        positivos += 1
        soma = soma + valor
    i += 1
else:
    print(f"{positivos} valores positivos")
    print(soma / positivos)

