from main import CipherTexts

class HillCipherText(CipherTexts):
    def __init__(self,plaintext):
        self.plaintext = plaintext

    def encrypt(self):
        self.keyword()
        self.caal = []
        sepratePlaintext = []
        f=[]
        p=[]
        pickPlainText = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
        for i in self.plaintext:
            for j in range(len(pickPlainText)):
                if i == pickPlainText[j]:
                    f.append(j)
        sepratePlaintext.append(f)
        result1 = [[0,0,0]]
        for i in range(len(sepratePlaintext)):
            for j in range(len(self.key[0])):
                for k in range(len(self.key)):
                    result1[i][j] += sepratePlaintext[i][k] * self.key[k][j]
        for i in range(1):
            for j in range(3):
                t = result1[i][j]
                u = t % 26
                print(pickPlainText[u],end=" ")
                p.append(u)
            self.caal.append(p)

    def keyword(self):
        self.key=[[3,10,20],
                  [20,9,17],
                  [9,4,17]]

    def decrypt(self):
        self.keyword()
        self.encrypt()
        keyAD = []
        keyInv = []
        result2 = [[0, 0, 0]]
        det,dmi = 0,0
        pickPlainText = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
        for i in range(3):
            det = (det + (self.key[0][i] * (self.key[1][(i + 1) % 3] * self.key[2][(i + 2) % 3] - self.key[1][(i + 2) % 3] * self.key[2][(i + 1) % 3]))) % 26
        for i in range(10):
            if (((det * i) % 26) == 1):
                dmi = i
        for i in range(len(self.key)):
            h = []
            for j in range(len(self.key)):
                s = ((self.key[(j + 1) % 3][(i + 1) % 3] * self.key[(j + 2) % 3][(i + 2) % 3]) - (
                            self.key[(j + 2) % 3][(i + 1) % 3] * self.key[(j + 1) % 3][(i + 2) % 3]))
                h.append(s)
            keyAD.append(h)
        for i in range(len(self.key)):
            h = []
            for j in range(len(self.key)):
                s = (((self.key[(j + 1) % 3][(i + 1) % 3] * self.key[(j + 2) % 3][(i + 2) % 3]) - (
                            self.key[(j + 2) % 3][(i + 1) % 3] * self.key[(j + 1) % 3][(i + 2) % 3])) * (dmi))%26
                h.append(s)
            keyInv.append(h)
        #for key inverse print
        # for i in keyInv:
        #     print(i)
        for i in range(len(self.caal)):
            for j in range(len(keyInv[0])):
                for k in range(len(keyInv)):
                    result2[i][j] += self.caal[i][k] * keyInv[k][j]
        for i in range(1):
            for j in range(3):
                t = result2[i][j]
                u = t % 26
                print(pickPlainText[u], end=" ")
                # print("\n",u, end=" ")

