#crie um comando que leia um numero e forneça seu sucessor e antecessor/ Exercicio 1

n=int(input('digite um numero inteiro'))
ant=n-1
su=n+1
print(f'Analisando numero inteiro {n}:')
print(f'O sucessor é {su} e antecessor é {ant}')

#crie um programa que leia um numero inteiro e de o seu dobro o seu triplo e sua raiz quadrada

n=int(input('Digite um numero inteiro:'))
do=n*2
tri=n*3
raiz=n**(1/2) 
print(f'O dobro do numero {n} é {do}, o triplo é {tri} e a raiz é {raiz}')

#Desenvolva um programa que leia as notas de um aluno e calcule a sua média:

print('bem vindo aluno, espero que tenha se esforçado duranteo ano! irei calcular sua média na matéria')
n=input('Digite a matéria que deseja verificar:')
print(f'Muito bem!\n suas notas em {n} são: \n Prova 1: 80 \n prova 2:76 \n Prova 3:40 \n Prova 4: 89')
prova1=int(80)
prova2=int(76)
prova3=int(40)
prova4=int(89)

soma=(prova1+prova2+prova3+prova4) /4
print('-' * 30)
print(f'A média final ´{soma}')

if soma>=60:
    print('Situação: Aprovado')
if soma<=60:
    print('Situação: reprovado')

# Escreva um programa que leia um valor em metros e e o exiba convertido em centimetros e milimetros

    m = float(input('Digite o numero que deseja converter:'))
    c = int(m * 100)
    mi = int(m * 1000)
    print('-' * 40)
    print(f'{m} metros \nEquivale a {c} centimetros \n E tambem a {mi} milimetros ')

