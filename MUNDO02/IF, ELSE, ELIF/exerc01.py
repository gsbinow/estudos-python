#Exercício 1: Validação de Investimento (Setor Financeiro) Uma corretora de valores quer automatizar a recomendação básica de perfil. Crie um programa que peça ao usuário o valor que ele deseja investir.
#Se o valor for menor que R$ 1.000,00, exiba: "Perfil iniciante: Sugerimos Tesouro Direto".
#Se o valor for entre R$ 1.000,00 e R$ 5.000,00 (inclusive), exiba: "Perfil moderado: Sugerimos Fundos Imobiliários".
#Se o valor for acima de R$ 5.000,00, exiba: "Perfil arrojado: Sugerimos Ações". *Lembre-se de tratar o input caso o usuário digite "R$" ou use vírgula.*

print('Bem-vindo ao [SETOR FINANCEIRO], sua calculadora de investimentos! ;)')

# 1. Tratamento do Input
entrada = input('Por favor, insira o valor a ser investido: ')

# Remove "R$", espaços e troca a vírgula decimal por ponto
entrada_limpa = entrada.replace('R$', '').replace(' ', '').replace(',', '.')
valor = float(entrada_limpa)

print(f'Capital investido: R$ {valor:.2f}\n')

# 2. Estrutura de Decisão
if valor < 1000:
    print("Perfil iniciante: Sugerimos Tesouro Direto")

elif 1000 <= valor <= 5000:
    # Esta sintaxe acima é o mesmo que: valor >= 1000 and valor <= 5000
    print("Perfil moderado: Sugerimos Fundos Imobiliários")

else:
    # Se não é menor que 1000 nem está entre 1000 e 5000, só pode ser acima de 5000
    print("Perfil arrojado: Sugerimos Ações") 

#--------------------------------------------------

