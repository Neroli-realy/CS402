from AffineCaesar import AffineCaesar

class AffineCaesarAttack:

    def getCoprimes(self, y):
        res = []
        for i in range(2, y):
            cop = True
            for j in range(2, min(i,y)+1):
                if y%j == 0 and i%j == 0:
                    cop = False
            if cop:
                res.append(i)
        return res

    def attack(self, ciphertext=None, fileIn=None, fileOut=None):
        if fileIn:
            ciphertext = fileIn.read().strip().lower()
        res = []
        max = self.getCoprimes(26)
        #since a must be coprime with 26 we can reduce this outer loop
        for a in max:
            for b in range(1, 26):
                res.append('a: ' + str(a) + ' b: ' + str(b) + " " + AffineCaesar(a, b).decrypt(ciphertext=ciphertext))

        if fileOut:
            fileOut.write(''.join(i+'\n' for i in res))
            fileOut.close()
            return
        else:
            return res

print(AffineCaesarAttack().attack(ciphertext='ijgvxokjuvrguhphwxsojmqwiejyxg'))