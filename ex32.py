the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for- loop goes through a list
for number in the_count:
    print ("This is count %d" % number)

# same as above
for fruit in fruits:
    print ("A fruit of type: %s" % fruit)

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print ("I got %r" % i)

# we can also build lists, first start with an empty one
elements = []
'''
# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print ("Adding %d to the list." % i)
    # append is a function that lists understand
    elements.append(i)
'''
elements=range(0,6)

# now we can print them out too
for i in elements:
    print ("Element was: %d" % i)

#1. range is a sequence of numbers, from 0 by default, increments by 1 and stops before a specified number, when there are two numbers, it starts from the first number and ends before the second one
#2. yes it works
#3. extend, insert, remove, pop, count, etc