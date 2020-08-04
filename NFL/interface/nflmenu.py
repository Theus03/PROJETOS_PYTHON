import emoji


def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print(f'\033[0;31mERRO! Por favor, digite um valor válido.\033[m')
        except KeyboardInterrupt:
            print(f'\033[0;31m O usuário preferiu não digitar esse número!\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return emoji.emojize(f'\033[0;31m:football:\033[m ' * 30, use_aliases=True)


def cabeçalho(txt):
    print(linha())
    print(txt.center(75))
    print(linha())


def menu(lista):
    cabeçalho('EPYTHON')
    c = 1
    for item in lista:
        print(f'\033[0;31m {c}\033[m - \033[30m{item}\033[m')
        c += 1
    print(linha())
    opc = LeiaInt('\033[31mSua Opção:')
    return opc
