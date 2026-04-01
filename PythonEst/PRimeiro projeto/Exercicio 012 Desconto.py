print('Bem vindo ao seu programa de auxiolio de desconto!')

while True:
    print('-'*40)
    pergunta = input('Selecione: (1) Aplicar desconto | (2) Retirar desconto | (3) Sair:').lower().strip()


    if pergunta == '1' or pergunta == 'aplicar desconto':
        v = float(input('\nInsira o valor bruto:'))
        d = int(input('Taxa de desconto(%):'))
        de=v * ( d/100 )
        desconto = v - de
        print(f'O desconto de {d} % aplicado ao valor {v} é equivalente a {desconto:.2f}\n')
        print('Espero ter ajudado!')
        print('-'*40)
        break

    if pergunta == '2' or pergunta == 'retirar desconto':
        v = float(input('Insira o valor afetado:'))
        d = float(input('Taxa de desconto(%):'))
        di = (d/100)
        di2 = 1 - di
        s = v/di2
        print(f'O valor bruto desse produto é {s}!')
        print('Espero ter ajudado!')
    elif pergunta == '3' or pergunta == 'Sair':
        print('Encerrando programa...')
        break
    else:
        print('Opção inválida!')

        #Meu primeiro codigo que se mexer muito caga S2