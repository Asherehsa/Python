import math

__author__ = 'Asher'

def main():
    message = 'Cenoonommstmme oo snnio. s s c'
    key = 8

    plaintext = decryptMessage(key, message)

    print(plaintext+'|')

def decryptMessage(key, message):
    numColumns = math.ceil(len(message)/key)
    numRows = key
    numShaded = (numColumns * numRows) - len(message)
    plaintext = [''] * numColumns

    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1 #next column

        #if there are no more columns or we're at shaded box go to 1st column of the next row
        if (col == numColumns) or (col == numColumns - 1 and row >= numRows - numShaded):
            col = 0
            row += 1
    return ''.join(plaintext)

if __name__ == '__main__':
    main()