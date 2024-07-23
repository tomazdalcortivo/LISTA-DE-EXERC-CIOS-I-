nome = input("Informe o nome do funcionário: ")
salario_bruto = float(input("Informe o salário bruto: "))
num_dependentes = int(input("Informe o número de dependentes: "))

desconto_inss = salario_bruto * 0.11

salario_liquido = (salario_bruto - desconto_inss) + (15.00 * num_dependentes) + 40.00 + 100.00

print(f"Nome do funcionário: {nome}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")
