symbols = 'abcdefghijklmnopqrstuvwxyz'
variants = ['encrypt', 'decrypt', 'e', 'd']
maxKeySize = len(symbols)


def getMode():
    while True:
        mode = input('Do you want to encrypt or decrypt message? \n').lower()
        if mode in variants:
            return mode
        else:
            print(
                f'input "{variants[0]}" or "{variants[2]}" for encryption. \nInput "{variants[1]}" or "{variants[3]}" for decription.')


def getMessage():
    msg = input('Input message: ')
    return msg


def getKey():
    key = 0
    while True:
        key = int(input(f'Input encryption key (1-{maxKeySize})'))
        if 1 <= key <= maxKeySize:
            return key


def getTranslatedMessage(mode, msg, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in msg:
        symbolIndex = symbols.find(symbol)
        if symbolIndex == -1:  # символ не найден
            # просто добавить этот символ без изменений
            translated += symbol
        else:  # Зашифровать или расшифровать
            symbolIndex += key

            if symbolIndex >= len(symbols):
                symbolIndex -= len(symbols)
            elif symbolIndex < 0:
                symbolIndex += len(symbols)

            translated += symbols[symbolIndex]
    return translated


mode = getMode()
message = getMessage()
key = getKey()
print(f'Your text: {getTranslatedMessage(mode, message, key)}')
