
def teste1():
 contador = 1

 while contador < 11:
    print(contador)
    contador+=1
 print('FIM')




def teste2 (): 
 numero = 1
 soma = 0
 print('Digite "0" para parar a soma...')
 while numero != 0:
   numero = int(input('Digite um valor:'))
   soma += numero
 print(f' A soma dos numeros é: {soma}')  





def fatorial ():
    print('Programa de fatorial:')
    n = int(input('Digite um numero:'))
    resultado = 1
    numero = n
    while n >1:
      resultado *= n
      n = n -1
    print(f'O fatoriall do numero {numero} é  {resultado}')

def media ():
  lista = []
  while True:
    n = int(input('Digite um numero para a lsita: '))
    lista.append(n)
    borda()
    p = input('| (c) continuar / (p) parar: ').lower().strip()
    
    if p in ['p','parar']:
      break
  if len(lista) > 0:
    contar = len(lista)
    resultado = sum(lista)

    maximo = max(lista)
    minimo = min(lista)
    media = resultado / contar
    
    print('\n--- Resultados ---')
    print(f'Números digitados: {lista}')
    print(f'Maior valor: {maximo}')
    print(f'Menor valor: {minimo}')
    print(f'A média é: {media:.2f}')
  else:
    print('Nenhum numero foi encontrado...')

def borda():
  print('-'*40)

while True:
 print('  Escolha qual você quer iniciar: ')
 escolha = input(     '| (1) teste1 | (2) teste2 | (3) fatorial | (4) meida | (s) Sair | :\n').strip().lower()
 
 
 if escolha in ['1', '(1)', 'teste1']:
   print('(teste1) selecionado!',0.2)
   borda()
   teste1()
   borda()


 elif escolha == '2' or escolha == '(2)' or escolha == 'teste2':
   
   print('(teste2) selecionado!\n')
   borda()
   teste2()
   borda()

 elif escolha in ['3', '(3)', 'fatorial']:
   print('(fatorial) selecionado!')
   borda()
   fatorial()
   borda()


 elif escolha in ['4', '(4)', 'media']:
   print('(media) selecionado!')
   borda()
   media()
   borda()


 elif escolha == 's' or escolha == '(s)' or escolha == 'sair':
   print('programa encerrando...')
   break
 
 
 else:
   print('Opção não encontrada...')
   print('tente novamente', 0.2 ) 
   
   



