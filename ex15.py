#import stuff
from sys import argv

#unpacking stuff
script, filename = argv

#call function on txt
txt = open(filename)

#print filename
print("Here's your file %r: "%(filename))
#print what it reads in the file
print(txt.read())
#prints stuff
print("type filename again:")
#filename is what u input again
file_again = input("> ")
#txtagain calls an open function on the file
txt_again = open(file_again)
#print what it reads
print(txt_again.read())
