Gol = ('De Gea', 91, 'Manchester United',
       'Neuer', 90, 'Bayer de Munique',
       'Courtois', 90, 'Real Madrid',
       'Oblak', 90, 'Atlético de Madrid',
       'Ter Stegen', 89, 'Barcelona')
print('='*90)
print(f'\033[1m{"TOP 5 MELHORES JOGADORES DE CADA POSIÇÃO - FIFA 19":^90}')
print('='*90)
print('GOLEIROS:')
for pos in range(0, len(Gol)):
    if pos == 0:
        print(f'\033[0;31m 1 - {Gol[pos]:.<30}', end='')
        print(f' Over {Gol [1]:.<30}', end='')
        print(f' Time = {Gol[2]:>3}')
    if pos == 3:
        print(f'\033[0;37m 2 - {Gol[pos]:.<30}', end='')
        print(f' Over {Gol [4]:.<30}', end='')
        print(f' Time = {Gol[5]:>3}')
    if pos == 6:
        print(f'\033[0;30m 3 - {Gol[pos]:.<30}', end='')
        print(f' Over {Gol[7]:.<30}', end='')
        print(f' Time =  {Gol[8]:>3}')
    if pos == 9:
        print(f'\033[0;33m 4 - {Gol[pos]:.<30}', end='')
        print(f' Over {Gol[10]:.<30}', end='')
        print(f' Time = {Gol[11]:>3}')
    if pos == 12:
        print(f'\033[0;34m 5 - {Gol[pos]:.<30}', end='')
        print(f' Over {Gol[13]:.<30}', end='')
        print(f' Time = {Gol[14]:>3}')

Zag = ('Sérgio Ramos', 91, 'Real Madrid',
       'Godín', 90, 'Atlético de Madrid',
       'Chiellini', 89, 'Juventus',
       'Hummels', 89, 'Bayer de Munique',
       'Thiago Silva', 88, 'PSG')
print(f'\033[1;30m ~'*90)
print('ZAGUEIROS:')
for pos in range(0, len(Zag)):
    if pos == 0:
        print(f'\033[0;30m 1 - {Zag[pos]:.<30}', end='')
        print(f' Over {Zag[1]:.<30}', end='')
        print(f' Time = {Zag[2]:>3}')
    if pos == 3:
        print(f'\033[0;33m 2 - {Zag[pos]:.<30}', end='')
        print(f' Over {Zag[4]:.<30}', end='')
        print(f' Time = {Zag[5]:>3}')
    if pos == 6:
        print(f'\033[0;32m 3 - {Zag[pos]:.<30}', end='')
        print(f' Over {Zag[7]:.<30}', end='')
        print(f' Time = {Zag[8]:>3}')
    if pos == 9:
        print(f'\033[0;37m 4 - {Zag[pos]:.<30}', end='')
        print(f' Over {Zag[10]:.<30}', end='')
        print(f' Time = {Zag[11]:>3}')
    if pos == 12:
        print(f'\033[0;35m 5 - {Zag[pos]:.<30}', end='')
        print(f' Over {Zag[13]:.<30}', end='')
        print(f' Time = {Zag[14]:>3}')

Lat = ('Marcelo', 88, 'Real Madrid',
       'Jordi Alba', 87, 'Barcelona',
       'Alex Sandro', 86, 'Juventus',
       'Alaba', 85, 'Bayer de Munique',
       'Filipe Luís', 85, 'Atlético de Madrid')
print(f'\033[1;30m ~'*90)
print('LATERAIS:')
for pos in range(0, len(Lat)):
    if pos == 0:
        print(f'\033[0;30m 1 - {Lat[pos]:.<30}', end='')
        print(f' Over {Lat[1]:.<30}', end='')
        print(f' Time = {Lat[2]:>3}')
    if pos == 3:
        print(f'\033[0;34m 2 - {Lat[pos]:.<30}', end='')
        print(f' Over {Lat[4]:.<30}', end='')
        print(f' Time = {Lat[5]:>3}')
    if pos == 6:
        print(f'\033[0;32m 3 - {Lat[pos]:.<30}', end='')
        print(f' Over {Lat[7]:.<30}', end='')
        print(f' Time = {Lat[8]:>3}')
    if pos == 9:
        print(f'\033[0;37m 4 - {Lat[pos]:.<30}', end='')
        print(f' Over {Lat[10]:.<30}', end='')
        print(f' Time = {Lat[11]:>3}')
    if pos == 12:
        print(f'\033[0;33m 5 - {Lat[pos]:.<30}', end='')
        print(f' Over {Lat[13]:.<30}', end='')
        print(f' Time = {Lat[14]:>3}')

Vol = ('Kanté', 89, 'Chelsea',
       'Sérgio Busquets', 88, 'Barcelona',
       'Casemiro', 88, 'Real Madrid',
       'Fernandinho', 86, 'Manchester City',
       'Matic', 86, 'Manchester United')
print(f'\033[1;30m ~'*90)
print('VOLANTES:')
for pos in range(0, len(Vol)):
    if pos == 0:
        print(f'\033[0;33m 1 - {Vol[pos]:.<30}', end='')
        print(f' Over {Vol[1]:.<30}', end='')
        print(f' Time = {Vol[2]:>3}')
    if pos == 3:
        print(f'\033[0;34m 2 - {Vol[pos]:.<30}', end='')
        print(f' Over {Vol[4]:.<30}', end='')
        print(f' Time = {Vol[5]:>3}')
    if pos == 6:
        print(f'\033[0;30m 3 - {Vol[pos]:.<30}', end='')
        print(f' Over {Vol[7]:.<30}', end='')
        print(f' Time = {Vol[8]:>3}')
    if pos == 9:
        print(f'\033[0;36m 4 - {Vol[pos]:.<30}', end='')
        print(f' Over {Vol[10]:.<30}', end='')
        print(f' Time = {Vol[11]:>3}')
    if pos == 12:
        print(f'\033[0;31m 5 - {Vol[pos]:.<30}', end='')
        print(f' Over {Vol[13]:.<30}', end='')
        print(f' Time = {Vol[14]:>3}')

Mei = ('Modric', 91, 'Real Madrid',
       'De Bruyne', 91, 'Manchester Ctiy',
       'Toni Kroos', 90, ' Real Madrid',
       'Dybala', 89, 'Juventus',
       'David Silva', 89, 'Manchester City')
print(f'\033[1;30m ~'*90)
print('MEIAS:')
for pos in range(0, len(Mei)):
    if pos == 0:
        print(f'\033[0;30m 1 - {Mei[pos]:.<30}', end='')
        print(f' Over {Mei[1]:.<30}', end='')
        print(f' Time = {Mei[2]:>3}')
    if pos == 3:
        print(f'\033[0;36m 2 - {Mei[pos]:.<30}', end='')
        print(f' Over {Mei[4]:.<30}', end='')
        print(f' Time = {Mei[5]:>3}')
    if pos == 6:
        print(f'\033[0;30m 3 - {Mei[pos]:.<30}', end='')
        print(f' Over {Mei[7]:.<30}', end='')
        print(f' Time = {Mei[8]:>3}')
    if pos == 9:
        print(f'\033[0;32m 4 - {Mei[pos]:.<30}', end='')
        print(f' Over {Mei[10]:.<30}', end='')
        print(f' Time = {Mei[11]:>3}')
    if pos == 12:
        print(f'\033[0;36m 5 - {Mei[pos]:.<30}', end='')
        print(f' Over {Mei[13]:.<30}', end='')
        print(f' Time = {Mei[14]:>3}')
Pon = ('Neymar', 92, 'PSG',
       'Hazard', 91, 'Chelsea',
       'Salah', 88, 'Liverpool',
       'Coutinho', 88, 'Barcelona',
       'Bale', 88, 'Real Madrid')
print(f'\033[1;30m ~'*90)
print('PONTAS:')
for pos in range(0, len(Pon)):
    if pos == 0:
        print(f'\033[0;35m 1 - {Pon[pos]:.<30}', end='')
        print(f' Over {Pon[1]:.<30}', end='')
        print(f' Time = {Pon[2]:>3}')
    if pos == 3:
        print(f'\033[0;33m 2 - {Pon[pos]:.<30}', end='')
        print(f' Over {Pon[4]:.<30}', end='')
        print(f' Time = {Pon[5]:>3}')
    if pos == 6:
        print(f'\033[0;31m 3 - {Pon[pos]:.<30}', end='')
        print(f' Over {Pon[7]:.<30}', end='')
        print(f' Time = {Pon[8]:>3}')
    if pos == 9:
        print(f'\033[0;34m 4 - {Pon[pos]:.<30}', end='')
        print(f' Over {Pon[10]:.<30}', end='')
        print(f' Time = {Pon[11]:>3}')
    if pos == 12:
        print(f'\033[0;30m 5 - {Pon[pos]:.<30}', end='')
        print(f' Over {Pon[13]:.<30}', end='')
        print(f' Time = {Pon[14]:>3}')
Ata = ('Cristiano Ronaldo', 94, 'Juventus',
       'Messi', 94, 'Barcelona',
       'Suárez', 91, 'Barcelona',
       'Lewandowski', 90, 'Bayer de Munique',
       'Kane', 89, 'Tottenham')
print(f'\033[1;30m ~'*90)
print('ATACANTES:')
for pos in range(0, len(Ata)):
    if pos == 0:
        print(f'\033[0;32m 1 - {Ata[pos]:.<30}', end='')
        print(f' Over {Ata[1]:.<30}', end='')
        print(f' Time = {Ata[2]:>3}')
    if pos == 3:
        print(f'\033[0;34m 2 - {Ata[pos]:.<30}', end='')
        print(f' Over {Ata[4]:.<30}', end='')
        print(f' Time = {Ata[5]:>3}')
    if pos == 6:
        print(f'\033[0;34m 3 - {Ata[pos]:.<30}', end='')
        print(f' Over {Ata[7]:.<30}', end='')
        print(f' Time = {Ata[8]:>3}')
    if pos == 9:
        print(f'\033[0;37m 4 - {Ata[pos]:.<30}', end='')
        print(f' Over {Ata[10]:.<30}', end='')
        print(f' Time = {Ata[11]:>3}')
    if pos == 12:
        print(f'\033[0;30m 5 - {Ata[pos]:.<30}', end='')
        print(f' Over {Ata[13]:.<30}', end='')
        print(f' Time = {Ata[14]:>3}')
