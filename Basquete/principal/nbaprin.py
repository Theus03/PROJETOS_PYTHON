from EPYTHON.Basquete.cadastros.cadnba import *
from EPYTHON.Basquete.interface.menunba import *
from time import sleep

arq = 'NBA.txt'

if not ArquivoExiste(arq):
    CriarArquivos(arq)

while True:
    res = menu(['Ver Franquias Cadastradas', 'Cadastrar nova Franquia', 'Sair do Sistema'])
    if res == 1:
        #Opção de listar o conteúdo de um arquivo!
        LerArquivos(arq)
    elif res == 2:
        #Opção de Cadastrar uma nova franquia.
        cabeçalho('NOVA FRANQUIA')
        fran = str(input('Franquia:'))
        loc = str(input('Localiadade:'))
        cadastrar(arq, fran, loc)
    elif res == 3:
        #Opção de Sair do Sistema
        cabeçalho('Volte Sempre.......PORQUE A VIDA PRECISA DE EPYTHON!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
