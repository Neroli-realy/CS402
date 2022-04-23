from MonoAlphabetic import MonoAlphabetic
class MonoAlphabeticAttack:

    def attack(self, knownPlainText=None, knownCipherText=None, ciphertext=None,
               knownPlainTextFile=None, knownCipherTextFile=None, ciphertextFile=None, fileOut=None):

        #assuming that kplaintext is 26 char

        if knownPlainTextFile:
            knownPlainText = knownPlainTextFile.read()
            knownCipherText  = knownCipherTextFile.read()
            ciphertext = ciphertextFile.read()

        keydict = {}
        knownPlainText = knownPlainText.strip().lower()
        knownCipherText = knownCipherText.strip().lower()
        ciphertext = ciphertext.strip().lower()

        for i in range(97, 123):
            keydict[chr(i)] =  knownPlainText[knownCipherText.find(chr(i))]

        res = ''
        for c in ciphertext:
            res += keydict.get(c, ' ')

        if fileOut:
            fileOut.write(res)
            fileOut.close()
            return
        else:
            return res

