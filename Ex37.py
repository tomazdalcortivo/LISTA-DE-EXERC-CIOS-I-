nota_portugues = float(input("Informe a nota de Português: "))
nota_matematica = float(input("Informe a nota de Matemática: "))
nota_conhecimentos_gerais = float(input("Informe a nota de Conhecimentos Gerais: "))

media = (nota_portugues + nota_matematica + nota_conhecimentos_gerais) / 3

if media >= 60:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"

print(f"Média do candidato: {media:.2f}")
print(f"Status do candidato: {resultado}")
