numeros = []
par = []
impar = []

for i in range(20):
    numero = int(input("Digite um número: "))
    numeros.append(numero)


for i in range(20):
    if numeros[i] % 2 == 0:
        par.append(numeros[i])
    else:
        impar.append(numeros[i])

print("\nNumeros: ", numeros)
print("\nPares: ", par)
print("\nImpares: ", impar)
    
