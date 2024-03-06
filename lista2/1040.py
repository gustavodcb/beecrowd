n1, n2, n3, n4 = map(float, input().split())
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
print(f"Media: {media:.1f}")

if media < 5.0:
    print("Aluno reprovado.")
elif media >= 7.0:
    print("Aluno aprovado.")
else:
    nota = float(input())
    print("Aluno em exame.")
    print("Nota do exame:", nota)
    mediaFinal = (media + nota) / 2
    print("Aluno aprovado.")
    print(f"Media final: {mediaFinal:.1f}")
