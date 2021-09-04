#def loop(var, increment):
def loop(var):
    i = 0
    numbers = []
    for i in range(var):
        print ("At the top i is %d" % i)
        numbers.append(i)
        #i+=increment
        print ("Numbers now: ", numbers)
        print ("At the bottom i is %d" % i)


    print ("The numbers: ")

    for num in numbers:
        print (num)

#loop(69,2) 2 was the increment
loop(69)
#dont need to do increments, so i deleted the increment variable
