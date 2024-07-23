disciplina = input("Informe a disciplina ")

nota = float(input("Digite a sua nota final "))
if (nota * 2) % 1 != 0:
    print( "Formanto de nota invalido")
else: 

    aulas_ministradas = int(input("Informe a quantidades de aulas da disiplina "))
    faltas = int(input("informe a quantidades faltas "))

    if (aulas_ministradas * 0.25) < faltas:
        print(f"Disciplina: {disciplina} - Nota: {nota:.2f} - Status: Reprovado por faltas")
    elif nota >= 5 and nota <= 10: 
        print(f"Disciplina: {disciplina} - Nota: {nota:.2f} - Status: Aprovado por nota")
    else:
        print(f"Disciplina: {disciplina} - Nota: {nota:.2f} - Status: Reprovado por nota")

