#Escreva um programa que leia um valor em metros e e o exiba convertido em centimetros e milimetros

m=float(input('Digite o numero que deseja converter:'))
c=int(m*100)
mi=int(m*1000)
print('-'*40)
print(f'{m} metros \nEquivale a {c} centimetros \n E tambem a {mi} milimetros ')

