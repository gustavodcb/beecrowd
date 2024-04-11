dentro = 0
fora = 0
cont = 0

quant = int(input())
while cont < quant:
    valor = int(input())
    if valor >= 0:
        if valor >= 10 and valor <= 20:
            dentro += 1
        elif valor < 10 or valor > 20:
            fora += 1
    cont += 1

print(f"{dentro} in")
print(f"{fora} out")