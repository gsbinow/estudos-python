#Faça um programa que forneça a tabuada de um determinado numero inteiro
n=int(input('Digite um  numero para ver sua tabuada'))
print(f'\n A tabuada do {n}:')
print('-' * 40)

for i in range(1, 101):
    resultado=n*i
    print(f'{n} x {i:2} = {resultado}')
print('-' * 40)
