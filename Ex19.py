valor = int(input("Digite o valor a ser sacado: "))

quantidade_200 = valor // 200
valor = valor % 200

quantidade_100 = valor // 100
valor = valor % 100

quantidade_50 = valor // 50
valor = valor % 50

quantidade_20 = valor // 20
valor = valor % 20

quantidade_10 = valor // 10
valor = valor % 10

quantidade_5 = valor // 5
valor = valor % 5

quantidade_2 = valor // 2
valor = valor % 2

quantidade_1 = valor // 1

print("O número mínimo de notas necessárias é:")
print(f"{quantidade_200} nota(s) de R$200")
print(f"{quantidade_100} nota(s) de R$100")
print(f"{quantidade_50} nota(s) de R$50")
print(f"{quantidade_20} nota(s) de R$20")
print(f"{quantidade_10} nota(s) de R$10")
print(f"{quantidade_5} nota(s) de R$5")
print(f"{quantidade_2} nota(s) de R$2")
print(f"{quantidade_1} nota(s) de R$1")
