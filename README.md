[LISTA DE EXERCÍCIOS I (ESTRUTURAS SEQUENCIAL E DE DECISÃO).pdf](https://github.com/user-attachments/files/16353462/LISTA.DE.EXERCICIOS.I.ESTRUTURAS.SEQUENCIAL.E.DE.DECISAO.pdf)

Orientações:

    a) Em cada exercício, utilize mensagens adequadas para explicar ao usuário o que é solicitado ou o resultado do programa.
    b) Os exercícios obrigatórios estão avaliados em três níveis de dificuldade:
        [*] fácil
        [**] médio
        [***] difícil
    c) Os problemas destacados como [****] são desafios de programação e não são de entrega obrigatória.
    d) A resolução desta lista de exercícios valida 10h do curso.

Estrutura Sequencial

[*] Escreva um programa em Python que calcule a área de um triângulo, considerando a equação:

area = base * altura / 2

[*] Escreva um programa em Python que leia dois números nas variáveis v1 e v2, calcule sua média na variável media e imprima seu valor.

[*] Escreva um programa em Python que leia dois números nas variáveis nA e nB, nessa ordem, e imprima em ordem inversa. Por exemplo, se os dados lidos forem 5 e 9, devem ser impressos na ordem 9 e 5.

[*] Escreva um programa em Python que leia três valores, representando o comprimento, largura e altura de uma caixa retangular e calcule o seu volume.

[*] Escreva um programa em Python para determinar o consumo médio de um automóvel, sendo fornecida a distância total percorrida pelo automóvel e o total de combustível gasto.

[*] Uma revendedora de carros paga aos seus funcionários vendedores dois salários-mínimos fixos, mais uma comissão fixa de R$ 150,00 por carro vendido e mais 5% do valor das vendas. Escreva um programa em Python que determine o salário total de um vendedor.

[*] O sistema de avaliação de determinada disciplina é composto por três provas. A primeira prova tem peso 2, a segunda prova tem peso 4 e a terceira prova tem peso 6. Escreva um programa em Python para calcular a média final de um aluno dessa disciplina.

[*] Um produto é vendido por um preço composto pelos seguintes valores: custo de produção, custo de transporte, impostos, margem de lucro. Faça um programa em Python que leia o valor do custo de produção (em R$), o custo para transporte (em R$), o percentual de impostos (em %) e o percentual de margem de lucro (em %) e mostre o preço final do produto ao consumidor. O preço do produto será dado pela equação:

scss

preço_final = custo_producao + (custo_producao * taxa_impostos) + custo_producao * taxa_lucro + transporte

[**] Escreva um programa em Python que leia dois valores: p e t, representando, respectivamente, o valor de uma prestação e a taxa de juros (entre 0 e 100) cobrada pelo atraso. Calcule o valor da prestação atrasada p_a com a equação:

css

p_a = p + (p * t / 100)

[**] Escreva um programa em Python que leia dois valores, representando o raio r e a altura a de uma lata e calcule seu volume v, cuja equação é dada por:

css

v = 3.1415 * r² * a

[**] Escreva um programa em Python que leia uma temperatura em graus Fahrenheit t_f e converta para graus Celsius t_c, cuja equação de conversão é:

scss

t_c = (t_f – 32) * (5 / 9)

[**] Escreva um programa em Python que leia uma quantidade de chuva dada em polegadas e imprima o equivalente em milímetros (25,4 mm = 1 polegada).

[**] Escreva um programa em Python para ler, calcular e escrever a média aritmética entre quatro números.

[**] Escreva um programa em Python que calcule a quantidade de galões de tinta necessários, bem como o seu custo, para pintar um tanque de combustível em formato cilíndrico. Sabe-se que o galão de 3,6 litros de tinta custa R$ 60,00 e que cada litro de tinta pinta três metros quadrados em média. Para se obter uma pintura de qualidade, são necessárias duas demãos.

[**] Uma fábrica deseja produzir caixas de papelão e para isso precisa adquirir matéria-prima. Escreva um programa em Python que leia o comprimento, a altura e a largura do modelo de caixa que será produzido, assim como a quantidade de caixas a serem fabricadas. Determine a quantidade de material em metros quadrados sabendo que é necessário prever um adicional de 10% sobre o valor mínimo de modo a garantir a produção.

[**] Faça um programa em Python em que o usuário informa os valores dos catetos de um triângulo retângulo e que ao final escreva a sua hipotenusa.

[**] Escreva um programa em Python que receba um intervalo de tempo em segundos. Calcule e imprima na tela quanto este intervalo corresponde em minutos, horas e dias.

[***] Escreva um programa em Python que leia um valor inteiro positivo e menor que 1000, armazene-o numa variável do tipo int e determine a soma dos dígitos que formam o valor. Exemplo: o valor 397 tem a soma dos dígitos igual a 3 + 9 + 7 = 19. Pesquise sobre o operador mod em Python.

[***] Suponha que um caixa eletrônico disponha de notas de 1, 2, 5, 10, 20, 50, 100 e 200 reais. Considerando que alguém está sacando uma quantia, escreva um programa em Python que mostre o número mínimo de notas de cada tipo que o caixa eletrônico deve entregar ao cliente.

[***] Dado que se tem o valor de um ângulo expresso em graus, minutos e segundos (exemplo 35º47'59''), escreva um programa em Python que forneça o valor desse ângulo em radianos. Dica: 360° = 2 * PI radianos.

[***] A compra de um produto ou serviço pago a empresa no exterior com cartão de crédito está sujeita à cobrança de Imposto sobre Operações Financeiras (IOF) na taxa de 6,38% sobre o valor convertido para reais. Sendo assim, escreva um programa em Python que leia o valor de uma compra (em dólar) e a taxa de câmbio do dia (ex: 1 dólar = 5 reais) e ao final imprima o valor da compra em reais (sem IOF), o valor do IOF e o valor total cobrado da pessoa.

[****] Escreva um programa em Python para determinar a distância entre dois pontos em um plano cartesiano.

[****] Uma escala termométrica é usualmente definida a partir de duas informações sobre a água, a saber: o seu ponto de fusão e o seu ponto de evaporação. Supondo uma nova escala termométrica chamada Estevam, na qual o ponto de fusão se dá no valor 20 e o ponto de evaporação ocorre em 150. Escreva um programa em Python que converta uma temperatura medida em Celsius para Estevam.

[****] A mesma ideia utilizada para criar novas escalas termométricas pode ser adotada para normalizar uma grandeza qualquer entre valores pré-definidos. Por exemplo, em uma aplicação de visão computacional é necessário ler valores de pixels de uma imagem. Sabendo que a representação da imagem utiliza uma profundidade de 8 bits, isso significa que os valores dos pixels podem variar entre 0 e 255. Entretanto, para usar como entrada em uma rede neural é necessário mudar a escala de valores para -1 a 1. Isso significa que um pixel 0 vale -1 e que um pixel 255 vale 1. Escreva um programa em Python que receba o valor de um pixel e o apresente dentro da escala entre -1 e 1.

Estrutura de Decisão

[*] Construa um programa em Python que receba como entrada dois valores e os imprima em ordem crescente.

[*] Faça um programa em Python que leia os valores A, B e C. Mostre uma mensagem que informe se a soma de A com B é menor, maior ou igual a C.

[*] Crie um programa em Python que peça o nome (tipo de dado literal), a altura e o peso de duas pessoas e apresente o nome da mais pesada e o nome da mais alta.

[*] Faça um programa em Python que leia o salário fixo de um vendedor e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas caso elas ultrapassem R$
