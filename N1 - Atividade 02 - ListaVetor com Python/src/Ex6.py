medias = []
maiorMedia = 0

for i in range(10):
    print("\nAluno: ", i + 1)
    n1 = float(input("Dgiite a nota 1: "))
    n2 = float(input("Dgiite a nota 2: "))
    n3 = float(input("Dgiite a nota 3: "))
    n4 = float(input("Dgiite a nota 4: "))

    media = (n1 + n2+ n3 + n4) / 4
    medias.append(media)

    if media >= 7:
      maiorMedia += + 1

print("Alunos com media maior que 7:", maiorMedia)