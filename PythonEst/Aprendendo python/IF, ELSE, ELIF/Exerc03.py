#Exercício 3: Cálculo de Desconto Progressivo (Setor de Vendas) Um e-commerce aplica descontos automáticos no carrinho. Crie um programa que receba o valor total da compra e aplique a seguinte lógica:
#Compras a partir de R$ 500,00: 15% de desconto.
#Compras a partir de R$ 200,00 (e menos de 500): 10% de desconto.
#Compras abaixo de R$ 200,00: Sem desconto. O programa deve exibir o valor do desconto e o valor final a pagar, formatados em R$.

print('-'*40)
print('Olá, Mundo, Seja bem vindo a essa experiencia')
print('-'*40)

entrada = input('Por favor, insira o valorda compra: ')

# Remove "R$", espaços e troca a vírgula decimal por ponto
entrada_limpa = entrada.replace('R$', '').replace(' ', '').replace(',', '.')
valor = float(entrada_limpa)
print(valor)

if valor >= 500:
    desconto = valor * 15/100
    aplicado = valor - desconto
    print('Descomto de 15% aplicado')
    print(f'Valor do desconto: {desconto}')
    print(f'Valor da compra é {aplicado}')
elif 500 > valor >= 200:
    desconto = valor * 10/100
    aplicado = valor - desconto
    print('Desconto de 10% aplicado')
    print(f'Valor com desconto: {desconto}')
    print(f'Valor da compra é {aplicado}')
else:
    print('Compra sem descomto')