import math 

raio = float(input('Digite o valor do raio do tanque em metros: '))
altura = float(input('Digite o valor da altura do tanque em metros: '))

area_superfice = 2 * math.pi * raio * (altura + raio)

area_total = 2 * area_superfice

litros_tinta = area_total / 3

# math.ceil para arredondar para cima
galoes_tinta = math.ceil(litros_tinta / 3.6) 

custo_total = galoes_tinta * 60

print(f'A quantidade de galões de tinta necessários é: {galoes_tinta}')
print(f'O custo total da tinta é: R$ {custo_total:.2f}')