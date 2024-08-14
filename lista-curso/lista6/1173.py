def func(v):
    if v <= 50:
        for c in range(0, 10):
            print(f"N[{c}] =", v)
            v = v * 2
n = int(input())
func(n)
