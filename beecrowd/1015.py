import math
eixox = input().split()
eixoy = input().split()
x1 = float(eixox[0])
x2 = float(eixox[1])
y1 = float(eixoy[0])
y2 = float(eixoy[1])

distancia = math.sqrt((x2 - x1) ** 2) + ((y2 - y1) ** 2)

print(distancia)