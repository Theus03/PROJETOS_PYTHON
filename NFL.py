print('LEVANTAMENTO DE DADOS DOS JOGADORES DA NFL')
print('<>'*30)
Quaterbacks = ('Tom Brady', 'Aaron Rodgers',
               'Russel Wilson', 'Drew Bress',
               'Matt Ryan', 'Cam Newton',
               'Big Ben', 'Andrew Luck',
               'Philip Rivers', 'Carson Wentz')

dados = ('9 participações no SuperBolw', '6 títulos do SuperBolw',
         '4 vezes eleito MVP', '16 títulos de divisão')

dados1 = ('6 participações no SuperBowl', '1 título do SuperBolw',
          '2 vezes eleito MVP', '1 título de divisão')

dados2 = ('1 participação no SuperBolw', '1 título do SuperBolw',
          '0 vezes eleito MVP', '2 título de divisão')

dados3 = ('2 participações no SuperBolw', '1 título do SuperBolw',
          '1 vez eleito MVP', '3 títulos de divisão')

dados4 = ('1 participação no SuperBolw', '0 título do SuperBolw',
          '1 vez eleito MVP', '0 título de divisão')

dados5 = ('1 participação no SuperBolw', '0 título do SuperBolw',
          '1 vez eleito MVP', '2 títulos de divisão')

dados6 = ('2 participações no SuperBolw', '2 títulos do SuperBolw',
          '0 vezes eleito MVP', '0 título de divisão')

dados7 = ('0 participações no SuperBolw', '0 títulos do SuperBolw',
          '0 vezes eleito MVP', '1 título de divisão',
          '(Obs.APOSENTADO)')

dados8 = ('0 participação no SuperBolw', '0 títulos do SuperBolw',
          '0 vezes eleito MVP', '2 títulos de divisão')

dados9 = ('1 participação no SuperBolw', '1 título do SuperBolw',
          '0 vezes eleito MVP', '5 títulos de divisão')
jogador = dict()
games = list()
print('QUATERBACKS:')
for p in range(0, len(Quaterbacks)):
    print(f' - {Quaterbacks[p]:<30}')
while True:
    jogador.clear()
    print('<>' * 30)
    jogador["nome"] = str(input('Nome do Quaterback: '))
    for j in range(0, len(dados)):
        if jogador["nome"] == Quaterbacks[0]:
            print(f' - {dados[j]:<30}')
    for j in range(0, len(dados1)):
        if jogador["nome"] == Quaterbacks[1]:
            print(f' - {dados1[j]:<30}')
    for j in range(0, len(dados2)):
        if jogador["nome"] == Quaterbacks[2]:
            print(f' - {dados2[j]:<30}')
    for j in range(0, len(dados3)):
        if jogador["nome"] == Quaterbacks[3]:
            print(f' - {dados3[j]:<30}')
    for j in range(0, len(dados4)):
        if jogador["nome"] == Quaterbacks[4]:
            print(f' - {dados4[j]:<30}')
    for j in range(0, len(dados5)):
        if jogador["nome"] == Quaterbacks[5]:
            print(f' - {dados5[j]:<30}')
    for j in range(0, len(dados6)):
        if jogador["nome"] == Quaterbacks[6]:
            print(f' - {dados6[j]:<30}')
    for j in range(0, len(dados7)):
        if jogador["nome"] == Quaterbacks[7]:
            print(f' - {dados7[j]:<30}')
    for j in range(0, len(dados8)):
        if jogador["nome"] == Quaterbacks[8]:
            print(f' - {dados8[j]:<30}')
    for j in range(0, len(dados9)):
        if jogador["nome"] == Quaterbacks[9]:
            print(f' - {dados9[j]:<30}')
    while True:
        print('<>' * 30)
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('<<<VOLTE SEMPRE!>>>')
