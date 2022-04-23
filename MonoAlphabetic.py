class MonoAlphabetic:
    def __init__(self, key):
        self.key = key.strip().lower()

    def encrypt(self, plaintext=None, fileIn=None, fileOut=None):
        if fileIn:
            plaintext = fileIn.read().strip().lower()

        #assuming that the key will be all the alpha in different order
        alpha = ''.join(sorted(self.key))
        res = ''.join([self.key[alpha.find(i)] for i in plaintext])

        if fileOut:
            fileOut.write(res)
            fileOut.close()
            return
        else:
            return res

    def decrypt(self, ciphertext=None, fileIn=None, fileOut=None):
        if fileIn:
            ciphertext = fileIn.read().strip().lower()

        alpha = ''.join(sorted(self.key))
        res = ''
        for c in ciphertext:
            res += alpha[self.find(c)]

        if fileOut:
            fileOut.write(res)
            fileOut.close()
            return
        else:
            return res