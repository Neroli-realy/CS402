class PlayFair:
    def __init__(self, key):
        self.pc = self.PlayfairKey()
        self.pc.buildKeymatrix(key)

    def encrypt(self, plaintext=None, fileIN=None, fileOUT=None):
        if fileIN:
            plaintext = fileIN.read()

        plaintext = plaintext.strip().lower()
        res = ''
        i = 0
        while i < len(plaintext)-1:
            if plaintext[i] == plaintext[i+1]:
                res += self.pc.encrypt(plaintext[i], 'x')
                i+=1
            else:
                res += self.pc.encrypt(plaintext[i], plaintext[i+1])
                i+=2
            if i == len(plaintext)-1:
                res += self.pc.encrypt(plaintext[i], 'z')
        if fileOUT:
            fileOUT.write(res)
            fileOUT.close()
            return

        return res

    def decrypt(self, ciphertext=None, fileIN=None, fileOUT=None):
        if fileIN:
            ciphertext = fileIN.read()
        ciphertext = ciphertext.strip().lower()
        res =''
        for i in range(0,len(ciphertext), 2):
            res += self.pc.decrypt(ciphertext[i], ciphertext[i+1])
        if fileOUT:
            fileOUT.write(res)
            fileOUT.close()
            return
        return res

    class PlayfairKey:
        def __init__(self):
            self.matrix = [[0 for i in range(5)] for x in range(5)]

        def buildKeymatrix(self, key):
            alpha = {}
            for i in key:
                alpha[i] = 0
            c = 'j'
            if key.find('j') != -1: c = 'i'
            for i in range(97, 123):
                if alpha.get(chr(i), -1) == -1 and not i == ord(c):
                    alpha[chr(i)] = 0

            alpha = list(alpha)
            index = 0
            for i in range(5):
                for j in range(5):
                    self.matrix[i][j] = alpha[index]
                    index += 1

        def findChar(self, c):
            for i in range(5):
                for j in range(5):
                    if(self.matrix[i][j] == c):
                        return (i,j)

        def encrypt(self, a, b):
            ch1X ,ch1Y = self.findChar(a)
            ch2X, ch2Y = self.findChar(b)

            if ch1X == ch2X:
                ch1Y = (ch1Y + 1) % 5
                ch2Y = (ch2Y + 1) % 5
            elif ch1Y == ch2Y:
                ch1X = (ch1X + 1) % 5
                ch2X = (ch2X + 1) % 5
            else:
                t = ch1Y
                ch1Y = ch2Y
                ch2Y = t

            return  self.matrix[ch1X][ch1Y] +self.matrix[ch2X][ch2Y]

        def decrypt(self, a, b):
            ch1X ,ch1Y = self.findChar(a)
            ch2X, ch2Y = self.findChar(b)

            if ch1X == ch2X:
                ch1Y = (ch1Y - 1) % 5
                ch2Y = (ch2Y - 1) % 5
            elif ch1Y == ch2Y:
                ch1X = (ch1X - 1) % 5
                ch2X = (ch2X - 1) % 5
            else:
                t = ch1Y
                ch1Y = ch2Y
                ch2Y = t

            return    self.matrix[ch1X][ch1Y] + self.matrix[ch2X][ch2Y]

print(PlayFair('gravity').encrypt('cryptographyandnetworksecurity'))