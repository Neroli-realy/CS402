import string

class OneTimePad:
    def __init__(self, keyFile):
        self.key = keyFile.strip().lower()
        self.ALPHA = string.ascii_lowercase

    def encrypt(self, plainText):
        plainText = plainText.lower()
        #cText = ''.join([self.ALPHA[(self.ALPHA.find(x) + self.ALPHA.find(y))%26] for x,y in zip(plainText, self.key)]) this is the right one
        #this is not right but it's the requested
        cText = ''.join([self.ALPHA[(self.ALPHA.find(x) ^ self.ALPHA.find(y))%26] for x,y in zip(plainText, self.key)])
        return cText

    def decrypt(self, cipherText):
        cipherText = cipherText.lower()
        pText = ''.join([self.ALPHA[(self.ALPHA.find(x) ^ self.ALPHA.find(y))%26] for x,y in zip(cipherText, self.key)])
        return pText

x = OneTimePad('lmbidzxwoxzitxrymatcjvnphareclueizufoldscujdigxp')
y = x.encrypt('itissaidthattheonetimepadisthebestcipheranywhere')
print(y)
print(x.decrypt(y))
