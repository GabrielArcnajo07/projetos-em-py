def contagem_pares_impares():
    pares = 0
    impares = 0

    for i in range(10):
        numero = int(input(f"Digite o {i + 1}º número inteiro: "))
        
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")


contagem_pares_impares()