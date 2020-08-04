from time import sleep
import emoji

c = ('\033[m',  # 0 - Sem cores
     '\033[0;30;41m',  # 1 - Vermelho
     '\033[0;30;42m',  # 2 - Verde
     '\033[0;30;43m',  # 3 - Amarelo
     '\033[0;30;44m',  # 4 - Azul
     '\033[0;30;45m',  # 5 - Roxo
     '\033[7;30m',  # 6 - Branco
     );


def vagas(com):
    tit(f'Acessando VAGAS.COM \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def tit(msg, cor=0):
    tam = len(msg) + 160
    print(c[cor], end='')
    print('=' * tam)
    print('{:^170}'.format(msg))
    print('=' * tam)
    print(c[0], end='')


def lin():
    print(emoji.emojize(f'\033[0;34m:briefcase:\033[m' * 105, use_aliases=True))


def lin1():
    print(emoji.emojize(f'\033[0;32m:white_check_mark:' * 105, use_aliases=True))


def dados():
    print(c[4], end='')
    print(f'Por favor se não cadastrado faça já seu login e preencha seu currículo on-line.'
          'Se já cadastrado coloque seu e-mail e senha.\'\'', [4])
    print(c[0], end='')


def júnior():
    if opção == 1:
        print(f' 1 - {vaga1[0]:.<50}', end='')
        print(f' Salário: {vaga1[1]:.<50}', end='')
        print(f'{vaga1[2]:.<50}', end='')
        print(f'{vaga1[3]:>5}')
        print(f' 2 - {vaga1[4]:.<50}', end='')
        print(f' Salário: {vaga1[5]:.<50}', end='')
        print(f'{vaga1[6]:.<50}', end='')
        print(f'{vaga1[7]:>5}')
        print(f' 3 - {vaga1[8]:.<50}', end='')
        print(f' Salário: {vaga1[9]:.<50}', end='')
        print(f'{vaga1[10]:.<50}', end='')
        print(f'{vaga1[11]:>5}')
        print(f' 4 - {vaga1[12]:.<50}', end='')
        print(f' Salário: {vaga1[13]:.<50}', end='')
        print(f'{vaga1[14]:.<50}', end='')
        print(f'{vaga1[15]:>5}')
        print(f' 5 - {vaga1[16]:.<50}', end='')
        print(f' Salário: {vaga1[17]:.<50}', end='')
        print(f'{vaga1[18]:.<50}', end='')
        print(f'{vaga1[19]:>5}')


def pleno():
    if opção == 2:
        print(f' 1 - {vaga2[0]:.<50}', end='')
        print(f' Salário: {vaga2[1]:.<50}', end='')
        print(f'{vaga2[2]:.<50}', end='')
        print(f'{vaga2[3]:>5}')
        print(f' 2 - {vaga2[4]:.<50}', end='')
        print(f' Salário: {vaga2[5]:.<50}', end='')
        print(f'{vaga2[6]:.<50}', end='')
        print(f'{vaga2[7]:>5}')
        print(f' 3 - {vaga2[8]:.<50}', end='')
        print(f' Salário: {vaga2[9]:.<50}', end='')
        print(f'{vaga2[10]:.<50}', end='')
        print(f'{vaga2[11]:>5}')
        print(f' 4 - {vaga2[12]:.<50}', end='')
        print(f' Salário: {vaga2[13]:.<50}', end='')
        print(f'{vaga2[14]:.<50}', end='')
        print(f'{vaga2[15]:>5}')
        print(f' 5 - {vaga2[16]:.<50}', end='')
        print(f' Salário: {vaga2[17]:.<50}', end='')
        print(f'{vaga2[18]:.<50}', end='')
        print(f'{vaga2[19]:>5}')


def sênior():
    if opção == 3:
        print(f' 1 - {vaga3[0]:.<50}', end='')
        print(f' Salário: {vaga3[1]:.<50}', end='')
        print(f'{vaga3[2]:.<50}', end='')
        print(f'{vaga3[3]:>5}')
        print(f' 2 - {vaga3[4]:.<50}', end=''),
        print(f' Salário: {vaga3[5]:.<50}', end='')
        print(f'{vaga3[6]:.<50}', end='')
        print(f'{vaga3[7]:>5}')
        print(f' 3 - {vaga3[8]:.<50}', end='')
        print(f' Salário: {vaga3[9]:.<50}', end='')
        print(f'{vaga3[10]:.<50}', end='')
        print(f'{vaga3[11]:.5}')
        print(f' 4 - {vaga3[12]:.<50}', end='')
        print(f' Salário: {vaga3[13]:.<50}', end='')
        print(f'{vaga3[14]:.<50}', end='')
        print(f'{vaga3[15]:>5}')
        print(f' 5 - {vaga3[16]:.<50}', end='')
        print(f' Salário: {vaga3[17]:.<50}', end='')
        print(f'{vaga3[18]:.<50}', end='')
        print(f'{vaga3[19]:>5}')


def p1():
    if opção == 4:
        print(f' 1 - {pro1[0]:.<50}', end='')
        print(f' Salário: {pro1[1]:.<50}', end='')
        print(f'{pro1[2]:.<50}', end='')
        print(f'{pro1[3]:>5}')
        print(f' 2 - {pro1[4]:.<50}', end='')
        print(f' Salário: {pro1[5]:.<50}', end='')
        print(f'{pro1[6]:.<50}', end='')
        print(f'{pro1[7]:>5}')
        print(f' 3 - {pro1[8]:.<50}', end='')
        print(f' Salário: {pro1[9]:.<50}', end='')
        print(f'{pro1[10]:.<50}', end='')
        print(f'{pro1[11]:>5}')
        print(f' 4 - {pro1[12]:.<50}', end='')
        print(f' Salário: {pro1[13]:.<50}', end='')
        print(f'{pro1[14]:.<50}', end='')
        print(f'{pro1[15]:>5}')
        print(f' 5 - {pro1[16]:.<50}', end='')
        print(f' Salário: {pro1[17]:.<50}', end='')
        print(f'{pro1[18]:.<50}', end='')
        print(f'{pro1[19]:>5}')
def p2():
    if opção == 4:
        print(f' 1 - {pro2[0]:.<40}', end='')
        print(f' Salário: {pro2[1]:.<40}', end='')
        print(f'{pro2[2]:.<40}', end='')
        print(f'{pro2[3]:>4}')
        print(f' 2 - {pro2[4]:.<40}', end='')
        print(f' Salário: {pro2[5]:.<40}', end='')
        print(f'{pro2[6]:.<40}', end='')
        print(f'{pro2[7]:>4}')
        print(f' 3 - {pro2[8]:.<40}', end='')
        print(f' Salário: {pro2[9]:.<40}', end='')
        print(f'{pro2[10]:.<40}', end='')
        print(f'{pro2[11]:>4}')
        print(f' 4 - {pro2[12]:.<40}', end='')
        print(f' Salário: {pro2[13]:.<40}', end='')
        print(f'{pro2[14]:.<40}', end='')
        print(f'{pro2[15]:>4}')
        print(f' 5 - {pro2[16]:.<40}', end='')
        print(f' Salário: {pro2[17]:.<40}', end='')
        print(f'{pro2[18]:.<40}', end='')
        print(f'{pro2[19]:>4}')
def p3():
    if opção == 4:
        print(f' 1 - {pro3[0]:.<50}', end='')
        print(f' Salário: {pro3[1]:.<50}', end='')
        print(f'{pro3[2]:.<50}', end='')
        print(f'{pro3[3]:>5}')
        print(f' 2 - {pro3[4]:.<50}', end='')
        print(f' Salário: {pro3[5]:.<50}', end='')
        print(f'{pro3[6]:.<50}', end='')
        print(f'{pro3[7]:>5}')
        print(f' 3 - {pro3[8]:.<50}', end='')
        print(f' Salário: {pro3[9]:.<50}', end='')
        print(f'{pro3[10]:.<50}', end='')
        print(f'{pro3[11]:>5}')
        print(f' 4 - {pro3[12]:.<50}', end='')
        print(f' Salário: {pro3[13]:.<50}', end='')
        print(f'{pro3[14]:.<50}', end='')
        print(f'{pro3[15]:>5}')
        print(f' 5 - {pro3[16]:.<50}', end='')
        print(f' Salário: {pro3[17]:.<50}', end='')
        print(f'{pro3[18]:.<50}', end='')
        print(f'{pro3[19]:>5}')
def p4():
    if opção == 4:
        print(f' 1 - {pro4[0]:.<50}', end='')
        print(f' Salário: {pro4[1]:.<50}', end='')
        print(f'{pro4[2]:.<50}', end='')
        print(f'{pro4[3]:>5}')
        print(f' 2 - {pro4[4]:.<50}', end='')
        print(f' Salário: {pro4[5]:.<50}', end='')
        print(f'{pro4[6]:.<50}', end='')
        print(f'{pro4[7]:>5}')
        print(f' 3 - {pro4[8]:.<50}', end='')
        print(f' Salário: {pro4[9]:.<50}', end='')
        print(f'{pro4[10]:.<50}', end='')
        print(f'{pro4[11]:>5}')
        print(f' 4 - {pro4[12]:.<50}', end='')
        print(f' Salário: {pro4[13]:.<50}', end='')
        print(f'{pro4[14]:.<50}', end='')
        print(f'{pro4[15]:>5}')
        print(f' 5 - {pro4[16]:.<50}', end='')
        print(f' Salário: {pro4[17]:.<50}', end='')
        print(f'{pro4[18]:.<50}', end='')
        print(f'{pro4[19]:>5}')
def p5():
    if opção == 4:
        print(f' 1 - {pro5[0]:.<50}', end='')
        print(f' Salário: {pro5[1]:.<50}', end='')
        print(f'{pro5[2]:.<50}', end='')
        print(f'{pro5[3]:>5}')
        print(f' 2 - {pro5[4]:.<50}', end='')
        print(f' Salário: {pro5[5]:.<50}', end='')
        print(f'{pro5[6]:.<50}', end='')
        print(f'{pro5[7]:>5}')
        print(f' 3 - {pro5[8]:.<50}', end='')
        print(f' Salário: {pro5[9]:.<50}', end='')
        print(f'{pro5[10]:.<50}', end='')
        print(f'{pro5[11]:>5}')
        print(f' 4 - {pro5[12]:.<50}', end='')
        print(f' Salário: {pro5[13]:.<50}', end='')
        print(f'{pro5[14]:.<50}', end='')
        print(f'{pro5[15]:>5}')
        print(f' 5 - {pro5[16]:.<50}', end='')
        print(f' Salário: {pro5[17]:.<50}', end='')
        print(f'{pro5[18]:.<50}', end='')
        print(f'{pro5[19]:>5}')
def p6():
    if opção == 4:
        print(f' 1 - {pro6[0]:.<40}', end='')
        print(f' Salário: {pro6[1]:.<40}', end='')
        print(f'{pro6[2]:.<40}', end='')
        print(f'{pro6[3]:>4}')
        print(f' 2 - {pro6[4]:.<40}', end='')
        print(f' Salário: {pro6[5]:.<40}', end='')
        print(f'{pro6[6]:.<40}', end='')
        print(f'{pro6[7]:>4}')
        print(f' 3 - {pro6[8]:.<40}', end='')
        print(f' Salário: {pro6[9]:.<40}', end='')
        print(f'{pro6[10]:.<40}', end='')
        print(f'{pro6[11]:>4}')
        print(f' 4 - {pro6[12]:.<40}', end='')
        print(f' Salário: {pro6[13]:.<40}', end='')
        print(f'{pro6[14]:.<40}', end='')
        print(f'{pro6[15]:>4}')
        print(f' 5 - {pro6[16]:.<40}', end='')
        print(f' Salário: {pro6[17]:.<40}', end='')
        print(f'{pro6[18]:.<40}', end='')
        print(f'{pro6[19]:>4}')
def p7():
    print(f' 1 - {pro7[0]:.<50}', end='')
    print(f' Salário: {pro7[1]:.<50}', end='')
    print(f'{pro7[2]:.<50}', end='')
    print(f'{pro7[3]:>5}')
    print(f' 2 - {pro7[4]:.<50}', end='')
    print(f' Salário: {pro7[5]:.<50}', end='')
    print(f'{pro7[6]:.<50}', end='')
    print(f'{pro7[7]:>5}')
    print(f' 3 - {pro7[8]:.<50}', end='')
    print(f' Salário: {pro7[9]:.<50}', end='')
    print(f'{pro7[10]:.<50}', end='')
    print(f'{pro7[11]:>5}')
    print(f' 4 - {pro7[12]:.<50}', end='')
    print(f' Salário: {pro7[13]:.<50}', end='')
    print(f'{pro7[14]:.<50}', end='')
    print(f'{pro7[15]:>5}')
    print(f' 5 - {pro7[16]:.<50}', end='')
    print(f' Salário: {pro7[17]:.<50}', end='')
    print(f'{pro7[18]:.<50}', end='')
    print(f'{pro7[19]:>5}')
def p8():
    print(f' 1 - {pro8[0]:.<40}', end='')
    print(f' Salário: {pro8[1]:.<40}', end='')
    print(f'{pro8[2]:.<40}', end='')
    print(f'{pro8[3]:>4}')
    print(f' 2 - {pro8[4]:.<40}', end='')
    print(f' Salário: {pro8[5]:.<40}', end='')
    print(f'{pro8[6]:.<40}', end='')
    print(f'{pro8[7]:>4}')
    print(f' 3 - {pro8[8]:.<40}', end='')
    print(f' Salário: {pro8[9]:.<40}', end='')
    print(f'{pro8[10]:.<40}', end='')
    print(f'{pro8[11]:>4}')
    print(f' 4 - {pro8[12]:.<40}', end='')
    print(f' Salário: {pro8[13]:.<40}', end='')
    print(f'{pro8[14]:.<40}', end='')
    print(f'{pro8[15]:>4}')
    print(f' 5 - {pro8[16]:.<40}', end='')
    print(f' Salário: {pro8[17]:.<40}', end='')
    print(f'{pro8[18]:.<40}', end='')
    print(f'{pro8[19]:>4}')
def p9():
    print(f' 1 - {pro9[0]:.<50}', end='')
    print(f' Salário: {pro9[1]:.<50}', end='')
    print(f'{pro9[2]:.<50}', end='')
    print(f'{pro9[3]:>5}')
    print(f' 2 - {pro9[4]:.<50}', end='')
    print(f' Salário: {pro9[5]:.<50}', end='')
    print(f'{pro9[6]:.<50}', end='')
    print(f'{pro9[7]:>5}')
    print(f' 3 - {pro9[8]:.<50}', end='')
    print(f' Salário: {pro9[9]:.<50}', end='')
    print(f'{pro9[10]:.<50}', end='')
    print(f'{pro9[11]:>5}')
    print(f' 4 - {pro9[12]:.<50}', end='')
    print(f' Salário: {pro9[13]:.<50}', end='')
    print(f'{pro9[14]:.<50}', end='')
    print(f'{pro9[15]:>5}')
    print(f' 5 - {pro9[16]:.<50}', end='')
    print(f' Salário: {pro9[17]:.<50}', end='')
    print(f'{pro9[18]:.<50}', end='')
    print(f'{pro9[19]:>5}')
def p10():
    print(f' 1 - {pro10[0]:.<50}', end='')
    print(f' Salário: {pro10[1]:.<50}', end='')
    print(f'{pro10[2]:.<50}', end='')
    print(f'{pro10[3]:>5}')
    print(f' 2 - {pro10[4]:.<50}', end='')
    print(f' Salário: {pro10[5]:.<50}', end='')
    print(f'{pro10[6]:.<50}', end='')
    print(f'{pro10[7]:>5}')
    print(f' 3 - {pro10[8]:.<50}', end='')
    print(f' Salário: {pro10[9]:.<50}', end='')
    print(f'{pro10[10]:.<50}', end='')
    print(f'{pro10[11]:>5}')
    print(f' 4 - {pro10[12]:.<50}', end='')
    print(f' Salário: {pro10[13]:.<50}', end='')
    print(f'{pro10[14]:.<50}', end='')
    print(f'{pro10[15]:>5}')
    print(f' 5 - {pro10[16]:.<50}', end='')
    print(f' Salário: {pro10[17]:.<50}', end='')
    print(f'{pro10[18]:.<50}', end='')
    print(f'{pro10[19]:>5}')
def p11():
    print(f' 1 - {pro11[0]:.<40}', end='')
    print(f' Salário: {pro11[1]:.<40}', end='')
    print(f'{pro11[2]:.<40}', end='')
    print(f'{pro11[3]:>4}')
    print(f' 2 - {pro11[4]:.<40}', end='')
    print(f' Salário: {pro11[5]:.<40}', end='')
    print(f'{pro11[6]:.<40}', end='')
    print(f'{pro11[7]:>4}')
    print(f' 3 - {pro11[8]:.<40}', end='')
    print(f' Salário: {pro11[9]:.<40}', end='')
    print(f'{pro11[10]:.<40}', end='')
    print(f'{pro11[11]:>4}')
    print(f' 4 - {pro11[12]:.<40}', end='')
    print(f' Saário: {pro11[13]:.<40}', end='')
    print(f'{pro11[14]:.<40}', end='')
    print(f'{pro11[15]:>4}')
    print(f' 5 - {pro11[16]:.<40}', end='')
    print(f' Salário: {pro11[17]:.<40}', end='')
    print(f'{pro11[18]:.<40}', end='')
    print(f'{pro11[19]:>4}')
def p12():
    print(f' 1 - {pro12[0]:.<40}', end='')
    print(f' Salário: {pro12[1]:.<40}', end='')
    print(f'{pro12[2]:.<40}', end='')
    print(f'{pro12[3]:>4}')
    print(f' 2 - {pro12[4]:.<40}', end='')
    print(f' Salário: {pro12[5]:.<40}', end='')
    print(f'{pro12[6]:.<40}', end='')
    print(f'{pro12[7]:>4}')
    print(f' 3 - {pro12[8]:.<40}', end='')
    print(f' Salário: {pro12[9]:.<40}', end='')
    print(f'{pro12[10]:.<40}', end='')
    print(f'{pro12[11]:>4}')
    print(f' 4 - {pro12[12]:.<40}', end='')
    print(f' Salário: {pro12[13]:.<40}', end='')
    print(f'{pro12[14]:.<40}', end='')
    print(f'{pro12[15]:>4}')
    print(f' 5 - {pro12[16]:.<40}', end='')
    print(f' Salário: {pro12[17]:.<40}', end='')
    print(f'{pro12[18]:.<40}', end='')
    print(f'{pro12[19]:>4}')


opção = 0

# Programa Principal
while True:
    lin()
    tit(f'VAGAS.COM - PYTHON', 2)
    lin()
    sleep(1)
    dados()
    print(c[6], end='')
    resp = str(input(f'\033[7;30m Já é cadastrado?[S/N]:')).upper()[0]
    while True:
        if resp == 'N':
            nome = str(input('Nome completo:'))
            idade = int(input('Idade:'))
            sexo = str(input('Sexo:'))
            print(f"Por gentileza sr.(a) {nome} crie um login, e uma senha com apenas números para ser cadastrada aqui no VAGAS.COM", )
            l = str(input('Login:'))
            s = int(input('Senha:'))
            print('PRONTO! Agora você já está cadastrado no VAGAS.COM')
            print('Agora nos fale um pouco de sua experiência profissional e faça seu curícuilo!')
            lin()
            # Currículo
            print('{:^55}'.format('CURRÍCULO:'))
            n = str(input(''))
            rua = str(input(''))
            anos = str(input(''))
            email = str(input(''))
            print('OBJETIVO PROFISSIONAL:')
            obj = str(input(''))
            print('CURSOS EXTRACURRICULARES:')
            cursos = str(input(''))
        if resp == 'S':
            login = str(input('Digite seu login:'))
            senha = int(input('Digite sua senha (APENAS NÚMEROS):'))
            # Vagas
            vaga1 = ('Desenvolvedor de Sistemas - Jr.', '3.500R$', 'São Paulo - SP', 'Google',
                     'Desenvolvedor de Sistemas - Jr.', '3.000R$', 'Belo Horizonte - MG', 'Mercado Livre',
                     'Desenvolvedor de Sistemas - Jr.', '2.900R$', 'São Paulo - SP', 'IBM',
                     'Desenvolvedor de Sistemas - Jr.', '2.900R$', 'Rio de Janeiro - RJ', 'Amazon',
                     'Desenvolvedor de Sistemas - Jr.', '2.500R$', 'Porto Alegre - RS', 'Rocketseat')

            vaga2 = ('Desenvolvedor de Sistemas - Pleno', '8.000R$', 'São Paulo - SP', 'Bradesco',
                     'Desenvolvedor de Sistemas - Pleno', '7.200R$', 'Florianópolis - SC', 'Banco do Brasil',
                     'Desenvolvedor de Sistemas - Pleno', '5.000R$', 'Brasília - DF', 'Governo Federal',
                     'Desenvolvedor de Sistemas - Pleno', '6.000R$', 'São Paulo - SP', 'Ambev',
                     'Desenvolvedor de Sistemas - Pleno', '4.500R$', 'Salvador - BA', 'Unilever')

            vaga3 = ('Desenvolvedor de Sistemas - Sênior', '11.000R$', 'São Paulo - SP', 'Apple',
                     'Desenvolvedor de Sistemas - Sênior', '11.000R$', 'Rio de Janeiro - RJ', 'Microsoft',
                     'Desenvolvedor de Sistemas - Sênior', '10.900R$', 'Curitiba - PR', 'HP',
                     'Desenvolvedor de Sistemas - Sênior', '10.500R$', 'Belo Horizonte - MG', 'Itaú',
                     'Desenvolvedor de Sistemas - Sênior', '10.000R$', 'São Paulo - SP', 'Dropbox')

            pro1 = ('Administração', '7.000R$', 'Rio de Janeiro - RJ', 'Bayer',
                    'Administração', '5.000R$', 'Belo Horizonte - MG', 'Grupo Netshoes',
                    'Administração', '4.200R$', 'Belo Horizonte - MG', 'Takeda Brasil',
                    'Administração', '3.500R$', 'São Paulo - SP', 'Mercado Livre',
                    'Administração', '3.000R$', 'São Paulo - SP', 'Nike')

            pro2 = ('Ciências Contábeis', '7.500R$', 'Rio de Janeiro - RJ', 'Contabilizario',
                    'Ciências Contábeis', '7.000R$', 'São Paulo - SP', 'Decolarh Desenvolvimento Organizacional',
                    'Ciências Contábeis', '6.000R$', 'Salvador - BA', 'Gess Administração e participações',
                    'Ciências Contábeis', '5.000R$', 'São Paulo - SP', 'Partners Contabilidade & Consultoria',
                    'Ciências Contábeis', '4.500R$', 'São Paulo - SP', 'Great Group')

            pro3 = ('Gestão de Recursos Humanos', '6.000R$', 'São Paulo - SP', 'Google',
                    'Gestão de Recursos Humanos', '5.000R$', 'Porto Alegre - RS', 'FedEx',
                    'Gestão de Recursos Humanos', '4.000R$', 'Curitiba - PR', 'Oxfam',
                    'Gestão de Recursos Humanos', '3.000R$', 'Belo Horizonte - MG', 'Prudential',
                    'Gestão de Recursos Humanos', '2.900R$', 'Espírito Santo - ES', 'SAS')

            pro4 = ('Logística', '3.300R$', 'São Paulo - SP', 'DHL',
                    'Logística', '3.000R$', 'São Paulo - SP', 'Colgate',
                    'Logística', '2.900R$', 'Mato Grosso do Sul - MS', 'CEVA',
                    'Logística', '2.900R$', 'Rio de Janeiro - RJ', 'AMBEV',
                    'Logística', '2.800R$', 'Belo Horizonte - MG', 'Nestlé')

            pro5 = ('Marketing', '4.200R$', 'Porto Alegre - RS', 'Grupo Hinode',
                    'Marketing', '4.100R$', 'Salvador - BA', 'i9life',
                    'Marketing', '4.000R$', 'Florianópolis - SC', 'Amakha Paris',
                    'Marketing', '4.000R$', 'Brasília - DF', 'Racco',
                    'Marketing', '4.000R$', 'São Paulo - SP', 'Polishop')

            pro6 = ('Arquitetura', '7.500R$', 'São Paulo - SP', 'Esritório Felipe Hess',
                    'Arquitetura', '7.000R$', 'Florianópolis - SC', 'Isay Wenfield',
                    'Arquitetura', '7.000R$', 'São Paulo - SP', 'Apiacás',
                    'Arquitetura', '7.000R$', 'São Paulo - SP', 'Studio Arthur Casas',
                    'Arquitetura', '6.900R$', 'São Paulo - SP', 'Ar Arquitetos')

            pro7 = ('Banco de Dados', '8.200R$', 'Porto Alegre - RS', 'OpService',
                    'Banco de Dados', '8.000R$', 'Rio de Janeiro - RJ', 'UniMed',
                    'Banco de Dados', '7.000R$', 'Curitiba - PR', 'Qualitor',
                    'Banco de Dados', '6.500R$', 'São Paulo - SP', 'AMF Tecnologia',
                    'Banco de Dados', '5.000R$', 'Porto Alegre - RS', 'Inter OP')

            pro8 = ('Pedagogia', '7.500R$', 'São Paulo - SP', 'Escola Mackenzie',
                    'Pedagogia', '5.000R$', 'Rio de Janeiro - RJ', 'Cruzeiro do Sul Educacional',
                    'Pedagogia', '4.100R$', 'Belo Horizonte - MG', 'Faculdade Pitágoras',
                    'Pedagogia', '3.500R$', 'Salvador - BA', 'ONG Educacional',
                    'Pedagogia', '2.500R$', 'São Paulo - SP', 'Faculdade Anhanguera Educacional')

            pro9 = ('Rádio, Tv e Internet', '5.500R$', 'Rio de Janeiro - RJ', 'Globo',
                    'Rádio, Tv e Internet', '3.500R$', 'Rio de Janeiro - RJ', 'Rádio FM',
                    'Rádio, Tv e Internet', '3.000R$', 'Mato Grosso do Sul - MS', 'UOL',
                    'Rádio, Tv e Internet', '2.500R$', 'São Paulo - SP', 'SBT',
                    'Rádio, Tv e Internet', '2.200R$', 'São Paulo', 'Youtube')

            pro10 = ('Engenharia Mecânica', '9.000R$', 'São Paulo - SP', 'Mercedes Benz',
                     'Engenharia Mecânica', '8.000R$', 'Espírito Santo - ES', 'Chevrolet',
                     'Engenharia Mecânica', '6.000R$', 'Belo Horizonte - MG', 'Honda',
                     'Engenharia Mecânica', '5.500R$', 'São Paulo - SP', 'Fiat',
                     'Engenharia Mecânica', '4.000R$', 'São Paulo - SP', 'Vip Engenharia')

            pro11 = ('Medicina', '18.000R$', 'São Paulo - SP', 'Hospital Sírio Libânes',
                     'Medicina', '13.000R$', 'Porto Alegre - RS', 'Hospital Moinhos de Ventos',
                     'Medicina', '11.000R$', 'São Paulo - SP', 'Hospital Albert Einsten',
                     'Medicina', '11.000R$', 'Rio de Janeiro - RJ', 'Hospital São Vicente de Paulo',
                     'Medicina', '8.000R$', 'São Paulo - SP', 'Hospital das Clínicas')

            pro12 = ('Design', '3.500R$', 'São Paulo - SP', 'Twist Comunicação',
                     'Design', '3.000R$', 'Rio de Janeiro - RJ', 'Strategica IT',
                     'Design', '2.900R$', 'Rio de Janeiro - RJ', 'Wizartes Gráfica',
                     'Design', '2.900R$', 'Canoas - RS', 'IsmaTec Info',
                     'Design', '2.600R$', 'São Paulo - SP', 'Unboud Sales')

            lin()
            print('Escolha uma dessa opções para buscarmos sua vaga.....')
            print('''[1] Desenvolvedor Júnior
[2] Desenvolvedor Pleno
[3] Desenvolvedor Sênior
[4] Outras profissões
[5] Sair do programa''')
            lin()
            opção = int(input('>>> Qual é a sua opção?:'))
            if opção == 4:
                print(c[0], end='')
                print("BUSCANDO PROFISSÕES.......")
                lin1()
                sleep(3)
            if opção == 5:
                print('PROGRAMA FINALIZADO!')
                break
            else:
                print(c[0], end='')
                print('BUSCANDO VAGAS.....')
                lin1()
                sleep(3)
            print(c[0], end='')
            if opção == 1:
                júnior()
                lin1()
            if opção == 2:
                pleno()
                lin1()
            if opção == 3:
                sênior()
                lin1()
            if opção == 4:
                print('Temos essa outras profissões disponíveis, escolha uma delas para buscarmos sua vaga.')
                print('''[1] Adminitração
[2] Ciências Contàbeis
[3] Gestão de Recursos Humanos
[4] Logística
[5] Marketing
[6] Arquitetura
[7] Banco de Dados
[8] Pedagogia
[9] Rádio, Tv e Internet
[10] Engenharia Mecânica
[11] Medicina
[12] Design''')
                op = int(input('>>> Qual é a sua opção?'))
                if op == 1:
                    print(c[0], end='')
                    print('BUSCANDO VAGAS.......')
                    sleep(3)
                    lin1()
                    print(c[0], end='')
                    p1()
                    lin1()
                if op == 2:
                    print(c[0], end='')
                    print('BUSCANDO VAGAS.......')
                    sleep(3)
                    lin1()
                    print(c[0], end='')
                    p2()
                    lin1()
                if op == 3:
                    print(c[0], end='')
                    print('BUSCANDO VAGAS.......')
                    sleep(3)
                    lin1()
                    print(c[0], end='')
                    p3()
                    lin1()
                if op == 4:
                    print(c[0], end='')
                    print('BUSCANDO VAGAS......')
                    sleep(3)
                    lin1()
                    print(c[0], end='')
                    p4()
                    lin1()
                if op == 5:
                    print(c[0], end='')
                    print('BUSCANDO VAGAS......')
                    sleep(3)
                    lin1()
                    print(c[0], end='')
                    p5()
                    lin1()
                if op == 6:
                    print(c[0], end='')
                    print('BUSCANDO VAGAS......')
                    sleep(3)
                    lin1()
                    print(c[0], end='')
                    p6()
                    lin1()
                if op == 7:
                    print(c[0], end='')
                    print('BUSCANDO VAGAS.......')
                    sleep(3)
                    lin1()
                    print(c[0], end='')
                    p7()
                    lin1()
                if op == 8:
                    print(c[0], end='')
                    print('BUSCANDO VAGAS.......')
                    sleep(3)
                    lin1()
                    print(c[0], end='')
                    p8()
                    lin1()
                if op == 9:
                    print(c[0], end='')
                    print('BUSCANDO VAGAS.......')
                    sleep(3)
                    lin1()
                    print(c[0], end='')
                    p9()
                    lin1()
                if op == 10:
                    print(c[0], end='')
                    print('BUSCANDO VAGAS.......')
                    sleep(3)
                    lin1()
                    print(c[0], end='')
                    p10()
                    lin1()
                if op == 11:
                    print(c[0], end='')
                    print('BUSCANDO VAGAS.......')
                    sleep(3)
                    lin1()
                    print(c[0], end='')
                    p11()
                    lin1()
                if op == 12:
                    print(c[0], end='')
                    print('BUSCANDO VAGAS.......')
                    sleep(3)
                    lin1()
                    print(c[0], end='')
                    p12()
                    lin1()
                break
        break
    break
print(c[2], end='')
print('Fim do Programa! Volte Sempre!!!')
