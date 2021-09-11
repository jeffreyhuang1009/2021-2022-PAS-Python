ten_things = "Apples Oranges Crows Telephone Light Sugar"

print ("Wait there's not 10 things in that list, let's fix that.")

stuff = ten_things.split(' ')
#split(' ', tenthings)
#split when see ' '
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
#length of stuff
    next_one = more_stuff.pop()
    #pop(more_stuff)
    #records last value and pops it from more_stuff
    print ("Adding: ", next_one)
    #add next_one to end of stuff
    stuff.append(next_one)
    print ("There's %d items now." % len(stuff))

print ("There we go: ", stuff)

print ("Let's do some things with stuff.")

print (stuff[1])
print (stuff[- 1]) # whoa! fancy
print (stuff.pop())
print (' '.join(stuff)) # what? cool!
#join each element by ' '
#join(' ', stuff)
print ('#'.join(stuff[3:5])) # super stellar!
#join('#',stuff[3:5])
#use # to join stuff from 3 to 4 inclusive


#dir returns list of the attributes and methods of any object, which is created thru class
