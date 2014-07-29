__author__ = 'Asher'

def main():
    #Declare the things!
    myMessage = 'Avi is handsome'
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    print(ciphertext + '|')

def encryptMessage(key, message):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message): #keep looping until pointer goes past the length of the message
            ciphertext[col] += message[pointer]
            pointer += key
    return ''.join(ciphertext)
if __name__ == '__main__':
    main()