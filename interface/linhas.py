import emoji
from WALLET.interface.cor import c, c1


def lindinheiro():
    print(c[2], end='')
    print(emoji.emojize(f':dollar:' * 105, use_aliases=True))
    print(c1[0], end='')

def linworld():
    print(c1[6], end='')
    print(emoji.emojize(f':earth_americas:' * 105, use_aliases=True))
    print(c[0], end='')

def airplane():
    print(c1[6], end='')
    print(emoji.emojize(f':airplane:' * 105, use_aliases=True))
    print(c[0], end='')
