class DESKey:

    def leftSh(self, m, n):
        return m[n::] + m[:n:]

    def Pad(self, n):
        return '0'*(64-len(n)) + n

    def __init__(self, keyFile):
        self.Key = '133457799BBCDFF1'
        self.Key = self.Pad(bin(int(self.Key,16))[2:])
        PC_1 = [57, 49, 41, 33, 25, 17, 9,
                1, 58, 50, 42, 34, 26, 18,
                10, 2, 59, 51, 43, 35, 27,
                19, 11, 3, 60, 52, 44, 36,
                63, 55, 47, 39, 31, 23, 15,
                7, 62, 54, 46, 38, 30, 22,
                14, 6, 61, 53, 45, 37, 29,
                21, 13, 5, 28, 20, 12, 4]

        PC_2 =  [14, 17, 11, 24, 1, 5,
                 3, 28, 15, 6, 21, 10,
                 23, 19, 12, 4, 26, 8,
                 16, 7, 27, 20, 13, 2,
                 41, 52, 31, 37, 47, 55,
                 30, 40, 51, 45, 33, 48,
                 44, 49, 39, 56, 34, 53,
                 46, 42, 50, 36, 29, 32]


        keyP = ['0' for _ in range(56)]
        for i in range(len(PC_1)):
            keyP[i] = self.Key[PC_1[i]-1]

        keyL = keyP[0:28]
        keyR = keyP[28:]
        keysList = []
        for i in range(16):
            if i in [0, 1, 8, 15]: j = 1
            else: j = 2
            keyL = self.leftSh(keyL, j)
            keyR = self.leftSh(keyR, j)
            keysList.append(keyL + keyR)

        keyP2List = [['0' for _ in range(48)]for _ in range(16)]
        for i in range(16):
            for j in range(len(PC_2)):
                keyP2List[i][j] = keysList[i][PC_2[j]-1]


        f = open('out.txt', 'w')
        for i in keyP2List:
            f.write(hex(int(''.join(i),2))[2:] + '\n')
        f.close()

x = DESKey('')







