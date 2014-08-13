__author__ = 'Asher'

import random, sys, transpositionEncrypt, transpositionDecrypt

def main():
    random.seed(42) #seed of math unguessable

    for i in range(20): #20 tests
        message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * random.randint(4,40) #message of random length

        message = list(message) #convert message string to a list
        random.shuffle(message) #shuffle it
        message = ''.join(message) #and back to a string

        print('Test #%s: "%s..."' % (i+1, message[:50]))

        for key in range(1, len(message)): #check all possible keys
            encrypted = transpositionEncrypt.encryptMessage(key, message)
            decrypted = transpositionDecrypt.decryptMessage(key, encrypted)

            if message != decrypted: #Error~!
                print('Key %s mismatch with message %s.' % (key,message))
                print(decrypted)
                sys.exit()
    print('Transposition cipher test passed.')

if __name__ == '__main__':
    main()