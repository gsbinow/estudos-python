print('bem vindo alumo, espero que tenha se esforçado duranteo ano! irei calcular sua média na matéria')
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