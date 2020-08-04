from EPYTHON.Basquete.interface.menunba import *


def ArquivoExiste(franquia):
    try:
        a = open(franquia, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def CriarArquivos(franquia):
    try:
        a = open(franquia, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação de arquivos!')
    else:
        print(f'Arquivo {franquia} criado com sucesso!')


def LerArquivos(franquia):
    try:
        a = open(franquia, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        cabeçalho('FRANQUIAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3}')


def cadastrar(arq, franquia='desconhecido', localidade='desconhecido'):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{franquia};{localidade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo Registro de {franquia} adicionado.')
            a.close()
