nome1 = input("Digite o primeiro nome: ")
altura1 = float(input("Digite a altura da primeira pessoa: "))
peso1 = float(input("Digite o peso da primeira pessoa: "))

nome2 = input("Digite o segundo nome: ")
altura2 = float(input("Digite a altura da segunda pessoa: "))
peso2 = float(input("Digite o peso da segunda pessoa: "))

if altura1 >= altura2:
    print(f"A pessoa mais alta é a {nome1}")
else:
    print(f"A pessoa mais alta é a {nome2}")

if peso1 >= peso2:
    print(f"A pessoa mais pesada é {nome1}")
else:
    print(f"A pessoa mais pesada é {nome2}")
