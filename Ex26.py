a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))


if a + b > c:
    print(f"A soma de {a} + {b} é maior que {c}.")
elif a + b < c:
    print(f"A soma de {a} + {b} é menor que {c}.")
else:
    print(f"A soma de {a} + {b} é igual a {c}.")
