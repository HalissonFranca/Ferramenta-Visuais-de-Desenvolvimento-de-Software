def contar_consoantes():
    vogais = {'a', 'e', 'i', 'o', 'u'}
    caracteres = []

    
    for i in range(10):
        char = input(f"Digite o {i+1}º caractere: ").lower()
        if char.isalpha(): 
            caracteres.append(char)
        else:
            print("Entrada inválida. Digite apenas letras.")
            return

    consoantes = [c for c in caracteres if c not in vogais]

    print(f"\nNúmero de consoantes lidas: {len(consoantes)}")
    print(f"Consoantes encontradas: {' '.join(consoantes)}")


contar_consoantes()
