# cidade=input('Escreva o nome da sua cidade:').lower().strip()
cidade = 'Santa Catarina'

primeiro_nome = cidade.split()
print(primeiro_nome[0])
if primeiro_nome == 'santos':
    print('Sua cidade começa com "Santo!"')
else:
    print('Sua cidade não começa com "Santo"...') 