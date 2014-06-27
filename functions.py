import math

#declare thingies
line1 = 'Bang tiddle '
line2 = 'tiddle bang.'

#Define functions
def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and work all day."

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    print_lyrics()

#parameters/arguments
def print_twice(bruce):
    print bruce
    print bruce
    
def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

#call functions
repeat_lyrics()
print_twice('Asher '*3)
cat_twice(line1, line2)
