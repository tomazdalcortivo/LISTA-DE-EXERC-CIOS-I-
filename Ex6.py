SALARIO_MINIMO = 1302.00

carrosVendidos = int(input("Digite o número de carros vendidos: "))
valorTotalVendas = float(input("Digite o valor total das vendas: "))

salarioFixo = 2 * SALARIO_MINIMO

comissaoFixa = 150 * carrosVendidos

comissaoPercentual = 0.05 * valorTotalVendas

salarioTotal = salarioFixo + comissaoFixa + comissaoPercentual

print(f"O salário total do vendedor é: R$ {salarioTotal:.2f}")
