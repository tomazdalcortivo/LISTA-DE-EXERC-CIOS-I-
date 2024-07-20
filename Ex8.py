valor_custo_producao = float(input('Digite qual valor foi o custo de produção: '))
custo_transporte = float(input('Digite qual valor foi o custo de transporte: '))
percentual_impostos = float(input('Digite qual valor foi o percentual de imposto (em %): '))
percentual_margem_lucro = float(input('Digite qual valor foi o percentual de margem de lucro (em %): '))


preco_final = valor_custo_producao + (valor_custo_producao * percentual_impostos / 100) + (valor_custo_producao * percentual_margem_lucro / 100) + custo_transporte

print(f'O preço final do produto é: R$ {preco_final:.2f}')
