import numpy as np
import math
import string
from Crypto.Util.number import inverse

class Hill:


    def isSquare(self, n):
        self.r = int(math.sqrt(n))
        return int(self.r)**2 == n

    def keyTomatrix(self):

        if(not self.isSquare(len(self.key))):
            print('Bad Key')
            exit()

        else:
            try:

                keyList = []
                for c in self.key: keyList.append(self.ALPHA.find(c))
                x = np.array(keyList).reshape(self.r, self.r)
                np.linalg.inv(x)
                return x
            except:
                print('Bad Key')
                exit(1)


    def __init__(self, keyFile):
        self.r = None
        self.ALPHA = string.ascii_lowercase
        self.key = keyFile.read().lower()
        self.keyMatrix = self.keyTomatrix()


    def Pad(self, t):
        x = self.r - (len(t) % self.r)
        for i in range(x): t += 'x'
        return t

    def encrypt(self, pText):
        pText = pText.lower()
        if not (len(pText) % self.r) == 0:
            pText = self.Pad(pText)

        cText = ''
        for i in range(0, len(pText), self.r):
            l = []
            for ch in pText[i:i+self.r]: l.append(self.ALPHA.find(ch))
            vector = np.array(l).reshape(self.r,1)
            c = self.keyMatrix.dot(vector)
            for cChar in c: cText += self.ALPHA[cChar[0]%26]
        return cText

    np.set_printoptions(suppress=True)
    def decrypt(self, cText):
        cText = cText.lower()
        det = int(np.linalg.det(self.keyMatrix))
        ADJ = np.round(np.linalg.inv(self.keyMatrix) * det).astype(int)
        ADJ = ADJ % 26
        det = det % 26
        det = inverse(det, 26)
        inv = det * ADJ
        inv %= 26

        pText = ''
        for i in range(0, len(cText), self.r):
            l = []
            for ch in cText[i:i+self.r]: l.append(self.ALPHA.find(ch))
            vector = np.array(l).reshape(self.r,1)
            c = inv.dot(vector)
            for cChar in c:
                pText += self.ALPHA[round(cChar[0])%26]
        return pText

f = open('keyHill')
x = Hill(f)
print(x.encrypt('aybcmwdofz'))
print(x.decrypt('odqtxxdioasggzod'))