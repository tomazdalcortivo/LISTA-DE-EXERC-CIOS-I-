valor_apostado = float(input("Informe o valor total apostado: "))

# utilizei o metodo strip e o lower para remover espaços e tambem deichar tudo em letra minuscula 
ficha1 = input("Informe a cor da primeira ficha (branca/preta): ").strip().lower()
ficha2 = input("Informe a cor da segunda ficha (branca/preta): ").strip().lower()


if ficha1 == "branca" and ficha2 == "branca":
    valor_recebido = 0
elif (ficha1 == "branca" and ficha2 == "preta") or (ficha1 == "preta" and ficha2 == "branca"):
    valor_recebido = valor_apostado / 2
elif ficha1 == "preta" and ficha2 == "preta":
    valor_recebido = valor_apostado * 2

print(f"O valor que o jogador deverá receber é: R$ {valor_recebido:.2f}")