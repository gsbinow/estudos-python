# # for é um intervalo fixo:
# for i in range(10):
#     print('Vai da esse seu cu!')

# #for para percorrer uma 
# lista = ['iphone','notbook', 'tv', 'não sei ']
# for item in lista:   #mostrar cade item da lista
#     print(item)
import time
def teste1():
    for n in range( 10,0-1, -1): #(comço, fim, ordem)
        print(n)
        time.sleep(1)
    print('Explodiu, Bum!')


def teste2():
    print('Os numeros pares de 1 a 50 são: ')
    for n in range(1,50+1):
     if n %2 == 0:
       
        print(f'{n}')
        time.sleep(0.2)

def teste3():
    s = 0
    print('Os numeros impars multiplos de 3, contados de 1 a 500 são: ')
    for n in range(1,500+1): #contar de 1 até 500. fim
     if n %2 == 1: # dentro do loop for, vai contar de 1 a 500 somento com numeros impars
        if n %3 == 0:# Usando os numeros impar, vai contar somente os numeros multiplos de 3
         s = s + n
         print(n , end= ' ')
        
    print(f'A soma dos numeros é: {s}') #fora do laço for. exibira a soma dos numeros



def teste4():
   n = int(input('Digite um numero:  '))
   print('-'*40)
   for i in range(0,10+1):
      r = n*i
      if i == 4:
         r = 'hellow world!'
      elif i != 4:
         r = n*i
      print(f'{i} - {n} x {i} = {r}')
   print('-'*40)
   print('Calculadora encerrada...')
   print('-'*40)


def teste5 ():
   s = 0
   for i in range(0,6):
    n = int(input('Digite um numero: '))
    if n %2 == 0:
       s += n
       
   print(s)

teste5()