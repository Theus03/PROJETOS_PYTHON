PG = ('Stephen Curry', 96, 'Golden State Warriors',
      'Russell Westbrook', 93, 'Oklahoma City',
      'Kyrie Irving', 90, 'Boston Celics',
      'Chris Paul', 90, 'Houston Rockets',
      'Damian Lillard', 90, 'Portland Trail Blazers')
print('='*100)
print(f'\033[1m {"TOP 5 - JOGADORES DE CADA POSIÇÃO - NBA2K19":^90}')
print('='*100)
print(f'\033[1m{"ARMADORES PRINCIPAIS:"}')
for pos in range(0, len(PG)):
    if pos == 0:
        print(f'\033[0;34m 1 - {PG[pos]:.<30}', end='')
        print(f' Over {PG[1]:.<30}', end='')
        print(f' Time = {PG[2]:>3}')
    if pos == 3:
        print(f'\033[0;36m 2 - {PG[pos]:.<30}', end='')
        print(f' Over {PG[4]:.<30}', end='')
        print(f' Time = {PG[5]:>3}')
    if pos == 6:
        print(f'\033[0;32m 3 - {PG[pos]:.<30}', end='')
        print(f' Over {PG[7]:.<30}', end='')
        print(f' Time = {PG[8]:>3}')
    if pos == 9:
        print(f'\033[0;31m 4 - {PG[pos]:.<30}', end='')
        print(f' Over {PG[10]:.<30}', end='')
        print(f' Time = {PG[11]:>3}')
    if pos == 12:
        print(f'\033[0;30m 5 - {PG[pos]:.<30}', end='')
        print(f' Over {PG[13]:.<30}', end='')
        print(f' Time = {PG[14]:>3}')

SG = ('James Harden', 96, 'Houston Rockets',
      'DeMar DeRozan', 89, 'San Antonio Spurs',
      'Jimmy Butler', 89, 'Minnesota Timberwolves',
      'Klay Thompson', 89, 'Golden State Warriors',
      'Victor Oladipo', 88, 'Indiana Pacers')
print('='*100)
print(f'\033[1m{"ARMADORES ARREMESSADORES:"}')
for pos in range(0, len(SG)):
    if pos == 0:
        print(f'\033[0;31m 1 - {SG[pos]:.<30}', end='')
        print(f' Over {SG[1]:.<30}', end='')
        print(f' Time = {SG[2]:3>}')
    if pos == 3:
        print(f'\033[0;30m 2 - {SG[pos]:.<30}', end='')
        print(f' Over {SG[4]:.<30}', end='')
        print(f' Time = {SG[5]:>3}')
    if pos == 6:
        print(f'\033[0;37m 3 - {SG[pos]:.<30}', end='')
        print(f' Over {SG[7]:.<30}', end='')
        print(f' Time = {SG[8]:>3}')
    if pos == 9:
        print(f'\033[0;34m 4 - {SG[pos]:.<30}', end='')
        print(f' Over {SG[10]:.<30}', end='')
        print(f' Time = {SG[11]:>3}')
    if pos == 12:
        print(f'\033[0;35m 5 - {SG[pos]:.<30}', end='')
        print(f' Over {SG[13]:.<30}', end='')
        print(f' Time = {SG[14]:>3}')

SF = ('LeBron James', 98, 'Los Angeles Lakers',
      'Kevin Durant', 96, 'Golden States Warriors',
      'Giannis Antetokounmpo', 94, 'Milauwakee Bucks',
      'Kawhi Leonard', 94, 'Toronto Raptors',
      'Paul George', 89, 'Oklahoma City Thunder')
print('='*100)
print(f'\033[1m{"ALAS:"}')
for pos in range(0, len(SF)):
    if pos == 0:
        print(f'\033[0;33m 1 - {SF[pos]:.<30}', end='')
        print(f' Over {SF[1]:.<30}', end='')
        print(f' Time = {SF[2]:>3}')
    if pos == 3:
        print(f'\033[0;34m 2 - {SF[pos]:.<30}', end='')
        print(f' Over {SF[4]:.<30}', end='')
        print(f' Time = {SF[5]:>3}')
    if pos == 6:
        print(f'\033[0;32m 3 - {SF[pos]:.<30}', end='')
        print(f' Over {SF[7]:.<30}', end='')
        print(f' Time = {SF[8]:>3}')
    if pos == 9:
        print(f'\033[0;31m 4 - {SF[pos]:.<30}', end='')
        print(f' Over {SF[10]:.<30}', end='')
        print(f' Time = {SF[11]:>3}')
    if pos == 12:
        print(f'\033[0;36m 5 - {SF[pos]:.<30}', end='')
        print(f' Over {SF[13]:.<30}', end='')
        print(f' Time = {SF[14]:>3}')

PF = ('Anthony Davis', 94, 'New Orleans Pelicans',
      'LaMarcus Aldridge', 89, 'San Antonio Spurs',
      'Kristaps Porzingis', 88, 'Knicks',
      'Kevin Love', 87, 'Cleveland Cavaliers',
      'Draymond Green', 87, 'Golden State Warriors')
print('='*100)
print(f'\033[1m{"ALA DE FORÇA:"}')
for pos in range(0, len(PF)):
    if pos == 0:
        print(f'\033[0;35m 1 - {PF[pos]:.<30}', end='')
        print(f' Over {PF[1]:.<30}', end='')
        print(f' Time = {PF[2]:>3}')
    if pos == 3:
        print(f'\033[0;30m 2 - {PF[pos]:.<30}', end='')
        print(f' Over {PF[4]:.<30}', end='')
        print(f' Time = {PF[5]:>3}')
    if pos == 6:
        print(f'\033[0;33m 3 - {PF[pos]:.<30}', end='')
        print(f' Over {PF[7]:.<30}', end='')
        print(f' Time = {PF[8]:>3}')
    if pos == 9:
        print(f'\033[0;37m 4 - {PF[pos]:.<30}', end='')
        print(f' Over {PF[10]:.<30}', end='')
        print(f' Time = {PF[11]:>3} ')
    if pos == 12:
        print(f'\033[0;34m 5 - {PF[pos]:.<30}', end='')
        print(f' Over {PF[13]:.<30}', end='')
        print(f' Time = {PF[14]:>3}')

C = ('Karl-Anthony Towns', 91, 'Minnesota Timberwolves',
     'DeMarcus Cousins', 90, 'Golden State Warriors',
     'Joel Embiid', 90, 'Philadelphia 76ers',
     'Nikola Jovic', 89, 'Denver Nuggets',
     'Andre Drummond', 87, 'Detroit Pistons')
print('='*100)
print(f'\033[1m{"PIVÔS:"}')
for pos in range(0, len(C)):
    if pos == 0:
        print(f'\033[0;37m 1 - {C[pos]:.<30}', end='')
        print(f' Over {C[1]:.<30}', end='')
        print(f' Time = {C[2]:>3}')
    if pos == 3:
        print(f'\033[0;34m 2 - {C[pos]:.<30}', end='')
        print(f' Over {C[4]:.<30}', end='')
        print(f' Time = {C[5]:>3}')
    if pos == 6:
        print(f'\033[0;30m 3 - {C[pos]:.<30}', end='')
        print(f' Over {C[7]:.<30}', end='')
        print(f' Time = {C[8]:>3}')
    if pos == 9:
        print(f'\033[0;36m 4 - {C[pos]:.<30}', end='')
        print(f' Over {C[10]:.<30}', end='')
        print(f' Time = {C[11]:.>3}')
    if pos == 12:
        print(f'\033[0;35m 5 - {C[pos]:.<30}', end='')
        print(f' Over {C[13]:.<30}', end='')
        print(f' Time = {C[14]:>3}')
print('='*100)
