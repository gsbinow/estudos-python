def teste1():
    dados = dict() #abrir o dicionario
    dados = { 'nome': 'Pedro', 'idade': 26}
    print(dados['nome'])
    print(dados['idade'])
    dados['sexo'] = 'M' # para adicionar elementos
    del dados ['idade'] #wliminar do dicionario

def teste2 ():
    filme = {'tiulo': 'star wars',
              'ano': 'não sei',
              'diretor':   'Tambem não sei'



    }
    print(filme.values())#todos os valores do dicionario:
    print(filme.keys()) #exibir os titulos de cada setor isolado
    print(filme.items()) #exibir tudo, valores e titulos


    for k,v in filme.items():
        print(f'o {k} é {v}')


def teste3():
    pessoas = {'nome':'Guilherme', 'idade':'21', 'sexo':'m'}
    print(pessoas)
    print(pessoas['nome'])
    print(pessoas['idade'])

    pessoas['nome'] =   'Leandro'

    pessoas['peso'] = 75

    print(pessoas.keys())
    print('-'*40)
    print(pessoas.items())





def teste4():
    aluno = {}
    matricula = []
    aluno['nome'] = input(' Digite seu nome: ')
    aluno['idade'] = input(' Digite sua idade: ')
    matricula.append(aluno)
    print(matricula)
teste4()