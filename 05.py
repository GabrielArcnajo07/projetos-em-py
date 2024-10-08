def gerar_tabela_precos():
    print("Lojas Quase Dois - Tabela de preços")
    for i in range(1, 51):
        preco = i * 1.99
        print(f"• {i} - R$ {preco:.2f}")

def calcular_valor(qtd_itens):
    return qtd_itens * 1.99

gerar_tabela_precos()

quantidade = int(input("Digite a quantidade de itens que o cliente comprou: "))
valor_total = calcular_valor(quantidade)

print(f"O valor total a ser pago é: R$ {valor_total:.2f}")