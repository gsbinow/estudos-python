import re
import time

# 1. Base de "Tradução" (Atualize com os nomes reais do seu sistema)
dicionario_produtos = {
    "bom ar": "purificador de ambiente em aerossol",
    "desinfetante": "desinfetante liquido uso geral 5L",
    "pó de café": "cafe torrado e moido 500g",
    "esponja": "esponja de limpeza dupla face",
    "álcool em gel": "alcool etilico em gel 70%",
    "pacote papel higiênico": "papel higienico folha dupla",
    "pacote de açúcar": "acucar cristal 1kg",
    "vassoura": "vassoura de pelo com cabo",
    "pacote de folha a4": "papel sulfite a4 resma",
    "fita transparente da larga": "fita adesiva transparente larga 45x50",
    "bombriu": "esponja de la de aco"
}

texto_email = """
03 bom ar;
04 desinfetante;
06 pó de café;
02 esponja;
01 álcool em gel;
04 pacote papel higiênico;
01 pacote de açúcar;
01 vassoura;
04 pacote de folha A4;
03 fita transparente da larga.
"""

# 2. Processamento: Lendo o texto e criando a variável
lista_pedidos_final = []

# Regex: (\d+) pega os números, \s+ ignora os espaços, (.+?) pega o nome do item, [;.] para no ; ou .
padrao_busca = re.compile(r'(\d+)\s+(.+?)[;.]')

# Colocamos o texto em minúsculo (.lower()) para facilitar a busca no dicionário
itens_encontrados = padrao_busca.findall(texto_email.lower())

for quantidade, nome_popular in itens_encontrados:
    nome_popular = nome_popular.strip() # Remove espaços extras no início e fim
    
    # O método .get() busca o nome oficial. Se não achar, ele mantém o nome popular.
    nome_oficial = dicionario_produtos.get(nome_popular, nome_popular)
    
    # Adicionamos os dados estruturados na nossa variável principal
    lista_pedidos_final.append({
        "quantidade": int(quantidade),
        "produto": nome_oficial
    })

# --- FIM DO PROCESSAMENTO ---
# A variável 'lista_pedidos_final' agora contém algo assim:
# [{'quantidade': 3, 'produto': 'purificador de ambiente em aerossol'}, {'quantidade': 4, 'produto': 'desinfetante liquido uso geral 5L'}, ...]


# 3. Integração com a Automação Web (Exemplo do fluxo principal)
def preencher_sistema():
    for item in lista_pedidos_final:
        produto = item['produto']
        qtd = item['quantidade']
        
        print(f"-> Inserindo no sistema: {qtd}x {produto}")
        
        # AQUI ENTRA O SEU CÓDIGO SELENIUM:
        # 1. driver.find_element(By.ID, "campo_busca").send_keys(produto)
        # 2. driver.find_element(By.ID, "campo_quantidade").send_keys(qtd)
        # 3. driver.find_element(By.ID, "botao_adicionar").click()
        
        # O programa espera o sistema carregar o item na lista da tela
        time.sleep(2) # Ou melhor ainda: usar WebDriverWait para o elemento aparecer
        
        # O loop recomeça e parte para o próximo item