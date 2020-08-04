from time import sleep
from WALLET.interface.cor import c, c1


def tit(msg, cor=0):
    tam = len(msg) + 160
    print(c1[cor], end='')
    print('=' * tam)
    print('{:^170}'.format(msg))
    print('=' * tam)
    print(c[0], end='')
