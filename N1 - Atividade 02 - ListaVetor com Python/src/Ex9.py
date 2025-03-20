vetorA = []
somaQuadrados = 0

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    vetorA.append(numero)

for numero in vetorA:
    somaQuadrados += numero ** 2

print(f"\nA soma dos quadrados dos elementos de A é: {somaQuadrados}")
