import math

A, B, C = map(int, input().split())

P = (A + B + C) / 2
res = math.sqrt(P * (P - A) * (P - B) * (P - C))

print(f"{res:.3f} m2")