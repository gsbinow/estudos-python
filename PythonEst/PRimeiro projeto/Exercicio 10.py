#EScreva um programa que calcule quantos dolares uma pessoa pide comprar
print('-' * 40)
print('Bem vindo ao convertor de moedas!')
print('O dolar está atualmente valendo 5.35R$')
print('-' * 40)

n = float(input('Porfavor, informe o valor disponivel para compra:'))
d = 5.35
con = n/d
print(f'Exelente, com a quantia de {n} você pode comprar {con:.2f}')
pergunta=input('Gostaria de continuar a compra? ( sim / não )').lower().strip()
if pergunta == 'sim':
    print('O valor foi depositado em sua conta!')
    print('Atendimento encerrado, Obrigado!')
print('-' * 40)