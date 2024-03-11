a, b = map(int, input().split())

if a < b:
    d = b - a
elif a > b:
    d = 24 - a + b
else:
    d = 24

print(f"O JOGO DUROU {d} HORA(S)")