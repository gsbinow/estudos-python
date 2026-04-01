from wsgiref.types import InputStream
Faça a soma dos numeros:
n=(input('digite um valor'))
print(n)
n1=(input('digite um valor'))
n3=int(n)+int(n1)
print('A soma dos numeros {} e {} é {}'.format(n,n1,n3))
print(f'A soma dos numeros {n} e {n1} é {n3}')

n=float(input('Digite um numero'))
print(n)

n=input('Digite um numero')
print(n.isnumeric())
print(n.isalpha())
print(n.isalnum())
print(n.isdecimal())
