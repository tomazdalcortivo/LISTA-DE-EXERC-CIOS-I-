valor_venda = float(input("Informe o valor da venda: "))
codigo_pagamento = int(input("Informe o código da condição de pagamento (1-6): "))

if codigo_pagamento == 1:
    valor_final = valor_venda * 0.90
    forma_pagamento = "Venda a Vista"
elif codigo_pagamento == 2:
    valor_final = valor_venda * 0.95
    forma_pagamento = "Venda a Prazo 30 dias"
elif codigo_pagamento == 3:
    valor_final = valor_venda
    forma_pagamento = "Venda a Prazo 60 dias"
elif codigo_pagamento == 4:
    valor_final = valor_venda * 1.05
    forma_pagamento = "Venda a Prazo 90 dias"
elif codigo_pagamento == 5:
    valor_final = valor_venda * 0.92
    forma_pagamento = "Venda com cartão de débito"
elif codigo_pagamento == 6:
    valor_final = valor_venda * 0.93
    forma_pagamento = "Venda com cartão de crédito"

print(f"Forma de pagamento: {forma_pagamento}")
print(f"Total da venda final (R$): {valor_final:.2f}")
