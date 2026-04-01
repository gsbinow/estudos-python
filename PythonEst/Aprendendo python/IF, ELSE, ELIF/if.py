#if cindiçao/comparação:
   #Tudo que acotecera se a condição for verdadeira:
#else: 
     #caso a condição seja falsa isso acontecera
     
vendas = 500
meta = 450

if vendas >= meta:
    print('batemos a meta de vendas')
    print('No mês que vem bateremos oo dobro!')
    if vendas >= (2* meta):
        print('Foi muito facil batemos o dobro da meta!')
    else:
        print('Passamos um pouco da meta!')
else:
    vendas_faltantes = meta - vendas
    print(f'Faltaram {vendas_faltantes} vendas')
    print('Meta nâo atingida')

    if vendas < 225:
        print('Meta extremamente abaixo do padrão!')
#-------------------------------------------------
# Meta do funcionario:

meta = 500
vendas = 1000

if vendas >= (2* meta):
    bonus = 100
elif vendas >= meta:
    bonus = 50
else:
    bonus = 0
print(bonus)
#--------------------------------------------------

lista = ['iphone', 'notebook', 'tv', 'video game', 'sofá']

produto = input(' digite o nome do produto a ser cadastrado:')

if produto in lista:
    print('Produto ja existe na lista!')
else:
    lista.append(produto)
    print(lista)
#--------------------------------------------------
