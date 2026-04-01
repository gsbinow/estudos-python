#Boiolagens
def bordas(b1):
    tam = len(b1)
    print('+', '='*tam, '+')
    print('|', b1, '|')
    print('+', '='*tam, '+')

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x<min) or (x>max)):
        x = int(input(pergunta))
        return x

def div():
    print('-'*40)

#Manipulação de arquivos:
def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
      return False
    else:
        return True

def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
      print('erro na criação')
    else:
        print(f'Arquivo criado com sucesso')


arquivo = 'gemes.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente')
    criarArquivo(arquivo)

def cadastrarJogo(nomeArquivo, nomeDoJogo, nomeGame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('erro ao abrir o arquivo')
    else:
        a.write(f'{nomeDoJogo}; {nomeGame}\n')
    finally:
        a.close()


def ListarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(a.read())
    finally:
        a.close()


#programa princiapl
while True:
    bordas('Bem vindo ao |MENU|!')

    print('Selecione uma das opções')
    div()
    input('|(1) Cadastrar novo item| (2) Listar os cadastros| (3) Sair |') 
    div()
    if '1' or 'Cadastrar novo item':
        print('Cadastrando...')
        nomeDoJogo = input('Nome do jogo:')
        nomeGame = input('Nome do videogame:')
        cadastrarJogo(arquivo, nomeDoJogo, nomeGame)
    elif '2' or 'Listar os cadastros':
        print('Listando...')
        ListarArquivo(arquivo)
    elif '31' or 'Sair':
        print('Encerrando...')
        break

