def ficha(nome=f'\033[1;31m<desconhecido>\033[m', franquia=f'\033[1;31m<desconhecido>\033[m', cesta=0, rebote=0):
    print(f'O Jogador {nome}, que joga na franquia do {franquia} fez {cesta} cesta(s) e teve um total de {rebote} rebotes na Temporada.')


#Programa Principal
n = str(input('Nome do Jogador:'))
f = str(input(f'Nome do time atual em que {n} joga:'))
c = str(input('Número de cesta(s):'))
r = str(input('Número de rebote(s) no campeonato:'))
if c.isnumeric():
    c = int(c)
else:
    c = 0
if r.isnumeric():
    r = int(r)
else:
    r = 0
if n.strip() == '':
    ficha(cesta=c, rebote=r)
else:
    print(ficha(n, f, c, r))
