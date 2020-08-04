from EPYTHON.Futebol.cadastros.cadastroepython import *
from EPYTHON.Futebol.Interface.menuepython import *
from time import sleep

arq = 'epython.txt'

if not arquivoexiste(arq):
    CriaCadastros(arq)

while True:
    res = menu(['Cadastre-se no FUTEPYTHON', 'Ver times e jogadores cadastrados', 'Sair do EPYTHON'])
    if res == 1:
        #Opção de cadastrar um novo time.
        Cabeçalho('NOVO CADASTRO')
        time = str(input('Time:'))
        jogador = str(input(f'Qual seu jogador favorito do {time}:'))
        Cadastrar(arq, time, jogador)
    if res == 2:
        # Opção de mostrar times e jogadores favoritos
        LerCadastros(arq)
    if res == 3:
        #Opção de Sair do Programa
        Cabeçalho('Volte Sempre! PORQUE A VIDA PRECISA DE EPYHTON')
        break
    sleep(2)
