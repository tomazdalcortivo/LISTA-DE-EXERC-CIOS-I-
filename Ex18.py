numero = int(input('Digite um valor inteiro positivo menor que 1000 '))

unidade = numero % 10 
dezena = (numero // 10) % 10 
centena = (numero // 100) % 10 

soma_dos_digitos = unidade + dezena + centena 

print(f"A soma dos dígitos de {numero} é {soma_dos_digitos}")