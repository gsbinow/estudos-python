print("\n-----------Bem vindo a loja do Binow!------------\n")
print('-'*40)

# DADOS
valor_unitario = float(input("Digite o valor unitario: "))
# Removi o acento de 'unitário' na variável, pois nomes de variáveis 
# com acento podem causar erros em alguns ambientes de execução.

qnt_produto = int(input("Digite a quantidade do produto: "))

# Calculo 1
valor_total = valor_unitario * qnt_produto

if valor_total < 2500:
    porcentagem_desconto = 0.00 # 0% desconto
elif valor_total >= 2500 and valor_total < 6000:
    porcentagem_desconto = 0.04 # 4%
elif valor_total >= 6000 and valor_total < 10000:
    porcentagem_desconto = 0.07 # 7%
else:
    porcentagem_desconto = 0.11 # 11%

# Calculos finais (Agora fora do bloco if/else para rodar sempre)
valor_do_desconto = valor_total * porcentagem_desconto
valor_com_desconto = valor_total - valor_do_desconto

print("-" * 40)
print(f"Valor total sem desconto: R$ {valor_total:.2f}")
print(f"Desconto aplicado: {porcentagem_desconto * 100:.0f}% (R$ {valor_do_desconto:.2f})")
print(f"Valor total com desconto: R$ {valor_com_desconto:.2f}")

print('7+1'+'1')

print('Bem vindo')
tamnaho_p_cp= 9
tamnho_m_cp= 14
tamnho_g_cp= 18 