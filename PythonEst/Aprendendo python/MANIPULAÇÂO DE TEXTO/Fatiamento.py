def div():
    print('-'*40,'\n')

fatiamento = 'Micro espaços e afins sei lá'
print('leitura da quantidade total')
print(len(fatiamento))
print(fatiamento)

div()
print('Quantas vezes eiste na frase: ')
print(fatiamento.count('n'))

div()
print("Quantas vezes eiste na frase ate certo ponto: .count()")
print(fatiamento.count('n',0,13))

div()
print("encontrar: .find()")
print(fatiamento.find('ços'))

div()
print("trocar frasas: .replace()")
print(fatiamento.replace('Micro','Maximo'))

div()
print("maiusculo: .upper()")
print(fatiamento.upper())

div()
print('Letras minusuculas = .lower()')
print(fatiamento.lower())

div()
print("letras iniciais maiusuculas: .title()")
print(fatiamento.title())

div()
print("Remover espaços: .strip()")
print(fatiamento.strip())

div()
print("separa os carcteries formando uma lista [0,1,2,3,...]")
print(fatiamento.split())

div()
print('Junção de listas: .join()')
lista = fatiamento.split()
junção = '-'.join(lista)
print(junção)

div()
print('Inverter a frase inteira: ::-1')
print(fatiamento[::-1])
#---------------------------------------------------
div()
print('Divisoes')
print('0:5')
print(fatiamento[0:5])

div()
print(':5 tambem funciona')
print(fatiamento[:5])

div()
print('0: tambem')
print(fatiamento[0:])

div()
print('1:5')
print(fatiamento[1:5])

div()
print('0:29')
print(fatiamento[0:29])

div()
print('0:29:2')
print(fatiamento[0:29:2])

div()
print('::2')
print(fatiamento[::2])
