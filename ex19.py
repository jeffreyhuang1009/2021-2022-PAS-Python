#defines the function of cheese and crackers, takes in two argumens, cheese and qtn of boxes
def cheese_and_crackers(cheese, boxes):
    #print sentence and variable cheese
    print("You have %d cheeses!"%cheese)
    #print sentence variable boxes
    print("You have %d boxes for crackers!"%boxes)
    #print stuff
    print("Thats enuf for a party!")
    #print stuff
    print("Get a blanket.\n")

#print stuff
print("We can just give the function numbers directly:")
#call function, with 20, 30 as arguments
cheese_and_crackers(20,30)

#print stuff
print("Or use variables from our script:")

#assign numbers to the amount of cheese and crackers, represented by two variables
amt_cheese=10
amt_crackers=50

#call the function with the two variables as arguments
cheese_and_crackers(amt_cheese, amt_crackers)

#print stuff
print("We can even do math inside too:")
#call the function with expressions as arguments
cheese_and_crackers(10+20, 5+6)

#print stuff
print("And we can combine two variables & math:")
#call function with two expressions with variables and numbers
cheese_and_crackers(amt_cheese+100, amt_crackers+1000)

#my function
def sum(n1, n2):
    print("%d + %d = "%(n1, n2), n1+n2)

#ten ways
x=1.0
y=2.0
sum(0,0)
sum(x+x,y+y)
sum(x, y+y)
sum(y+y,x)
sum(y+x, x+y)
sum(y+x, x)
sum(y, x+y)
sum(x*x, y*y)
sum(x*y, x*y)
sum(x*x*y,y)
