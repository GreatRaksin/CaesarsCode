from OOP.engine import CaesarChifer


def ask():
    ans = input('На каком языке вы хотите работать?')
    while ans not in ('English', 'En', 'Eng', 'english', 'eng', 'en', 'Russian', 'rus', 'ru'):
        ans = input('На каком языке вы хотите работать?')
    return ans


def getMode():
    mode = input('Вы хотите зашифровать или расшифровать сообщение? ')
    if mode.lower().startswith(('з', 'p')):
        mode = 1
    elif mode.lower().startswith(('р', 'h')):
        mode = 2
    return mode


def worker(ans, m):
    msg = input('Введите текст: ')
    message = CaesarChifer(msg)
    message.setLanguage(ans)

    if m == 1:
        key = int(input('Введите сдвиг шифра: '))
        return message.encrypt(key)
    elif m == 2:
        return message.decrypt()
