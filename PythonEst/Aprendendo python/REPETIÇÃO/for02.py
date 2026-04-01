s=0
print('Os valores digitados serão somados;')
l = int(input('Digite a quantidade de numeros a serem somados:'))
for c in range(l):
    n = int(input('Digite um numero:'))
    s += n
print(f'A soma dos numeros é {s}')