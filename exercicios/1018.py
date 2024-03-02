valor = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]

for nota in notas:
    #operador // não retorna resultado flutuando, exemplo: 3.666666
    quantidade_notas = valor // nota
    #atualiza o valor para o restante
    valor %= nota
    print(f"{quantidade_notas} nota(s) de R$ {nota},00")