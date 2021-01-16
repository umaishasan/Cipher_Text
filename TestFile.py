from timeit import default_timer as timer
from CaeserCipher import CaeserCipherText
from HillCipher import HillCipherText
from MonoalphabeticCipher import MonoalphabeticCipherText

if __name__ == '__main__':
    start = timer()
    print("Hill Cipher: ")
    obj1 = HillCipherText('att')
    print("encrypted text: ")
    obj1.encrypt()
    print("\ndecrypted text: ")
    obj1.decrypt()
    end = timer()
    print("\nHill cipher takes: ",end - start,"s")

    start = timer()
    print("\nCaeser Cipher: ")
    obj2 = CaeserCipherText('mus')
    obj2.encrypt()
    end = timer()
    print("Caeser cipher takes: ", end - start, "s")

    start = timer()
    print("\nMonoalphabetic Cipher: ")
    obj3 = MonoalphabeticCipherText('uma')
    print("Encryption: ")
    obj3.encrypt()
    print("\nDecryption: ")
    obj3.decrypt()
    end = timer()
    print("\nMonoalphabetic cipher takes: ", end - start, "s")
