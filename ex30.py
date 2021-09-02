#objective of the code: set variable values, use if elif else by comparing > < or == of the variables and print stuff accordingly

people = 300
cars = 40
buses = 40

#will print We should not take the cars
if cars > people:
    print ("We should take the cars.")
elif cars < people:
    print ("We should not take the cars.")
else:
    print ("We can't decide.")

#will print We still can't decide
if buses > cars:
    print ("That's too many buses.")
elif buses < cars:
    print ("Maybe we could take the buses.")
else:
    print ("We still can't decide.")

#will print Alright, let's just take the buses
if people > buses:
    print ("Alright, let's just take the buses.")
else:
    print ("Fine, let's stay home then.")

#will print THEN HmMmMmMmmmm
if cars > people and buses < cars:
    print("then hmmmmm")
else:
    print("THEN HmMmMmMmmmm")

'''
1. elif means, if the if condition isn't met, then it will go to the elif condition to see if it applies, and finally, when everything doesn't apply, it's else, it doesn't have a condition
2. yeah, i did that
3. the last one, i did it
4. tina said we dont have to comment everything, objective of program stated on first line
'''