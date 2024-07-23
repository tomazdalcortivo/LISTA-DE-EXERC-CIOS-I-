total_diarias = int(input("Informe o total de diarias: "))

VALOR_DIARIA = 60.00

if total_diarias > 5:
    valor_total_conta = (total_diarias * VALOR_DIARIA) + (5.50 * total_diarias)
elif total_diarias == 5:
    valor_total_conta = (total_diarias * VALOR_DIARIA) + (6.00 * total_diarias)
else:
    valor_total_conta = (total_diarias * VALOR_DIARIA) + (8.00 * total_diarias)

print(f"Número de diárias: {total_diarias}")
print(f"Valor total da conta com taxa já aplicada: R$ {valor_total_conta:.2f}")
