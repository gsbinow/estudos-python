#Exercício 1: Dashboard de Vendas (Análise de Dados) Você recebeu uma lista com as vendas diárias de uma equipe: vendas = [1500, 2000, 800, 3500, 1200]. Crie um programa que exiba um pequeno relatório contendo:

 #O total de vendas na semana.
#A média de vendas diária.
#O valor da melhor venda e da pior venda do período.

vendas= [1500, 2000, 800, 3500, 1200]
print(vendas)
vendas_total = sum(vendas)
print(f'A soma das vendas equivale á: R${vendas_total}')
vendas_maximas = max(vendas)
vendas_minimas = min(vendas)
vendas_medias = vendas_total / len(vendas)
print(f'O valor médio das vendas é de R${vendas_medias}')
print(f'O melhor valor de vendas doi de R${vendas_maximas} e o pior foi R${vendas_minimas}')


#Exercício 2: Gestão de Estoque (Edição e Verificação) Uma loja de eletrônicos possui os seguintes produtos: estoque = ["monitor", "teclado", "mouse", "headset"]. O gerente pediu para:

#Adicionar o item "webcam" ao final da lista.

#O "teclado" teve seu nome atualizado para "teclado mecanico". Faça essa alteração na lista.

#Verificar se "impressora" está no estoque. O programa deve exibir True ou False.

#Remover o "mouse" da lista, pois saiu de linha
print('-'*40)
estoque = ["monitor", "teclado", "mouse", "headset"]
print(f'Antiga lista{estoque}')
#Adicionando a webcam
estoque.append("webcam")
#removendo teclado e adicionando teclado mecanico
estoque.remove('teclado')
estoque.append('teclado mecanico')
#verificando se eixste impressora.
existe = "impressora" in estoque
#tirando mouse
estoque.remove("mouse")
print(existe)
print(f'Nova lista{estoque}')

#Exercício 3: Organização de Preços (Ordenação e Slicing) Uma importadora listou os preços de frete em dólar: fretes = [50, 80, 20, 150, 40]. Para apresentar em uma reunião, você deve:

#Ordenar a lista do maior para o menor preço.

#Pegar os 2 fretes mais caros (usando fatiamento/slicing) e armazenar em uma nova lista chamada top_fretes.

#Exibir a lista original ordenada e a lista dos top_fretes
print('-'*40)
fretes = [50, 80, 20, 150, 40]
print(fretes)
fretes.sort(reverse=True)
print(fretes)

top_fretes = fretes[:2]

print(f"Lista ordenada (maior para o menor): {fretes}")
print(f"Top 2 fretes mais caros: {top_fretes}")