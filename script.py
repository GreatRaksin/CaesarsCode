symbols = 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзиклмнопрстуфхцчшщъыьэю'
variants = ['зашифровать', 'з', 'расшифровать', 'р', 'hfcibahjdfnm', 'h', 'pfibahjdfnm', 'p']
maxKeySize = len(symbols)


def getMode():
    while True:
        mode = input('Вы хотите зашифровать или расшифровать? \n').lower()
        if mode in variants:
            return mode
        else:
            print(f'Введите "{variants[0]}" или "{variants[1]}" для зашифровки. \nВведите "{variants[2]}" или "{variants[3]}" для расшифровки.')


def getMessage():
    msg = input('Введите текст: ')
    return msg


def getKey():
    key = 0
    while True:
        key = int(input(f'Введите ключ шифрования (1-{maxKeySize})'))
        if 1 <= key <= maxKeySize:
            return key


def getTranslatedMessage(mode, msg, key):
    if mode[0] == 'р':
        key = -key
    translated = ''

    for symbol in msg:
        symbolIndex = symbols.find(symbol)
        if symbolIndex == -1:  # символ не найден
            # просто добавить этот символ без изменений
            translated += symbol
        else: # Зашифровать или расшифровать
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
print(f'Преобразованный текст: {getTranslatedMessage(mode, message, key)}')

