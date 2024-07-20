comprimento = float(input('Informe o comprimento da caixa '))
altura = float(input('Informe o comprimento da altura '))
largura = float(input('Informe o comprimento da largura '))
quantidade_caixas = float(input('Informe o comprimento da quantidades de caixas '))

area_caixa = 2 * (comprimento * altura + comprimento * largura + altura * largura)

area_total = (area_caixa * quantidade_caixas) * 1.10

print(f'A quantidade de material necessária é: {area_total:.2f} metros quadrados')