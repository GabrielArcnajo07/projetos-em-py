salario = 1000.00
ano_inicial = 1995
ano_final = 2025

aumento_1996 = 0.015  # 1.5%
salario *= (1 + aumento_1996)

for ano in range(1997, ano_final + 1):
    aumento = 2 * aumento_1996 
    salario *= (1 + aumento)
    aumento_1996 = aumento  

print(f"O salário do funcionário em {ano_final} será: R$ {salario:.2f}")