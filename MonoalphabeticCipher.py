from main import CipherTexts

class MonoalphabeticCipherText(CipherTexts):
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
                    a = alphabet[j].replace(alphabet[j], self.key[j])
                    self.cipher.append(a)
        for i in self.cipher:
            print(i,end=" ")

    def keyword(self):
        self.key = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

    def decrypt(self):
        self.keyword()
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
        result = []
        for i in self.cipher:
            for j in range(len(self.key)):
                if i in self.key[j]:
                    b = self.key[j].replace(self.key[j],alphabet[j])
                    result.append(b)
        for i in result:
            print(i,end=" ")