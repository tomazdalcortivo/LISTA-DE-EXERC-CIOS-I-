tempo_seg = int(input('Digite o tempo em segundos '))

# utilizei divisão intera por pegar exatamente quando contabiliza uma hora ou dia 
tempo_min  = tempo_seg // 60 
tempo_horas = tempo_min // 60 
tempo_dias = tempo_horas // 24 

print(f'Tempo em minutos: {tempo_min}')
print(f'Tempo em horas: {tempo_horas}')
print(f'Tempo em dias: {tempo_dias}')  