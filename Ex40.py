num1 = float(input("informe o numero um "))
num2 = float(input("informe o numero dois "))
num3 = float(input("informe o numero três "))

# ignorei os caso de igualdade por que tanto faz se o numero é igual, não estaria sendo maior que o outro
if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num1 and num2 > num3:
    maior = num2
else:
    maior = num3

print(f"O maior numero é {maior}")
