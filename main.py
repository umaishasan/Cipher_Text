from abc import abstractmethod

class CipherTexts:

    @abstractmethod
    def encrypt(self):
        raise NotImplementedError("Should be define")

    @abstractmethod
    def decrypt(self,a):
        raise NotImplementedError("Should be define")

    @abstractmethod
    def keyword(self):
        raise NotImplementedError("Should be define")