def add(a, b):
    print ("ADDING %d + %d" % (a, b))
    return a + b

def subtract(a, b):
    print ("SUBTRACTING %d - %d" % (a, b))
    return a -b

def multiply(a, b):
    print ("MULTIPLYING %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print ("DIVIDING %d / %d" % (a, b))
    return a / b

#1
def mod(a, b):
    print ("Remainder %d / %d" % (a, b))
    return a % b

print ("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print ("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))


# A puzzle for the extra credit, type it in anyway. 2
print ("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print ("That becomes: ", what, "Can you do it by hand?")

#2
print(age+(height-weight*(iq/2)))

#3
print(age-(height-weight*(iq/2)))
print(add(age, subtract(age, multiply(weight, divide(iq, 2)))))

print(1+2-1)
print(add(1, subtract(2,1)))