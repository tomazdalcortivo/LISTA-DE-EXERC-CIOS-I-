idade = int(input("Informe a sua idade "))
anos_trabalhados = int(input("Informe os anos trabalhados "))


if idade < 65 or anos_trabalhados >= 30 or (idade >= 60 and anos_trabalhados >= 30):
    print("Requer aposentadoria ")
else:
    print("Não requer aposentadoria ")
