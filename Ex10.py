import math 

raio = float(input('Digite o valor do raio '))
altura = float(input('Digite o valor do altura '))

volume =  math.pi * (raio ** 2) * altura 

print(f'O volume do cilindro é {volume:.2f} metros cúbicos')