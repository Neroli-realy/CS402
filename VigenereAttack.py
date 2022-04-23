import string

class VigenereAttack:


    def removePadding(self, key):
        for i in range(len(key)):
            for j in range(i+1, len(key)):
                r=  key[i:j]
                x = r
                while len(x) < len(key):
                    x += r
                if x == key:
                    return r
        return key

    def attack(self, kpText, kcText):
        ALPHA = string.ascii_lowercase
        k = ''
        kpText = kpText.lower()
        kcText = kcText.lower()
        for i in range(len(kpText)):
            k += ALPHA[(ALPHA.find(kcText[i]) - ALPHA.find(kpText[i])) % 26]
        return self.removePadding(k)


x = VigenereAttack()
print(x.attack('wearediscoveredsaveyourself', 'zicvtwqngrzgvtwavzhcqyglmgj'))