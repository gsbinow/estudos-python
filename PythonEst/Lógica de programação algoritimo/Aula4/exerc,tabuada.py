tabuada = 1 #inicio.
while tabuada <= 10: #Repetição até 10
    print(f'tabuada do {tabuada}:') # Exibição de tabuada ate chegar a 10
    i = 1 
    while i <=10: #Reptição do multiplicador
        print(f'{tabuada} x {i} = {tabuada * i}')
        i += 1
    tabuada += 1

# 1ª ele cria uma variavel contendo o valor inicial | tabuada = 1
# 2ª while para estrutura de repetição de comaando até chegar a 10.
# 3ª print exibindo cada aumento da variavel
for i in range (1, 11, 1):
    print(f'A TABUADA DE {i}')
    for n in range (1,11,1):
        print(f'{i} x {n} ={i * n}')
        n += 1
    i += 1
    