from EPYTHON.Futebol.Interface.menuepython import *


def arquivoexiste(time):
    try:
        a = open(time, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def CriaCadastros(time):
    try:
        a = open(time, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na Criação dos cadastros')
    else:
        print(f'Cadastro {time} criado com sucesso!')


def LerCadastros(time):
    try:
        a = open(time, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        Cabeçalho('TIMES E-PYTHON')
        for linha in a:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<20}{dados[1]:<2}')
    finally:
        a.close()


def Cadastrar(arq, time='Desconhecido', jogador='desconhecido'):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{time}; {jogador};\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo Cadastro do {time} adicionado.')
            a.close()
