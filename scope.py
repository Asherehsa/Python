__author__ = 'Asher'

spam = 42

def eggs():
    spam = 99 #local to this function
    print('In egg():',spam)
def ham():
    print('In ham():', spam) #spam in this function is global

def bacon():
    global spam #le global spam
    print("In bacon():", spam)
    spam = 0
#def CRASH():
#    print(spam) #local in this function
#    spam = 0

print(spam)
eggs()
print(spam)
ham()
print(spam)
bacon()
print(spam)
#CRASH()