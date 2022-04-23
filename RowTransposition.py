import math


class RowTransposition:
    def __init__(self, key):
        self.key = key.strip().replace(' ', '')


    def pad(self, plainText):
        res = plainText + ' '*(len(self.key) - (len(plainText) % len(self.key)))
        return res

    def encrypt(self, plainText):
        cText = ''
        for i in sorted(self.key):
            column = self.key.find(i)
            cIndex = column
            for j in range(len(plainText)):
                cText += plainText[cIndex]
                cIndex += len(self.key)
                if cIndex >= len(plainText):
                    break
        return cText

    def decrypt(self, cipherText):
        pText = ''
        rate = math.ceil(len(cipherText) / len(self.key))
        for i in range(rate):
            for j in self.key:
                pText += cipherText[(((int(j)-1)*rate)+i)]
        return pText


