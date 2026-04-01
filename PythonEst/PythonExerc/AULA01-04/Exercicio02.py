#  EXERCÍCIO 2 - Conteúdos até aula 04
# Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um
# app de vendas para uma loja que vende Açaí e Cupuaçu. Você ficou com a parte de
# desenvolver a interface do cliente para retirada do produto.

# A Loja possui seguinte relação:
# • Tamanho P de Cupuaçu (CP) custa 9 reais e o Açaí (AC) custa 11 reais;
# • Tamanho M de Cupuaçu (CP) custa 14 reais e o Açaí (AC) custa 16 reais;
# • Tamanho G de Cupuaçu (CP) custa 18 reais e o Açaí (AC) custa 20 reais;

# Elabore um programa em Python que:
# A. Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu
# nome e sobrenome (somente print, não usar input aqui);
# B. Deve-se implementar o input do sabor (CP/AC) e o print “Sabor inválido. Tente
# novamente" se o usuário entra com valor diferente de CP e AC;
# C. Deve-se implementar o input do tamanho (P/M/G) e o print “Tamanho inválido.
# Tente novamente" se o usuário com entra valor diferente de P, M ou G;
# D. Deve-se implementar if, elif e/ou else, utilizando o modelo aninhado (aula 3 – Tema
# 4) com cada uma das combinações de sabor e tamanho;
# E. Deve-se implementar um acumulador para somar os valores dos pedidos;
# F. Deve-se implementar o input com a pergunta: “Deseja pedir mais alguma coisa?”.
# Se sim repetir a partir do item B, senão encerrar o programa executar o print do
# acumulador;
# G. Deve-se implementar as estruturas de while, break, continue (todas elas);
# H. Deve-se inserir comentários relevantes no código;
# Teste seu código atendendo as seguintes exigências:
# I. Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu
# nome e sobrenome;
# J. Deve-se apresentar na saída de console um pedido em que o usuário errou o sabor;
# K. Deve-se apresentar na saída de console um pedido em que o usuário errou o
# tamanho;
# L. Deve-se apresentar na saída de console um pedido com duas opções sabores
# diferentes e com tamanhos diferentes;
# A. Mensagem de boas-vindas com nome


print("Bem-vindo à Loja de Gelados do [G.S]")
print('• Tamanho P de Cupuaçu (CP) custa 9 reais e o Açaí (AC) custa 11 reais; • Tamanho M de Cupuaçu (CP) custa 14 reais e o Açaí (AC) custa 16 reais;• Tamanho G de Cupuaçu (CP) custa 18 reais e o Açaí (AC) custa 20 reais;')
# E. Acumulador para somar os valores dos pedidos
acumulador_vendas = 0

# G. Estrutura de repetição while
while True:
    # B. Input do sabor e validação
    sabor = input("\nEntre com o sabor desejado (CP/AC): ").upper().strip()
    
    if sabor != 'CP' and sabor != 'AC':
        print("Sabor Inválido. Tente novamente")
        continue  # G. Retorna para o início do laço se o sabor for inválido

    # C. Input do tamanho e validação
    tamanho = input("Entre com o tamanho desejado (P/M/G): ").upper().strip()
    
    if tamanho not in ['P', 'M', 'G']:
        print("Tamanho Inválido. Tente novamente")
        continue  # G. Retorna para o início do laço se o tamanho for inválido

    # D. Processamento usando modelo aninhado (If dentro de If)
    if sabor == 'CP':
        if tamanho == 'P':
            valor_pedido = 9
        elif tamanho == 'M':
            valor_pedido = 14
        else: # Tamanho G
            valor_pedido = 18
        print(f"Você pediu um Cupuaçu no tamanho {tamanho}: R$ {valor_pedido:.2f}")

    elif sabor == 'AC':
        if tamanho == 'P':
            valor_pedido = 11
        elif tamanho == 'M':
            valor_pedido = 16
        else: # Tamanho G
            valor_pedido = 20
        print(f"Você pediu um Açaí no tamanho {tamanho}: R$ {valor_pedido:.2f}")

    # E. Somando ao acumulador
    acumulador_vendas += valor_pedido

    # F. Pergunta se deseja continuar
    mais_alguma_coisa = input("\nDeseja pedir mais alguma coisa? (S/N): ").upper().strip()
    
    if mais_alguma_coisa == 'S':
        continue
    else:
        # F. Encerra o programa e exibe o total acumulado
        print(f"\nO valor total a ser pago: R$ {acumulador_vendas:.2f}")
        break  # G. Sai do laço while