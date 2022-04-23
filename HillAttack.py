import numpy as np
import math
import string
from Crypto.Util.number import inverse


class HillAttack:

    def __init__(self):
        self.r = None
        self.ALPHA = string.ascii_lowercase
    def textToMatrix(self, t):
        res =np.array([], dtype=int)
        self.r = int(math.sqrt(len(t)))
        for i in t: res = np.append(res, self.ALPHA.find(i))
        res = res.reshape(self.r, self.r)
        return res


    def attack(self, plainTextFile, cipherTextFile):
        #pText = plainTextFile.read().lower()
        #cText = cipherTextFile.read().lower()

        pText = 'hill'
        cText = 'hcrz'
        pTextMatrix = self.textToMatrix(pText)

        det = int(np.linalg.det(pTextMatrix))
        ADJ = np.round(np.linalg.inv(pTextMatrix) * det).astype(int)
        ADJ = ADJ % 26
        det = det % 26
        det = inverse(det, 26)
        inv = det * ADJ
        inv %= 26
        keyM = np.array([])
        for i in range(0, len(cText), self.r):
            l = []
            for ch in cText[i:i+self.r]: l.append(self.ALPHA.find(ch))
            vector = np.array(l).reshape(self.r,1)
            vv = ((inv.dot(vector) % 26).transpose(1,0))
            if(len(keyM) == 0): keyM = vv
            else: keyM = np.vstack([keyM, vv])
        return keyM

x = HillAttack()
print(x.attack('', ''))