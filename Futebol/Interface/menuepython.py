import emoji


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31m ERRO! Por favor, digite um valor válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return emoji.emojize(f'\033[0;31;30m:soccer:\033[m' * 50, use_aliases=True)


def Cabeçalho(txt):
    print(linha())
    print(txt.center(75))
    print(linha())


def menu(lista):
    Cabeçalho('EPYTHON')
    c = 1
    for item in lista:
        print(f'\033[31m{c}\033[m - \033[30m{item}\033[m')
        c += 1
    opc = leiaInt('\033[31mSua Opção: \033[m')
    return opc
