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
    print(isolamento[2])
teste2()