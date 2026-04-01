nome=input('Qual é o seu nome?')
print('prazer em te conhecer{:+^20}'.format(nome))
n1=int(input('Adicione um numero'))
n2=int(input('Adicione outro numero para a soma'))
s=n1+n2
n=n1-n2
a=n1*n2
b=n1/n2
c=n1**n2
d=n1//n2
e=n1%n2
print('A adição {} subtração {} soma {} divisão {}'.format(s,n,a,b), end=' ')
print('O resto é {}, {} , {} ' .format(c,d,e))

n1=int(input('Adicione um numero'))
n2=int(input('Adicione outro numero para a soma'))
s=n1+n2
n=n1-n2
a=n1*n2
b=n1/n2
c=n1**n2
d=n1//n2
e=n1%n2
print('A adição {} \n subtração {} \n soma {} \n divisão {}'.format(s,n,a,b), end=' ')
print('O resto é {},\n {} , \n{} ' .format(c,d,e))