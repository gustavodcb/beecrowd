seg = int(input())
minu = seg // 60
seg %= 60
hor = minu // 60
minu %= 60
print(f"{hor}:{minu}:{seg}")
