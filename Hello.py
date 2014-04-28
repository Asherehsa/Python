#function with default value for an argument
def power(num, x=1):
    result = 1;
    for i in range(x):
        result = result * num
    return result

#function with variable number of args
def multiAdd(*args):
    result = 0;
    for x in args:
        result = result + x
    return result

print power(2)
print power(2,3)
print power(x=4, num=2)

print multiAdd(4,5,10,4)
