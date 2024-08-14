while True:
    # Lê os valores de entrada
    M, N = map(int, input().split())
    
    # Verifica se algum dos valores é menor ou igual a zero
    if M <= 0 or N <= 0:
        break

    # Encontra o menor e o maior valor
    menor = min(M, N)
    maior = max(M, N)

    # Calcula a soma dos inteiros consecutivos
    soma = sum(range(menor, maior + 1))

    # Imprime a sequência e a soma
    print(' '.join(map(str, range(menor, maior + 1))), "Sum={}".format(soma))