# Enunciado: Você foi contratado para desenvolver um sistema de cobrança de serviços de
# uma copiadora. Você ficou com a parte de desenvolver a interface com o funcionário.
# A copiadora opera da seguinte maneira:

# ▪ Se número de páginas for menor que 20 retornar o número de página sem desconto;
# ▪ Se número de páginas for igual ou maior que 20 e menor que 200 retornar o número
# de páginas com o desconto é de 15%;
# ▪ Se número de páginas for igual ou maior que 200 e menor que 2000 retornar o
# número de páginas com o desconto é de 20%;
# ▪ Se número de páginas for igual ou maior que 2000 e menor que 20000 retornar o
# número de páginas com o desconto é de 25%;
# ▪ Se número de páginas for maior ou igual à 20000 não é aceito pedidos nessa
# quantidade de páginas;

# ♦ Para o adicional de encadernação simples (1) é cobrado um valor extra de 15 reais;
# ♦ Para o adicional de encadernação de capa dura (2) é cobrado um valor extra de 40
# reais;
# ♦ Para o adicional de não querer mais nada (0) é cobrado um valor extra de 0 reais;
# O valor final da conta é calculado da seguinte maneira:
# total = (servico * num_pagina) + extra

# Elabore um programa em Python que:




#
# D. Deve-se implementar a função servico_extra() em que:
# a. Pergunta pelo serviço adicional;
# b. Retornar (use return) o valor de apenas uma das opções de adicional
# c. Repetir a pergunta item D.a se digitar uma opção diferente de: 1/2/0;

# E. Deve-se implementar o total a pagar no código principal (main), ou seja, não pode
# estar dentro de função, conforme o enunciado;
# F. Deve-se implementar try/except;
# G. Deve-se inserir comentários relevantes no código;
# Teste seu código atendendo as seguintes exigências:
# H. Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu
# nome e sobrenome;
# I. Deve-se apresentar na saída de console um pedido no qual o usuário errou a opção
# de serviço;
# J. Deve-se apresentar na saída de console um pedido no qual o usuário ultrapassou
# no número de páginas;
# K. Deve-se apresentar na saída de consol

# A. Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu
# nome e sobrenome (somente print, não usar input aqui);

print('bem vindo a grafica G.S!')
print('\n---------------Serciços----------------')
print('-----------------------------------------')
print(f'(dig) Digitalçao preço:       R$1.10')
print(f'(ico) colorido preço:         R$1')
print(f'(ipb)Preto e branco preço:   R$0.40')
print(f'(fot)Fotocopia preço:        R$0.20')
print('-----------------------------------------') 
print('\n------------Serciços Extras-------------')
print(f'encardenação simples preço: R$14')
print(f'encardenação dura preço:    R$40')
print('-----------------------------------------\n')

# B. Deve-se implementar a função escolha_servico() em que:
def escolha_servico():
    while True:
     # a. Pergunta o servico desejado;
     pedido = input('Qual serviço deseja? |(dig)|(ico)|(ipb)|(fot)| ').lower().strip()
     if pedido == 'dig':
         return 1.10 # b. Retorna o valor servico com base na escolha do usuário (use return);
     elif pedido == 'ico':
         return 1
     elif pedido == 'ipb':
         return  0.40
     elif pedido == 'fot':
         return 0.20
     else: # c. Repete a pergunta do item B.a se digitar uma opção diferente de:
# dig/ico/ipb/fot;
         print('Escolja invalida, escolha novamente...')
         continue #retornar

# C. Deve-se implementar a função num_pagina() em que:
def num_pagina():
    while True:
        try: # a. Pergunta o número de páginas;
            paginas = int(input('Numero de paginas que deseja: '))
            if paginas > 20000:
             print('Não fazemos esse pedido...')
             print('Tente noamente')
             continue
            if paginas < 20:
             porcentagem = 0 
            elif paginas <200:
             porcentagem = 0.15 # 15%
            elif paginas < 2000:
             porcentagem = 0.20 #20%
            elif paginas <= 20000:
             porcentagem = 0.25 #25%
            else:
             print('Não aceitamos essa quantidade de paginas...')
             # b. Retorna (use return) o número de páginas com desconto seguindo a regra
            return paginas * (1 - porcentagem) # Oq vai sair dessa função
        
        
# do enunciado (desconto calculado em cima do número de páginas);
        
    
        except ValueError:
            print('Erro: Por favor, digite apenas números inteiros.')
 
    
    # Valores de exemplo (coloque os seus valores reais aqui)
def servico_extra():
    while True:
        try:
            resposta = input('Gostaria do serviço extra? (S)/(N): ').upper().strip()
        
            if resposta not in ['S', 'SIM', 'N', 'NÃO', 'NAO']:
             print('Opção inválida... Digite S ou N.')
             continue 
        
            if resposta in ['N', 'NÃO', 'NAO']:
             print('Entendido! Prosseguindo sem extras...')
              
            
            if resposta in ['S', 'SIM']:
             print('Muito bem!')
             mais = input('Escolha o serviço: (1) - Capa simples | (2) - Capa dura | (3) - Sair : ').upper().strip()

             if mais in ['1', 'CAPA SIMPLES']:
                return 15.00 
             elif mais in ['2', 'CAPA DURA']:
                return 40.00
             elif mais in ['sair', '3']:
                print('Obrigado pela preferencia!')
             else:
                print('Opção inválida. Vamos tentar de novo.')
                continue 
        except ValueError:
           print('Por favor digite um numero valido')


try:
    # 1. Chamamos a função do serviço e guardamos o preço
    valor_servico = escolha_servico()
    
    # 2. Chamamos a função das páginas e guardamos o número de páginas com desconto
    paginas_com_desconto = num_pagina()
    
    # 3. Chamamos a função do extra e guardamos o preço do extra
    valor_extra = servico_extra()
    
    # Requisito E: O cálculo da conta conforme a fórmula do enunciado
    total = (valor_servico * paginas_com_desconto) + valor_extra
    
    # Requisito K (Implícito): Apresentar a saída formatada do console
    print(f"\nTotal a pagar: R$ {total:.2f} (serviço: {valor_servico:.2f} * páginas: {paginas_com_desconto:.0f} + extra: {valor_extra:.2f})")

except Exception as erro:
    print(f"Ocorreu um erro inesperado no programa: {erro}")
