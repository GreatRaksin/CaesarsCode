class CaesarChifer:
    def __init__(self, m):
        self.message = m
        self.symbols = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'

    def setLanguage(self, lang):
        if lang.startswith(('en', 'En')):
            self.symbols = 'ABCDEFGHIJKLMNOPQRSTUWXYZabcdefghijklmnopqrstuwxyz'
        elif lang.startswith(('Ru', 'ru')):
            self.symbols = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя'
        else:
            print('Такого языка я не знаю!')

    def getLanguage(self):
        return self.symbols

    def encrypt(self, key):
        translated = ''

        for symbol in self.message:
            symbolIndex = self.symbols.find(symbol)

            if symbolIndex == -1:
                translated += symbol
            else:
                symbolIndex += key

                if symbolIndex >= len(self.symbols):
                    symbolIndex -= len(self.symbols)
                elif symbolIndex < 0:
                    symbolIndex += len(self.symbols)

                translated += self.symbols[symbolIndex]
        return translated

    def decrypt(self):
        print('Сейчас будет брутфорс, наслаждайтесь.\n')
        for key in range(len(self.symbols)):
            translated = ''
            for symbol in self.message:
                if symbol in self.symbols:
                    num = self.symbols.find(symbol)
                    num = num - key
                    if num < 0:
                        num = num + len(self.symbols)
                    translated = translated + self.symbols[num]
                else:
                    translated = translated + symbol
            print(f'Подбираю ключ #{key}: {translated}')
