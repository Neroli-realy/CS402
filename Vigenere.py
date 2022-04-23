import string

class Vigenere:
    def __init__(self, key):
        self.key = key.lower()
        self.ALPHA = string.ascii_lowercase


    def makeKeyHoldText(self, text):
        k = self.key
        while len(k) < len(text):
            k = k * 2
        k = k[0:len(text)]
        return k

    def encrypt(self, pText):
        pText = pText.lower()
        k = self.makeKeyHoldText(pText)
        cText = ''
        for i in range(len(pText)):
            cText += self.ALPHA[(self.ALPHA.find(pText[i]) + self.ALPHA.find(k[i])) % 26]
        return cText

    def decrypt(self, cText):
        cText = cText.lower()
        k = self.makeKeyHoldText(cText)
        pText = ''
        for i in range(len(cText)):
            pText += self.ALPHA[(self.ALPHA.find(cText[i]) - self.ALPHA.find(k[i])) % 26]
        return pText

