# Aprendendo comandos python

# print = comentario
print('-'*40)
print('Meu primeiro código em Python')
print("Meu segundo código Python")
#sempre que for escrever algo use ''ou ""
 
 #===========================================

# Variaveis = Caixas de armazenamento de dados
# varivel não tem espaço; sem letra maiuscula; sem carcterie esepcial
variavel= 'Isso é uma variavel'
dinhero = 1200
gastos = 1300
resto = dinhero - gastos
Musica = 'dança Kuduro'

print (variavel)
print (dinhero)
print (f'{gastos} e {resto}')
print(f'Uma musica boa é {Musica}')
# f é um atalho para exibir a variavel em meio a uma frase 

#==================================================

#Matematica:
   # int -> numeros inteiros
numero1 = int(input('digite um numero')) 
   #Int vai registrar a resposta do usuario como um numero e não como uma frase.

   # float -> Para números decimais serem registrados e respeitados
numero2 = float(input('Digite um numero decimal:'))       


 # Outros:
  # string -> textos
  #booleanos -> Verdadeiro ou falso ( True / False )

 # Simbolos:
   # > -> maior que
   # >= -> maior ou igual que
   # < -> menor ou igual que
   # <= -> menor ou igual que
   # == -> identico a 
   # != não sei

maior_numero = numero1 >= numero2

print(f'A afirmação do maior numero ser o {numero1} é {maior_numero}')

 # Operadores matematicos:
  # % -> Resto de uma divisão
     # 10/3 = 9 e sobra 1. esse 1 sera exibido
 # // -> Parte inteira da divisão (Sem considerar a cirgula)

duração_contrato= 140 #meses

anos = duração_contrato // 12 # // para fazer a divisao inteira
meses_sobra = duração_contrato % 12  
print(f'O contrato possui {anos} anos e {meses_sobra} meses de sobra')