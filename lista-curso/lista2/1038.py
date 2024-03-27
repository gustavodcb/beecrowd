cod, quant = map(int, input().split())
preco = [4.00, 4.50, 5.00, 2.00, 1.50]

if(cod == 1):
    c = preco[0] * quant
    print(f"Total: R$ {c:.2f}")
elif(cod == 2):
    c = preco[1] * quant
    print(f"Total: R$ {c:.2f}")
elif(cod == 3):
    c = preco[2] * quant
    print(f"Total: R$ {c:.2f}")
elif(cod == 4):
    c = preco[3] * quant
    print(f"Total: R$ {c:.2f}")
elif(cod == 5):
    c = preco[4] * quant
    print(f"Total: R$ {c:.2f}")