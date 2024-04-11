num1 = int(input())
cont = 0
cobaias = 0
Coelhos = 0
Ratos = 0
Sapos = 0

while cont < num1:
    Num, Str = input().split()
    Num = int(Num)
    Str = str(Str)
    if Str == "C":
        Coelhos += Num
    elif Str == "R":
        Ratos += Num
    elif Str == "S":
        Sapos += Num 
    cobaias += Num
    cont += 1

PorcentCoelho = (Coelhos / cobaias) * 100
PorcentRatos = (Ratos / cobaias) * 100
PorcentSapos = (Sapos / cobaias) * 100

print(f"Total: {cobaias} cobaias")
print("Total de coelhos",Coelhos)
print("Total de ratos",Ratos)
print("Total de sapos",Sapos)

print(f"Percentual de coelhos: {PorcentCoelho:.2f} %")
print(f"Percentual de ratos: {PorcentRatos:.2f} %")
print(f"Percentual de sapos: {PorcentSapos:.2f} %")