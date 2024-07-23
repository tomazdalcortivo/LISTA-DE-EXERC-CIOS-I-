idade = int(input("Informe a sua idade "))

if idade < 16:
    print("Não eleitor")
elif 18 <= idade <= 65:
    print("Eleitor obrigatorio")
else:
    print("Eleitor falcultativo")
