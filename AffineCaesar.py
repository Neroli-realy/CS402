from Crypto.Util.number import inverse

class AffineCaesar:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def encrypt(self, plainText=None, fileIn=None, fileOut=None):
        if fileIn:
            plainText = fileIn.read().strip().lower()
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        res = ''
        for i in plainText:
            res += alpha[((self.a * alpha.find(i))+self.b) % 26]

        if fileOut:
            fileOut.write(res)
            fileOut.close()
            return
        else:
            return res

    def decrypt(self, ciphertext=None, fileIn=None, fileOut=None):
        if fileIn:
            ciphertext = fileIn.read().strip().lower()
        res = ''
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        # modinv in this case is so easy to bruteforce since it's from 1 to 25
        for i in ciphertext:
            res += alpha[(inverse(self.a, 26) * (alpha.find(i) - self.b)) % 26]

        if fileOut:
            fileOut.write(res)
            fileOut.close()
            return
        else:
            return res
x = AffineCaesar(7,20).encrypt(plainText='cryptographyandnetworksecurity')
print(x)
print(AffineCaesar(7,20).decrypt(ciphertext=x))
