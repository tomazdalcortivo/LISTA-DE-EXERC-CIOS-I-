tipo_media = input("Informe o tipo de média a ser calculada (aritmetica/ponderada): ").strip().lower()


nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

if tipo_media == "aritmetica":

    media = (nota1 + nota2 + nota3) / 3
elif tipo_media == "ponderada":

    peso1 = float(input("Informe o peso da primeira nota: "))
    peso2 = float(input("Informe o peso da segunda nota: "))
    peso3 = float(input("Informe o peso da terceira nota: "))

    media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

print(f"A média calculada é: {media:.2f}")
