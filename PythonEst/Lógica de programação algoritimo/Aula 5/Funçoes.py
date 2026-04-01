def div():
    print('-'*40)
div()

def funcao ():
    print('|','__'*10,'|')

div()
funcao()
print('         Teste Função')
funcao()

div()

def funcao_variavel(s1):
    print('|','__'*10,'|')
    print(s1)
    print('|','__'*10,'|')

funcao_variavel( '\n Teste função variavel')

div()

def bordas(s2):
    tam = len(s2)
    if tam:
        print('+','-'*tam,'+')
        print('|',s2,'|')
        print('+','-'*tam,'+')
bordas('Olá')
bordas('Qual é o seu nome?  ')

div()

def soma1(x=0,y=0,z=0): #Valores padrão 
    res = x+y+z
    return res

#programa principal
retornado = soma1(1,2,3)#alteração do x,y,z
print(retornado)

print(soma1(2,2)) #exibindo a variavel soma e somando 2+2

# div()

# def string_valido(pergunta,min,max):
#     s1 = input(pergunta)
#     tam = len(s1)
#     while ((tam<min) or (tam > max)):
#         s1 = input(pergunta)
#         tam = len(s1)
#     return s1

# x = string_valido('Digite uma String:',10,30)
# print(f'Você digitou a strinhg {x}\n) Encerrando o programa...')

div()
while True:
    try:
        x = bordas(int(input('Digite um numero inteiro:')))
        break
    except ValueError:
        bordas('Numero invalido, tente novamente!')
