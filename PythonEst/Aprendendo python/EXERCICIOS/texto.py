# [DADOS]

faturamento= 1000
lucro= 500

 # formas de escrita:

print('O faturamento foi de ', faturamento , 'e o lucro foi de' , lucro)
mensagem = 'O faturamento foi de ' + str(faturamento) +  'e o lucro foi de' + str(lucro)
print(mensagem)

 #formas de escrita2:

print(f'O faturamento foi d {faturamento} e o lucro de {lucro}')
str(print('O lucro foi de', lucro , 'e o faturamento de' , faturamento))

 #forma de escrita3:

mensagem2= f'O faturamento foi d R${faturamento} e o lucro de R${lucro}'
print(mensagem2) 

#===========================================

# formulas e funçoes de texto
  
  #formatação

email = "EMAIL_FALSO@gmail.com"
email = email.lower() #RECONHECER em letra minuscula
email = email.upper() #Reconhecer em letra maiusucula

  # Tamanho do texto
tamanho_do_texto = len(email) # ver quantia de carcteries
print(email)
print(tamanho_do_texto)

#Tamanho do texto
tamanho_do_texto = len(mensagem) #Quantidade e caracteries
print(tamanho_do_texto)

#Procurar dentro de um texto
posição=email.find("@") #Exibir a posição de determinada seleção
print(posição)


#PRocurar trexo do texto
posição_texto= email[0:posição]#[posição_inicial:posição_final] = onde começa e onde termina a exibição
print(posição_texto)

# Alteração no texto:
email = email.lower()
email = email.replace("gmail.com","yahoo.com" ) # [Trocar esse, por esse]
print(email)

#title, capitalize, upper
nome = "guilherme soares binow"
print(nome.title()) # Todas as iniciais em letra maiuscula
print(nome.capitalize()) # A primeira inicial em letra maiucusula
print(nome.upper()) # O texto em maiucusulo

nome = input('Difite seu nome: ').lower().strip()
print(f'Bem vindo, {nome.title()}')