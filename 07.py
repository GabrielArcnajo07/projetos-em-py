def calcular_tabela_divida(valor_divida):
    # Tabela de juros
    parcelas = [1, 3, 6, 9, 12]
    porcentagens_juros = [0, 10, 15, 20, 25]

    print("|{:<10}|{:<7}|{:<24}|{:<20}|".format("Dívida", "Juros", "Quantidade de Parcelas", "Valor da Parcela"))
    print("|" + "-" * 10 + "|" + "-" * 7 + "|" + "-" * 24 + "|" + "-" * 20 + "|")
    
    for i in range(len(parcelas)):
        quantidade_parcelas = parcelas[i]
        juros = (porcentagens_juros[i] / 100) * valor_divida
        valor_total = valor_divida + juros
        valor_parcela = valor_total / quantidade_parcelas

        print(f"| R$ {valor_total:.2f} | R$ {juros:.2f} | {quantidade_parcelas}                     | R$ {valor_parcela:.2f}       |")

# Solicitar o valor da dívida ao usuário
valor_divida = float(input("Digite o valor da dívida: R$ "))
calcular_tabela_divida(valor_divida)