def teste1():
    dados = list()
    dados.append('Pedro')
    dados.append(18)
    print(dados)
    pessoas = list()
    pessoas.append(dados[:])#copia da lista
    print(pessoas)


def teste2():
    cadastro = list()
    isolamento = list()
    while True:
        nome = str(input('Informe seu primeiro nome: '))
        idade = input('digite sua idade: ')
        cadastro.append(nome)
        cadastro.append(idade)
        isolamento.append(cadastro[:])
        cont = input('deseja continuar? [s|n]: ').lower()
        if cont in ['n','não','nao']: 
            print('programa encerrado...')
            break
    print(isolamento)
    print(isolamento[0])
    if len(isolamento) > 0:
        for i in range(1,len(isolamento)):
          print(isolamento[i])
    
    isolamento2 = [['pedro' ,25],['Joao',20],['Alice',26]] #listas compostas
    
    print(isolamento2[2])
    # mostrar lista isolada
    
    print(isolamento2[0][0]) 
    #mostrar item dentro da lista isolado


def teste3():
    isolamento = list()
    acima = []
    abaixo = []
    ideal = []
    while True:
        nome = str(input('Informe seu primeiro nome: '))
        peso = input('digite seu peso: ')
        isolamento.append([nome, peso])
        cont = input('deseja continuar? [s|n]: ').lower()
        if cont in ['n','não','nao']: 
            print('programa encerrado...')
            break
        
    n = len(isolamento)
    for pessoa in isolamento:
        if pessoa[1] > 68:
            acima.append(pessoa[0])
        elif pessoa[1] < 68:
            abaixo.append(pessoa[0])
        else:
            ideal.append(pessoa[0])

            
    print(f'\nAcima do peso (68kg): {acima}')
    print(f'Abaixo do peso (68kg): {abaixo}')
    print(f'No peso ideal (68kg): {ideal}')
     
teste3()



