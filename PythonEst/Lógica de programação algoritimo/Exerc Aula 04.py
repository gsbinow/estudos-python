x= 10
y = 1
z = 5.5
res = (x > y) and (z == y) # x é maior que y e z é igual a y
print(res)
res2 = x > y or not z == y  #x é maior que y ou z não é igual a y
print(res2)
res3 = x > y or not z == y and y != y + z / x
print(res3)

média = 7
n1 = float(input('Insira sua nota de història:'))
n2 = float(input('Insira sua nota de Geografia:'))
n3 = float(input('Insira sua nota de filosofis:'))

if (n1 >= média):
    print('Você passou em história!')
elif  (n1 < média):
    print('Você não passou em história!')

if n2 >= média:
    print('Você passou em Geografia!')
elif n2 < média:
    print('Você não passou em Geografia!')
if n3 >= média:
    print('Você passou em filosifia!')
elif n3 < média:
    print('Você não passou em filosifia')
print('Resultado final:')
if n1 >= média and n2 >= média and n3 >= média:
    print('Parabens, você foi aprovado!')
else:
    print('você foi reprovado')
