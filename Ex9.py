p = float(input('Informe o o valor de uma prestação '))
t = float(input('Informe o valor da taxa de juros (entre 0 e 100): '))

p_a = p + (p * t / 100)

print(f'O valor da prestação atrasada foi de R$ {p_a:.2f}')