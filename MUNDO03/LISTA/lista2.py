def adicionar ():
    lista = []
    print('Digite "parar" para sair da lista')
    while True:
        n = input('Digite um numero para adicionar a lista:   ')
        lista.append(n)
        lista.sort()
        if n == 'sair':
         print(lista)
         print('Programa encerrado...')
         break
        
        

    
def teste():
   valores = []
   valores.append(9)
   valores.append(5)
   valores.append(3)
   valores.append(8)
   for c, v in enumerate(valores):
      print(f'Na posição {c} encontrei o valor {v}!') 
   print('fim')

def ligar():
   a = [1,3,4,9]
   b = a
   b[2] = 8
   print(f'lista a {a}')
   print(f'lista b {b}')
   ''' As duas listas mudaram enves de so mudar a lita b pq as duas estão intrerligadas.'''



def copia():
   a = [1,3,4,9]
   b = a[:]
   b[2] = 8
   print(f'lista a {a}')
   print(f'lista b {b}')
   ''' Somento o B foi alterado pois ele tem uma copia de A.'''


def desafio1():
   lista = []
   for n in range(5):
      n = int(input('digite um valor numerico para a lista:  '))
      lista.append(n)
   print(lista)
   maximo = max(lista)
   minimo = min(lista)
   print(maximo)
   posM = lista.index(max(lista))
   posE = lista.index(min(lista))
   print(f'O maior numero é {maximo} na posição {posM}')
   print(f'O menor numero é {minimo} na posição {posE}')






def desafio2():
   lista = []
   while True:
      n = int(input('Digite um numero:  '))
      lista.append(n)
      tipo = ''


      num_digitados = len(lista)
      print(f'A quantidade de numeros digitados foi: {num_digitados}')
   
      while tipo not in ['s','n']:
        tipo = str(input('Quer continuar? (s|n):  ')).lower().strip()
      if tipo == 'n':
        break
      
   print('-'*20)
   lista.sort(reverse=True)
   print(lista)
   if 5 in lista:
      print('5 Esta na lista')
   else:
      ('5 Não esta na lista...')



def desafio3():
   lista = []
   print('Digite 0 para sair')
   while True:
      n = int(input('Digite um numero:  '))
      
      if n == 0:
         break
      lista.append(n)
   listaPar = []
   listaImpar = []
   for valor in lista:#para ler toda a lista item por item
    if valor % 2 == 0:
        listaPar.append(valor)
    else:
       listaImpar.append(valor)
   print(f'\nPrimeira lista: {lista}\n')
   print(f'Lista com valores par: {listaPar}\n')
   print(f'Lista com valores impar: {listaImpar}\n')
   print('Programa encerrado...')

def desafio4 ():
   print( 'obs: Uma expressão é uma frase entre parenteses: "()"')

   '''Verificador se existe ou não. ele ira detextar se a frase dita possui os dois parenteses. 
   Se, a expressão tiver parenteses no começo ele sera adicionado a uma lista. Se o programa ler no digitado
   parenteses no final da frase, ele removera da lista. Se no fim a expressão estiver fora da lista, então ela estara correta.'''
   pilha = []
   expre = input('Digite uma expressão: ').strip().lower()
      
   for caractere in expre:
         if caractere == '(':
            pilha.append('(') 
         elif caractere == ')':
            if len(pilha) > 0: #Verifica se a lista esta vazia.
               pilha.pop()
         else:
            pilha.append(')')
            break #Pr encerrar o ciclo
   if len(pilha) == 0:
      print('Sua expressao esta correta!')
   else:
      print('Sua expressão est errada...')
desafio4()