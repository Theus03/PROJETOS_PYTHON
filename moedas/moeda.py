from time import sleep
from WALLET.interface.cor import c, c1
from WALLET.interface.linhas import airplane

def moedas():
    print(' -> MOEDAS:')
    print('''
    - REAL
    - DÓLAR
    - EURO
    - PESO''')


def real1():
    print(c1[6], end='')
    print('Boa escolha você ira converter o real para o dólar e poderá viajar para os Estados Unidos com nossa ajuda!')
    print(c[0], end='')
    reais = float(input('Quantos reais vc tem em sua carteira?:'))
    sleep(2)
    dólar = reais/4.07
    airplane()
    print(c1[6], end='')
    print(f'Com {reais:.2f} reais, você poderá comprar {dólar:.2f} dólares')
    airplane()
def real2():
    print(c1[6], end='')
    print('Ótima escolha iremos converter o real para o euro!')
    print(c[0], end='')
    reais = float(input('Quantos reais você tem em sua carteira?:'))
    sleep(2)
    euro = reais/4.52
    airplane()
    print(c1[6], end='')
    print(f'Com {reais:.2f} reais, você poderá comprar {euro:.2f} euros')
    airplane()
def real3():
    print(c1[6], end='')
    print('Vamos converter o real para o peso!')
    print(c[0], end='')
    reais = float(input('Quantos reais você tem em sua carteira?:'))
    sleep(2)
    peso = reais/14.72
    airplane()
    print(c1[6], end='')
    print(f'Com {reais:.2f} reais, você pode comprar {peso:.2f} com o peso')
    airplane()
def dólar1():
    print(c1[6], end='')
    print('Vamos converter o dólar para o real, e você vai conseguir trocar seu dinheiro!')
    print(c[0], end='')
    dólares = float(input('Quantos dólares você tem em sua carteira?:'))
    sleep(2)
    real = dólares * 4.07
    airplane()
    print(c1[6], end='')
    print(f'Com {dólares:.2f} dólares, você vai conseguir comprar {real:.2f} reais.')
    airplane()
def dólar2():
    print(c1[6], end='')
    print('Ótima escolha iremos converter sua moeda e com nossa ajuda você viajará para a Europa!')
    print(c[0], end='')
    dólares = float(input('Quantos dólares você tem em sua carteira?:'))
    sleep(2)
    euro = dólares * 0.9030
    airplane()
    print(c1[6], end='')
    print(f'Com {dólares:.2f} dólares, você vai conseguir comprar {euro:.2f} euros.')
    airplane()
def dólar3():
    print(c1[6], end='')
    print('OK! Vamos converter seus dólares para o peso.')
    print(c[0], end='')
    dólares = float(input('Quantos dólares você tem em sua carteira?:'))
    sleep(2)
    peso = dólares * 59.820
    airplane()
    print(c1[6], end='')
    print(f'Com {dólares:.2f} dólares, você vai conseguir comprar {peso:.2f} pesos.')
    airplane()
def euro1():
    print(c1[6], end='')
    print('Vamos converter o Euro para o Real.')
    print(c[0], end='')
    euros = float(input('Quantos euros você tem em sua carteira?:'))
    sleep(2)
    real = euros * 4.52
    airplane()
    print(c1[6], end='')
    print(f'Com {euros:.2f} euros, você pode comprar {real:.2f} reais.')
    airplane()
def euro2():
    print(c1[6], end='')
    print('Ótima escolha, iremos converter a sua moeda para o Dólar!')
    print(c[0], end='')
    euros = float(input('Quantos euros você tem em sua carteira?:'))
    sleep(2)
    dólar = euros * 1.10
    airplane()
    print(c1[6], end='')
    print(f'Com {euros:.2f} euros, você vai conseguir comprar {dólar:.2f} dólares.')
    airplane()
def euro3():
    print(c1[6], end='')
    print('Iremos converter seus euros para o peso.')
    print(c[0], end='')
    euros = float(input('Quantos euros você tem em sua carteira?:'))
    sleep(2)
    peso = euros * 66.22
    airplane()
    print(c1[6], end='')
    print(f'Com {euros:.2f} euros, você irá comprar {peso:.2f} peso.')
    airplane()
def peso1():
    print(c1[6], end='')
    print('Ok! Iremos coverter seus pesos para o Real e você irá conseguir viajar ao Brasil com nossa ajuda!')
    print(c[0], end='')
    pesos = float(input('Quantos pesos você tem em sua carteira?:'))
    sleep(2)
    real = pesos/14.60
    airplane()
    print(c1[6], end='')
    print(f'Com {pesos:.2f} pesos argentinos, você irá conseguir comprar {real:.2f} reais.')
    airplane()
def peso2():
    print(c1[6], end='')
    print('Vamos converter o Peso para o Dólar.')
    print(c[0], end='')
    pesos = float(input('Quantos pesos você tem em sua carteira?:'))
    sleep(2)
    dólar = pesos/59.820
    airplane()
    print(c1[6], end='')
    print(f'Com {pesos:.2f} pesos argentinos, você irá conseguir comprar {dólar:.2f} dólares.')
    airplane()
def peso3():
    print(c1[6], end='')
    print('Ótima escolha! Iremos converter sua moeda para o Euro.')
    print(c[0], end='')
    pesos = float(input('Quantos pesos você tem em sua carteira?:'))
    sleep(2)
    euro = pesos/66.220
    airplane()
    print(c1[6], end='')
    print(f'Com {pesos:.2f} pesos argentinos, você vai conseguir comprar {euro:.2f} euros.')
    airplane()
