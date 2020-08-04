from EPYTHON.NFL.interface.nflmenu import *


def ArquivoExiste(Time):
    try:
        a = open(Time, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def CriarArquivos(Time):
    try:
        a = open(Time, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação de arquivos!')
    else:
        print(f'Arquivo {Time} criado com sucesso!')


def LerArquivos(Time):
    try:
        a = open(Time, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        cabeçalho('TIMES E JOGADORES CADASTRADOS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            dado[2] = dado[2].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:<30}{dado[2]:>3}')


def Cadastrar(arq, Time='desconhecido', Jogador='desconhecido', SB = 0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{Time}; {Jogador}; {SB}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print('Novo Registro adicionado.')
            a.close()
