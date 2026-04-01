#Exemplo estrutura de repetição


#Sem estutura
print(1)
print(2)
print(3)
print(4)
print(5)
print('-'*40)
#----------------------------------------
x=1
print(x)
x=2
print(x)
x=3
print(x)
x=4
print(x)
x=5
print(x)
print('-'*40)
#---------------------------------------
x=1
print(x)
x = x + 1
print(x)
x = x + 1
print(x)
x = x + 1
print(x)
x = x + 1
print(x)
print('-'*40)
#---------------------------------
#Usando while

x=1
while (x <=10): #Enquanto x for menor ou igual a 5 ele repitira
    print(x)
    x=x+1
print('-'*40)
#------------------------------
x=1
final=40
while (x <= final):
    if (x % 2 ==0):
        print(x)
    x = x+1
print('-'*40)
#-----------------------------------
soma = 0
cont = 1
while (cont <=5):
    x = float(input(f'Digite a {cont} nota:'))
    soma = soma + x
    cont = cont + 1
média = soma / 5
print(f'Média final: {média}')
#-----------------------------------
#Validação de entrada:
x = int(input('Digite um valor maior do que zero:'))
while (x <= 0):
    x = int(input('Digite um valor maior do que zero:'))
print(f'Você digitou {x}. Encerrando programa...')
#---------------------------------------------------------
print('digite um texto que ira se repetir para você')
print('para encerrar digiyte "sair"')

while True:
    texto = input('')
    print(texto)
    if texto == 'sair':
        break
print('Encerrando o programa...')
#---------------------------------------------------------------
# while True:
    # nome = input('Qual é o seu nome?')
    # if (nome != 'Teucu'):
        # continue
    
    # senha = input('Qual é a sua senha?')
    # if (senha == 'bunda'):
        # break
# print('Acessp concedido.')
#----------------------------------------------------
for i in range(6):
    print(i)
    # o programa ira contar de 0 ate a 5 automatico

for i in range (0, 5, 1):
    print(i)
    # o programa contara do 1 ate 5
    #---------------------------------------------
frase = "logica de programação"
for i in range(0, len(frase),1):
        print(frase[i]), #end= "")
