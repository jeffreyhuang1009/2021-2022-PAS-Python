from sys import argv

script, filename = argv

print ("We're going to erase %r." % filename)
print ("If you don't want that, hit CTRL- C (^C).")
print ("If you do want that, hit RETURN.")

input("?")

print ("Opening the file...")
target = open(filename, 'w')
#writing file add w, overrides it

print ("Truncating the file. Goodbye!")
target.truncate()
#truncate part is unnecessary

print ("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("I'm going to write these to the file.")
target.write(line1+"\n"+line2+"\n"+line3+"\n")

print ("And finally, we close it.")
target.close()


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