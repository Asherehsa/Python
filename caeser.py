__author__ = 'Asher'

message = 'This is my secret message.'

key = 13

mode = 'encrypt' # encrypt or decrypt

#All the things
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789?.'

# ze end result
translated = ''

#capatalize all the strings!
message = message.upper()

#loop for all the things
for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol) #get
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        #wrap it around
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        translated = translated + LETTERS[num]
    else:
        translated = translated + symbol
print(translated)