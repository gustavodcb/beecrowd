a, b, c = map(int, input().split())

if(a <= b <= c):
    print(f"{a}\n{b}\n{c}")
elif(a <= c <= b):
    print(f"{a}\n{c}\n{b}")
elif(b <= a <= c):
    print(f"{b}\n{a}\n{c}")
elif(b <= c <= a):
    print(f"{b}\n{c}\n{a}")
elif(c <= a <= b):
    print(f"{c}\n{a}\n{b}")
else:
    print(f"{c}\n{b}\n{a}")

print("")
print(f"{a}\n{b}\n{c}")