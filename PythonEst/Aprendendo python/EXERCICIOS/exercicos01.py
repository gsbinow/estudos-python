 # Exeercicios Lógica basica

#Exercício 1: Cálculo de Bônus de Vendas (RH/Vendas)

#Cenário: Uma empresa decidiu dar um bônus de 10% sobre o faturamento total para a equipe de vendas.
#  Objetivo: Calcule o valor do bônus e o faturamento final da empresa após subtrair esse bônus.

faturamento_inicial = 500000
percentual_bonus = 0.10
comissao = faturamento_inicial * percentual_bonus
faturamento = faturamento_inicial - comissao
print(f'\nA comissão do funcionário é R$ {comissao:,.2f}\n') #:,. 2f para pontuaçao dos numeros confrome as casas
print(f'\nO faturamento da empresa é R$ {faturamento:,.2f}\n')

print('='*40)

#Exercício 2: Controle de Estoque de E-commerce (Logística)

#Cenário: Um e-commerce começou o dia com 250 unidades de um smartphone no estoque. Durante o dia, 
#foram vendidos 78 unidades e chegaram mais 100 unidades de um fornecedor. Objetivo: Atualize a variável de estoque e exiba o saldo 

#dados
# começo do dia: 250 unidades de smartphone
#foram vendidas 78 e chegaram mais 100

estoque = 250 #smartphone 
entrada = 100 #smartphone
vendas = 78

estoque_final = estoque - vendas + entrada
print('\n[SALDO DO ESTOQUE:]\n')
print('-'*40)
print('\n[DADOS]\n')
print(f'Saldo inicial: {estoque} unidades')
print(f'Saida do estoque: {vendas}')
print(f'Entrada do estoque: {entrada}\n')
print('-'*40)
print(f'\nO estoque atual é {estoque_final:,.2f} unidades\n')

print('='*40)

#Exercício 3: Divisão de Cargas (Logística/Transporte)

#Cenário: Uma transportadora precisa levar 1.250 caixas em caminhões pequenos. Cada caminhão suporta exatamente 12 caixas.
# Objetivo: 
# 1. Quantos caminhões sairão totalmente cheios? (Use //) 
# 2. Quantas caixas sobrarão para serem enviadas em uma última viagem menor? (Use %)

print('\n[DADOS]\n')
carga_unidade = 1250
carga_p_caminhao = 12
transporte = carga_unidade // carga_p_caminhao
sobras = carga_unidade % carga_p_caminhao
print(f'A carga para transporte é {carga_unidade}')
print(f'Quantidade suportada é {carga_p_caminhao} unidades\n')
print(f'{transporte} sairão cheios e sobrarão {sobras} caixas\n')

print('='*40)

#Exercício 4: Análise de Margem de Lucro (Financeiro)

#Cenário: Uma consultoria faturou R$ 15.000,00 em um projeto. Os custos fixos foram de R$ 5.000,00 e o imposto sobre o faturamento é de 15%.
#  Objetivo: Calcule o imposto, o lucro líquido e a margem de lucro (Lucro / Faturamento).
#  No final, crie uma variável booleana chamada meta_atingida que verifica se a margem de lucro é superior a 0.30 (30%).

fatura = 15000
custo = 5000
taxa_imposto = 0.15

# 1. Calculando o valor do imposto (15% de 15.000)
valor_imposto = fatura * taxa_imposto

# 2. Calculando o Lucro Líquido (Fatura - Custos - Impostos)
lucro_liquido = fatura - custo - valor_imposto

# 3. Calculando a Margem de Lucro (Lucro / Faturamento)
margem_lucro = lucro_liquido / fatura

# 4. Verificando se a meta (30%) foi atingida
meta_atingida = margem_lucro > 0.30

print(f'Imposto Pago: R$ {valor_imposto:,.2f}')
print(f'Lucro Líquido: R$ {lucro_liquido:,.2f}')
print(f'Margem de Lucro: {margem_lucro:.2%}') # Formata como porcentagem
print(f'A meta de 30% foi atingida? {meta_atingida}')

print('='*40)

#exercício 5: Conversão de Tempo de Contrato (Gestão de Projetos)

#Cenário: Um contrato de manutenção de software tem a duração de 40 meses.
#  O cliente quer ver esse tempo no formato: "X anos e Y meses".
#  Objetivo: Utilize os operadores de divisão inteira e resto da divisão para converter os 40 meses.
tempo_manutencao = 40 #meses
anos = tempo_manutencao // 12 # meses
meses = tempo_manutencao % 12

print('[DADOS]\n')
print(f'Tempo de manutençao: {tempo_manutencao} meses')
print(f'A próxima manutenção deverá ser feita em {anos} anos e {meses} meses\n')
print('='*40)

#🏆 Desafio de Finalização de Nível 1:


#Cenário: A Loja de Peças

#Um cliente comprou 150 peças de um motor.

#Cada peça custa R$ 20,00.

#Você deve colocar essas peças em caixas que cabem 12 unidades.

#O cliente terá um desconto de 5% no valor total da compra.

#Seu desafio é exibir:

#Quantas caixas cheias serão enviadas e quantas peças sobram?

#Qual o valor total da compra (com o desconto)?

#Crie uma variável booleana que diga se a compra foi maior que R$ 2.500,00.


peças = 150
valor_peças = 20 # R$
capacidade_pacote = 12 # peças
desconto = 0.05
valor_desconto = valor_peças * desconto
valor_final= valor_peças - valor_desconto

compra = peças * valor_final
envio = 150 // 12 #quantidade de caixas com capacidade par a 12 peças
resto = 150 % 12
print('VENDA EFETUADA\n')

print(f'Solicitação: {peças} peças')
print(f'Valor unitário {valor_peças:,.2f}')
print('\n[DESCONTO APLICADO]\n')
print(f'Desconto aplicado {desconto}')
print(f'Valor individual com desconto {valor_desconto:,.2f}')
print(f'Fatura: {compra:,.2f}')
print('\n[TRANSPORTE]\n')
print(f'Quantia de caixas: {envio}')
print(f'Peças restantes: {resto}\n')
meta= compra > 2500
print('Meta da venda: 2.500,00')
print(f'O resultado da meta foi: {meta}')