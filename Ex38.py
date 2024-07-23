ASSINATURA = 21.40
CUSTO_LOCAL = 0.03
CUSTO_INTERURBANO = 0.40

min_locais = float(input("Minutos locais excedentes: "))
min_interurbanos = float(input("Minutos interurbanos excedentes: "))

valor_local = min_locais * CUSTO_LOCAL
valor_interurbano = min_interurbanos * CUSTO_INTERURBANO
valor_total = ASSINATURA + valor_local + valor_interurbano

print(f"Assinatura (R$): {ASSINATURA:.2f}")
print(f"Minutos locais (R$): {valor_local:.2f}")
print(f"Minutos interurbanos (R$): {valor_interurbano:.2f}")
print(f"Total (R$): {valor_total:.2f}")
