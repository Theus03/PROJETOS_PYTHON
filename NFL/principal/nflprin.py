from EPYTHON.NFL.cadastros.nlfcad import *
from EPYTHON.NFL.interface.nflmenu import *
from time import sleep

arq = 'NFL.txt'

if not ArquivoExiste(arq):
    CriarArquivos(arq)


while True:
    res = menu(['Ver Times cadastrados no EPYTHON', 'Cadastar novos regitros de jogadores e times', 'Sair do Sistema'])
    if res == 1:
        #Opção de ver times e registros dos jogadores cadastrados
        LerArquivos(arq)
    elif res == 2:
        #Opção de cadastro
        cabeçalho('NOVO REGISTRO')
        time = str(input('Time:'))
        jog = str(input('Jogador:'))
        sb = int(input('Quantos SuperBolw participou:'))
        Cadastrar(arq, time, jog, sb)
    elif res == 3:
        #Sair do Sistema
        cabeçalho('Volte Sempre.......PORQUE A VIDA PRECISA DE EPYTHON!')
        break
    else:
        print('\033[31mDigite uma opção válida!\033[m')
    sleep(2)
