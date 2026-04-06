lista_de_nomes = ['Mara','Julia','Puta','Lula','Jura','Cunha'] # Lista de nomes 
print(lista_de_nomes)

#Mostrar o tamanho da lista
print(len(lista_de_nomes)) #Ler lista

# Pegar um item da lista

primeiro = lista_de_nomes[0] # A contagem começa com [0]
segundo = lista_de_nomes[1]
terceiro = lista_de_nomes[2]
quarto = lista_de_nomes[3]
quinto= lista_de_nomes[4]
print(primeiro)
print(segundo)
print(terceiro)
print(quarto)
print(quinto)

#Encontrar na lista
Existe_na_lista = "Puta" in lista_de_nomes
print(Existe_na_lista) #Verdaderio e falso

posição_lista = lista_de_nomes.index('Puta') 
print(posição_lista)

# Exemplo com numeros:
lista_vendas = [1000 , 100 , 10 ,1 ,5000]

# Total
total_vendas = sum(lista_vendas) #sum é para somar
print(total_vendas)

# Maior valor
maior_valor = max(lista_vendas)

# Menor valor
menor_valor = min(lista_vendas)

#Média 
media = total_vendas / len(lista_vendas)

print(maior_valor)
print(menor_valor)
print(media)
#-------------------------------------
#Adicionar um elemento na lista 

lista_vendas.append(600) #append é para adicionar um elemento da lista

# Remover um elemento
lista_vendas.remove(1)
print(lista_vendas)

#-------------------------------------------------------------------
# Juntar listas
novos_nomes = ['Paola']
lista_de_nomes.extend(novos_nomes)#extended junta duas listas existentes sem erro

#------------------------------------------------------------------
# Ordenar lista
lista_vendas.sort()#ORdem crescente
lista_vendas.sort(reverse=True) #Ordem decrescente
print(lista_vendas)