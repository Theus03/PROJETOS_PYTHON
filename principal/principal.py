from time import sleep
from WALLET.interface.cor import c, c1
from WALLET.moedas.moeda import moedas, real1, real2, real3
from WALLET.moedas.moeda import dólar1, dólar2, dólar3
from WALLET.moedas.moeda import euro1, euro2, euro3
from WALLET.moedas.moeda import peso1, peso2, peso3
from WALLET.interface.linhas import lindinheiro, linworld
from WALLET.interface.menu import tit


lindinheiro()
tit(f'CONVERSOR DE MOEDAS - THEUS.PY', 7)
lindinheiro()

moedas()


sleep(2)

m = str(input('Qual ou quais moedas você tem em sua carteira?:'))
sleep(1)
con = str(input(f'Você irá converter o {m} para qual moeda:'))
linworld()
print(c1[6], end='')
print('{:^170}'.format('CARREGANDO........'))
print(c[0], end='')
sleep(3)

if m == 'Real' or 'real' or 'REAL' and con == 'Dólar' or 'dólar' or 'DÓLAR':
    linworld()
    real1()
if m == 'Real' or 'real' or 'REAL' and con == 'Euro' or 'euro' or 'EURO':
    real2()
if m == 'Real' or 'real' or 'REAL' and con == 'Peso' or 'peso' or 'PESO':
    real3()
if m == 'Dólar' or 'dólar' or 'DÓLAR' and con == 'Real' or 'real' or 'REAL':
    dólar1()
if m == 'Dólar' or 'dólar' or 'DÓLAR' and con == 'Euro' or 'euro' or 'EURO':
    dólar2()
if m == 'Dólar' or 'dólar' or 'DÓLAR' and con == 'Peso' or 'peso' or 'PESO':
    dólar3()
if m == 'Euro' or 'euro' or 'EURO' and con == 'Real' or 'real' or 'REAL':
    euro1()
if m == 'Euro' or 'euro' or 'EURO' and con == 'Dólar' or 'dólar' or 'DÓLAR':
    euro2()
if m == 'Euro' or 'euro' or 'EURO' and con == 'Peso' or 'peso' or 'PESO':
    euro3()
if m == 'Peso' or 'peso' or 'PESO' and con == 'Real' or 'real' or 'REAL':
    peso1()
if m == 'Peso' or 'peso' or 'PESO' and con == 'Dólar' or 'dólar' or 'DÓLAR':
    peso2()
if m == 'Peso' or 'peso' or 'PESO' and con == 'Euro' or 'euro' or 'EURO':
    peso3()
