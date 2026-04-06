def div():
    print('-'*40,'\n')

lista = ['cao','gato','passaro','pato']

print(lista)
div()


print('troca de elemtnos:')
lista = ['cao','gato','passaro','pato','\n']
print(lista)
print('Trocar o item [3] pato por cavalo\n')
lista[3] = 'cavalo'
print(lista)
div()


print(' Adicionar elementos - .append()')
lista = ['cao','gato','passaro','pato']
print(lista,'\n')
print(' Adicionar galinha ao final da lista:\n')
lista.append('galinha')
print(lista)

div()
print(' Adicionar item a outra posiçã da lista: .insert(,)')
lista = ['cao','gato','passaro','pato']
print('\n Adicionando "boi" ao começo da lista:\n')

lista.insert(0,'boi')
print(lista)

div()


print('Remover item da lista - "del lista[]"\n')
lista = ['cao','gato','passaro','pato']
print(lista)

print('\nRemovendo gato\n')
del lista[1]
print(lista)

div()

print('\n Remover item da lista forma 2 - "lista.pop()"\n')
lista = ['cao','gato','passaro','pato']
print(lista)

print('\nRemovendo gato\n')
lista.pop(1)
print(lista)

div()

print('Remover item da lista metodo3 - "lanche.removel("nome do item")"\n')
lista = ['cao','gato','passaro','pato']
print(lista)

print('\nRemovendo gato\n')
lista.remove('gato')
print(lista)


div()

valores = list(range(0,20))
print(valores)


print('Ordenar lista numérica:')
valores = [8,4,3,6,9,0,2]
valores.sort()
print(valores)
print('Ordem inversa:')
valores.sort(reverse=True)
print(valores)


div()
a = [1,2,3,4,5,6]
b = a
print(a)
print(b)

div()
a = [1,2,3,4,5,6]
b = a
b[2] = 8
print(a)
print(b)

div()

a = [1,2,3,4,5,6]
b = a[:]
b[2] = 8
print(a)
print(b)
