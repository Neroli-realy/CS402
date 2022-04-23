from itertools import  cycle
class RailFence:
    def __init__(self, key):
        self.key = int(key.strip().lower())


    def constructFence(self, plainText):
        charsIndex = list(range(self.key)) + list(range(self.key-2, 0, -1))
        return  zip(cycle(charsIndex), range(len(plainText)))

    def encrypt(self, plainText):
        x = self.constructFence(plainText)
        cText = ''.join([c for _, c in sorted(zip(x, plainText))])
        return cText

    def decrypt(self, cipherText):
        x = self.constructFence(cipherText)
        plainText = ''.join([p for _, p in (sorted(zip(sorted(x), cipherText), key=lambda g: g[0][1]))])
        return plainText

x = RailFence('5')
y = x.encrypt('Be confident in yourself. Nobody can make you feel inferior without your permission.')
print(y)

print(x.decrypt(y))