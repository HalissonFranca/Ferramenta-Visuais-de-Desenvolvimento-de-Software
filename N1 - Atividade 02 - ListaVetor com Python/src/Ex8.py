colecaoidade = []
colecaoaltura = []

for i in range(5):
   print("Pessoa ", i + 1)
   altura =  float(input("Digite sua altura: "))
   colecaoaltura.append(altura)
   idade = int(input("Digite sua idade: "))
   colecaoidade.append(idade)

colecaoIdadeInvertida = colecaoidade[::-1]
colecaoAlturaInvertida = colecaoaltura[::-1]

print("Altura: ", colecaoAlturaInvertida)
print("Idade: ", colecaoIdadeInvertida)

