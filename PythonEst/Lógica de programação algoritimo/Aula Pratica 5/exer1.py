def div():
    """
Explicação da funcionamento da função:
DIvisão estetica

"""

    print('-'*40)

print('Ola, mUndo!', end='    ')
print('Ola, mUndo!')
div()
print('Ola, mUndo!', end='  \n  ')
print('Ola, mUndo!')
div()
print('Ola, mUndo!', end='\n')
print('Ola, mUndo!')

div()
help(div)

def exerc():
    while True:
        try:
            # 1. Tenta ler o número
            numero = int(input('Digite um numero inteiro: '))
            
            # Se chegou aqui, o número é válido. Podemos calcular:
            fatorial = 1
            for i in range(1, numero + 1):
                fatorial *= i
            
            print(f'O fatorial de {numero} é {fatorial}, Programa encerrado')
            
            # 2. Sai do loop após o cálculo bem-sucedido
            break 
            
        except ValueError:
            # Se houver erro na digitação, ele volta para o início do while
            print('Número inválido. Por favor, tente novamente!')

# Chama a função
exerc()