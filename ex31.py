print ("You enter a dark room with two doors. Do you go through door #1 or door #2 or door sus?")

door = input("> ")

if door == "1":
    print ("There's a giant bear here eating a cheese cake. What do you do?")
    print ("1. Take the cake.")
    print ("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print ("The bear eats your face off. Good job!")
    elif bear == "2":
        print ("The bear eats your legs off. Good job!")
    else:
        print ("Well, doing %s is probably better. Bear runs away." % bear)

elif door == "2":
    print ("You stare into the endless abyss at Cthulhu's retina.")
    print ("1. Blueberries.")
    print ("2. Yellow jacket clothespins.")
    print ("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello. Good job!")
    else:
        print ("The insanity rots your eyes into a pool of muck. Good job!")

elif door == "sus":
    print ("You stare into a crowd eyeing you. In their eyes, you are very sus.")
    print ("1. Close your eyes.")
    print ("2. Leave.")

    sus = input("> ")

    if sus == "1" or sus == "2":
        print("You are boring, end of story")
    else:
        print ("Ew. why.")

else:
    print ("You stumble around and fall on a knife and die. Good job!")