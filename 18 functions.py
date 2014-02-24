def print_two(*args):
    arg1, arg2 = args
    print "argl: %r, arg2: %r" % (arg1, arg2)
# *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#for only one arg
def print_one(arg1):
    print "arg1: %r" % arg1

#This takes no args
def print_none():
    print "I got nothin'."

print_two("Asher", "Bunny")
print_two_again("Asher", "Bunny")
print_one("Asher!")
print_none()