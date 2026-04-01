print('Bem-vindo ao seu programa de auxílio engenharia!')

area_salva = 0  # Variável para armazenar o resultado anterior

while True: #While true=loop infinito do programa
    print('-' * 40)
    pergunta = input('Selecione: (1) Calcular área | (2) Cobrir área | (3) Sair: ').lower().strip()#lower transforma maiúscula em minúsculo


    if pergunta == '1' or pergunta == 'calcular área':
        a = float(input('Insira a altura (m): '))
        b = float(input('Insira a largura (m): '))
        area_salva = a * b
        print(f'A área total é de {area_salva:.2f} m²')#.2f numeros decimais exibidos apos o ponto


        usar_agora = input('Deseja calcular a cobertura para esta área agora? (s/n): ').lower().strip()
        if usar_agora == 's':
            pergunta = '2'  # Forçamos o programa a entrar no próximo bloco 'if'
        else:
            continue  # Volta para o menu principal

    if pergunta == '2' or pergunta == 'cobrir área':
        print('\n[Cobrir área] selecionado!')

        # Se ele veio da opção 1, já temos a área. Se não, perguntamos.
        if area_salva > 0: #testa se um numero é maior que zero
            usar_salva = input(f'Encontrei uma área de {area_salva:.2f} m² salva. Usar ela? (s/n): ').lower().strip()
            if usar_salva == 's':
                a_cobrir = area_salva
            else:
                a_cobrir = float(input('Insira o valor da nova área (m²): '))
        else:
            a_cobrir = float(input('Insira o valor da área (m²): '))

        d = input('O que será utilizado? ')
        litros = a_cobrir / 2
        print(f'Você precisará de {litros:.2f} litros de {d} para cobrir {a_cobrir:.2f} m².')
        area_salva = 0  # Resetamos após o uso (opcional)

    elif pergunta == '3' or pergunta == 'sair':
        print('Encerrando programa...')
        break
    else:
        print('Opção inválida!')






