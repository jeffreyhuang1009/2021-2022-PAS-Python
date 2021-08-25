#import stuff
from sys import argv

#unpack
script, input_file = argv

#define function printall that prints everything in f
def print_all(f):
    print(f.read())

#move position in file to beginning
def rewind(f):
    f.seek(0)

#print prints out, in number, the line it is reading
def print_a_line(line_count, f):
    print (line_count, f.readline())

#open file through new variable called currentfile
current_file = open(input_file)

#print stuff
print ("First let's print the whole file:\n")

#calls on printall function to print everything at th esame time
print_all(current_file)

#print stuff
print ("Now let's rewind, kind of like a tape.")

#calls on rewind and move position to beginning in currentfile
rewind(current_file)

#print stuff
print("Let's print three lines:")

#set current line to 1, which means python starts reading it from the first line
current_line = 1
#calls print a line function, prints 1 and whatever is in the first line, current line is the first parameter, line count
print_a_line(current_line, current_file)

#increment current line to 2
current_line +=1
#calls print a line function, prints 2 and whatever is in the second line, current line is the first parameter, line count
print_a_line(current_line, current_file)

#increment current line to 3
current_line += 1
#calls print a line function, prints 3 and whatever is in the third line, current line is the first parameter, line count
print_a_line(current_line, current_file)

#+= means that variable becomes that variable + something, x=x+1 is x+=1