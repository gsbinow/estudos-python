nome = input('Insira seu nome completo:')

print(nome)


print(f'seu nome em maiusculo {nome.upper()}\n')
print(f'seu nome em minusculo {nome.lower()}\n')
print(f'Quantas eltras tem seu nome: {len(nome.strip())}\n')

primeiro_nome = nome.split()

print(f'Seu primeiro nome: {primeiro_nome[0]}\n')

print(f'Quantidades de letras do seu primeiro nome: {len(primeiro_nome[0])}\n')



