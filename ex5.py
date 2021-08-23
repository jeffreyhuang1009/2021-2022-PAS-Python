#define all the variables
name = 'Zed A. Shaw'
age = 35
height = 74
weight = 18
eyes = 'Blue'
hair = 'Brown'
teeth = 'White'

#f allows stuff like this, putting variables in strings
print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the  coffee.")

#total is sthe sum of all three
total = age + height + weight
#similar to previous printing method
print(f"If I add {age}, {height}, and {weight} I get {total}.")

incm = 2.54
lbkg = 0.45359237

print("He's %f centimeters tall." % (height * incm))
print("He's %f kilos heavy." % (weight * lbkg))