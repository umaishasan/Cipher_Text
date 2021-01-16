from main import CipherTexts

class CaeserCipherText(CipherTexts):
    def __init__(self,plaintext):
        self.plaintext = plaintext

    def encrypt(self):
        self.keyword()
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
        self.cipher = []
        for i in self.plaintext:
            for j in range(len(alphabet)):
                if i in alphabet[j]:
                    self.cipher = alphabet[j].replace(alphabet[j],self.aa[j])
                    self.decrypt(self.cipher)

    def keyword(self):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
        key = []
        for j in range(7, 26):
            key.append(alphabet[j])
        for k in range(7):
            key.append(alphabet[k])
        self.aa = key

    def decrypt(self,a):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
        for i in a:
            for j in range(len(self.aa)):
                if i in self.aa[j]:
                    d=self.aa[j].replace(self.aa[j],alphabet[j])
                    print("Encrypted Text: ",i,", Decrypted Text: ",d)