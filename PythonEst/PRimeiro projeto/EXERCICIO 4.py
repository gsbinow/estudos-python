#Faça um programa que leia algo pelo teclado e de informações sobre ele
a=input('Digite algo:')
print(f'O tipo primitivo de desse valor é: {type(a)}')
print(f'Só tem espaços? {a.isspace()}')
print(f'É um numerico? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É alfanumerico? {a.isalnum()}')
print(f'Está capitalizado (primeira letra maiucusla)? {a.istitle()}')