codigoPeca1, numeroPeca1, valorPeca1 = input().split()
codigoPeca2, numeroPeca2, valorPeca2 = input().split()

codigoPeca1, numeroPeca1, codigoPeca2, numeroPeca2 = int(codigoPeca1), int(numeroPeca1), int(codigoPeca2), int(numeroPeca2)
valorPeca1, valorPeca2 = float(valorPeca1), float(valorPeca2)

valor = (numeroPeca1 * valorPeca1) + (numeroPeca2 * valorPeca2)

print(f"VALOR A PAGAR: R$ {valor:.2f}") 
