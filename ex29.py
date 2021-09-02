people = 20
cats = 30
dogs = 15


if people < cats:
    print ("Too many cats! The world is doomed!")

if people > cats:
    print ("Not many cats! The world is saved!")

if people < dogs:
    print ("The world is drooled on!")

if people > dogs:
    print ("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print ("People are less than or equal to dogs.")


if people != dogs:
    print ("People are dogs.")

'''
1. it only lets the code under it run if the conditions in the if statement is met
2. i think it must be indented, since there aren't {}s so far, python doesn't know what codes r under the if statement, so indented lines means they are under the if statement
3. if it isn't indented, then it isn't in the if statement
4. tried
5. Then, depending on what the values are, the conditions may or may not be met, and ther may or may not be different outoput, as in some wouldn't print
'''