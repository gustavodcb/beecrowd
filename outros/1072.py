quantidadeN = int(input())
c = 0
i = 0
o = 0

while c < quantidadeN:
    N = int(input())

    if N >= 10 and N <= 20:
        i += 1
        c += 1
    else:
        o += 1
        c += 1

print(f"{i} in")
print(f"{o} out")