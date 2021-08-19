types_of_people = 10
x = f"There are {types_of_people} types of people."
#There are 10 types of people.

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
#Those who know binary and those who don't.

print(x)
print(y)
#print x and y

print(f"I said: {x}")
print(f"I also said: '{y}'")
#print stuff before + x and + y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))
#print joke evaluation first then print the status of hilarious

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
#print w and e, string concatenation