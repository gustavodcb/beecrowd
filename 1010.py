codigoPeca1, numeroPeca1, valorPeca1 = input().split()
codigoPeca2, numeroPeca2, valorPeca2 = input().split()

codigoPeca1, numeroPeca1, codigoPeca2, numeroPeca2 = int(codigoPeca1), int(numeroPeca1), int(codigoPeca2), int(codigoPeca2)
valorPeca1, valorPeca2 = float(valorPeca1), float(valorPeca2)
l1 = numeroPeca1 + valorPeca1
l2 = numeroPeca2 * valorPeca2
valor = l1 + l2

print("VALOR A PAGAR: R$", l1)