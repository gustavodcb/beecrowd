num = int(input())
cont = 0
a = 2

while cont < num:
    if a % 2 == 0 and a <= num:
        print(f"{a}^2 = {a ** 2}")
        a += 2
    cont += 1
    