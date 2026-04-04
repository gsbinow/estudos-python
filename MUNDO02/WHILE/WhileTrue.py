from random import randint


def div ():
    print('-'*40)


def teste1 ():
    contador = 1
    while contador <= 10:
        print(contador, '->' , end='' ) 
        contador += 1
    print('Encerrado')



def teste2 ():
    contador = 1
    while True:
        print(contador, '->' , end='' ) 
        contador += 1
        if contador == 11:
            break
    print('Encerrado')



def lista ():
    lista = []
    print('O programa ira parar quandp digitar 999')
    while True:
       n =int(input('Digite um numero:'))
       lista.append(n)
       if n == 999:
           break
    print(len(lista)) #Quantidade de numero digitados
    print(sum(lista)) #soma dos numero



def tabuada():
    print('Digite um numeto negativo para parar')
    while True:
        n = int(input('Digite um numero para ver seu multiplicador:  '))
        if n < 0:
            print('Programa encerrado...')
            break
        for m in range(1,11):
            mult = n * m
            
            print(f'{n} x {m} é = {mult}')
            div()
    


def pi():
    v = 0
    while True:
        print('-' * 20)
        n = int(input('Digite um numero: '))
        computador = randint(0, 10)
        soma = n + computador
        
        tipo = ' ' # Começa com um espaço para entrar no while abaixo
        while tipo not in 'PI':
            tipo = str(input('Escolha: [P|I]: ')).strip().upper()[0]
            
        print(f'Seu numero: {n} | Computador: {computador} | Soma: {soma}')
        print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')

        if tipo == 'P':
            if soma % 2 == 0:
                v += 1
                print('VOCÊ VENCEU!')
            else:
                print('VOCÊ PERDEU!')
                break
        elif tipo == 'I':
            if soma % 2 == 1:
                v += 1
                print('VOCÊ VENCEU!')
            else:
                print('VOCÊ PERDEU!')
                break
        
        print('Vamos jogar novamente...')
        
    print(f'GAME OVER! Você venceu {v} vezes.')