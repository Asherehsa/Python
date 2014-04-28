__author__ = 'Asher'

def main():
    x = 0
    #while loop, prints 1-4
    while (x < 5):
        print x
        x = x + 1

    #for loop (iterator)
    for x in range(5, 10): #not inclusive of 10
        print(x)

    #for loop over a collection
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for d in days:
        print d

    #break and continue
    for x in range(5,10):
        if (x == 7): break
        if (x % 2 == 0): continue #skips print statement on even numbers
        print x

    #using enumberate()
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


if __name__ = "__main__":
    main()