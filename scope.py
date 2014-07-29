__author__ = 'Asher'

spam = 42

def eggs():
    spam = 99 #local to this function
    print('In egg():',spam)
def ham():
    print('In ham():', spam) #spam in this function is global
    
