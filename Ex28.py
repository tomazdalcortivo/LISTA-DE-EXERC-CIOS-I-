salario_fixo = float(input("Digite o seu salario mensal: "))
total_vendas = float(input("Digite o total de vendas efetuado em R$: "))


if total_vendas > 10000:
    salario_total = salario_fixo + (total_vendas * 0.15)
else:
    salario_total = salario_fixo + (total_vendas * 0.075)

print(f"O seu salário total foi R$ {salario_total:.2f}")
