numeros = []
soma = 0
multiplicacao = 1
for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

for i in range(2):
    soma += numeros[i]
    multiplicacao *= numeros[i]

print("\nSoma: ", soma)
print("Multiplicação: ", multiplicacao)