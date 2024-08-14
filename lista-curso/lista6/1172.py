def func(x):
    if x <= 0:
        x = 1
    print(f"X[{j}] =", x)

for j in range(0, 10):
    n = int(input())
    func(n)