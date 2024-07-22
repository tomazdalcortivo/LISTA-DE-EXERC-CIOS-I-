valor_dolar = float(input("Digite o valor em dolar a ser convertido "))

COTACAO_DOLAR = 5.80 

valor_conversao = valor_dolar * COTACAO_DOLAR 

valor_conversao_IOF = valor_conversao * 1.0638
 
print(f"O valor em dólar ${valor_dolar} equivale a R${valor_conversao:.2f} na conversão sem IOF.")
print(f"Com IOF, o valor convertido é R${valor_conversao_IOF:.2f}.")
