num1 = int(input())
i = 1

if num1 % 2 != 0:
    print(num1)
    while i <= 5:
        num1 += 2
        print(num1)
        i += 1

if num1 % 2 == 0:
    num1 += 1
    print(num1)
    while i <= 5:
        num1 += 2
        print(num1)
        i += 1
