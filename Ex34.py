nota = int(input("informe a sua nota"))

if 0 <= nota < 60:
    print("D")
elif 60 <= nota < 80:
    print("C")
elif 80 <= nota > 90:
    print("B")
elif 90 <= nota <= 100:
    print("A")
else: 
    print("Nota invalida")
