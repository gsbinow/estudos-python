# Requisito A e H: Mensagem de boas-vindas com Nome e Sobrenome
print("Bem-vindo a Copiadora do [SEU NOME E SOBRENOME AQUI]")

# Requisito B: Função escolha_servico()
def escolha_servico():
    while True:
        # Requisito B.a: Pergunta o serviço
        servico = input("Entre com o tipo de serviço desejado\n"
                        "dig - Digitação\n"
                        "ico - Impressão Colorida\n"
                        "ipb - Impressão Preto e Branco\n"
                        "fot - Fotocópia\n"
                        ">> ").lower().strip()
        
        # Requisito B.b: Retorna o valor do serviço
        if servico == 'dig':
            return 1.10
        elif servico == 'ico':
            return 1.00
        elif servico == 'ipb':
            return 0.40
        elif servico == 'fot':
            return 0.20
        else:
            # Requisito B.c e I: Repete a pergunta se errar a opção
            print("Escolha inválida, entre com o tipo do serviço novamente.")
            continue

# Requisito C: Função num_pagina()
def num_pagina():
    while True:
        try:
            # Requisito C.a: Pergunta o número
            paginas = int(input("Entre com o número de páginas: "))
            
            # Requisito C.c e J: Repete se ultrapassar 20000
            if paginas >= 20000:
                print("Não aceitamos tantas páginas de uma vez.")
                print("Por favor, entre com o número de páginas novamente.")
                continue
            
            # Requisito C.b: Calcula o desconto em cima do número de páginas
            if paginas < 20:
                desconto = 0
            elif paginas < 200:
                desconto = 0.15 # 15%
            elif paginas < 2000:
                desconto = 0.20 # 20%
            else: # Entre 2000 e 19999
                desconto = 0.25 # 25%
            
            # Retorna o valor das páginas já com o desconto aplicado
            return paginas * (1 - desconto)
            
        except ValueError:
            # Requisito F: Uso do try/except para não numérico
            print("Por favor, entre com um valor numérico válido.")

# Requisito D: Função servico_extra()
def servico_extra():
    while True:
        try:
            # Requisito D.a: Pergunta pelo serviço adicional
            extra = int(input("Deseja adicionar algum serviço extra?\n"
                              "1 - Encadernação Simples - R$ 15.00\n"
                              "2 - Encadernação Capa Dura - R$ 40.00\n"
                              "0 - Não desejo mais nada\n"
                              ">> "))
            
            # Requisito D.b: Retorna o valor do adicional
            if extra == 1:
                return 15.00
            elif extra == 2:
                return 40.00
            elif extra == 0:
                return 0.00
            else:
                # Requisito D.c: Repetir se digitar opção diferente
                print("Opção inválida. Digite 1, 2 ou 0.")
        except ValueError:
            print("Por favor, digite um número válido.")

# --- CÓDIGO PRINCIPAL (MAIN) ---

# Requisito E: Implementar o total a pagar no código principal
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
