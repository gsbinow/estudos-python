# EXERCÍCIO 1 – Conteúdos até Aula 3
# Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção
# de um app de vendas para uma determinada empresa X que vende em atacado. Uma das
# estratégias de vendas dessa empresa X é dar desconto maior conforme o valor da compra,
# conforme a listagem abaixo:os futuros chats."
# # Se valor_total for menor que 2500 o desconto será de 0%;
# # Se valor_total for maior ou igual que 2500 e menor que 6000 o desconto será de
# 4%;
# • Se valor_total for maior ou igual que 6000 e menor que 10000 o desconto será
# de 7%;
# • Se valor_total for maior ou igual que 10000 o desconto será de 11%;
# Elabore um programa em Python que:
# A. Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu
# nome e sobrenome (somente print, não usar input aqui);
# B. Deve-se implementar o input do valor unitário e da quantidade do produto;
# C. Deve-se implementar o desconto conforme a enunciado acima (obs.: atente-se
# as condições de menor, igual e maior;
# D. Deve-se implementar o valor total sem desconto e o valor total com desconto;
# E. Deve-se implementar as estruturas if, elif e else (todas elas);
# F. Deve-se inserir comentários relevantes no código;
# Teste seu código atendendo as seguintes exigências:
# G. Deve-se apresentar na saída de console uma mensagem de boas-vindas com seu
# nome e sobrenome;
# H. Deve-se apresentar na saída de console um pedido recebendo desconto (valor total
# sem desconto maior ou igual a 2500);
def divisoria():
    print('-' * 45)

# A. Boas-vindas
print("Bem-vindo ao Sistema de Vendas de G.S")
divisoria()

try:
    # B. Entrada de dados com conversão de tipos
    valor_unitario = float(input("Digite o valor do produto: "))
    quantidade = int(input("Digite a quantidade comprada: "))
    
    # Cálculo base
    total_bruto = valor_unitario * quantidade
    
    # C, E. Lógica de faixas de desconto (Hierarquia correta)
    if total_bruto < 2500:
        porcentagem = 0
    elif total_bruto < 6000:
        porcentagem = 4
    elif total_bruto < 10000:
        porcentagem = 7
    else:
        porcentagem = 11

    # D. Cálculos finais
    valor_desconto = total_bruto * (porcentagem / 100)
    total_com_desconto = total_bruto - valor_desconto

    # Saída de resultados formatada
    divisoria()
    print(f"Valor Total Bruto:    R$ {total_bruto:>10.2f}") #>10 para alinhamento
    print(f"Desconto aplicado:    {porcentagem:>10}%")
    print(f"Valor do Desconto:    R$ {valor_desconto:>10.2f}")
    print(f"Valor Total Líquido:  R$ {total_com_desconto:>10.2f}")
    divisoria()

except ValueError:
    print("Erro: Por favor, digite apenas números para valor e quantidade.")