from sys import argv

from os.path import exists

script, from_file, to_file = argv

print ("Copying from %s to %s" % (from_file, to_file))

indata = open(from_file).read()

'''
print ("The input file is %d bytes long" % len(indata))

print ("Does the output file exist? %r" % exists(to_file))
print ("Ready, hit RETURN to continue, CTRL- C to abort.")
input()
'''

out_file = open(to_file, 'w')
out_file.write(indata)

print ("Alright, all done.")

out_file.close()
#close open file
#study drill 1: tried, done, deleted back to prevent confusion

'''
This  package  provides a class to manage the plugins for the import of
tables of contents from other formats, i.e. their conversion from,  for
example doctoc, json, etc.
'''

'''
open(input("tofile"), 'w').write(open(input("fromfile")).read())
'''

'''
cat: concatenate and print files
     The cat utility reads files sequentially, writing them to the standard
     output.  The file operands are processed in command-line order.  If file
     is a single dash (`-') or absent, cat reads from the standard input.  If
     file is a UNIX domain socket, cat connects to it and then reads it until
     EOF.  This complements the UNIX domain binding capability available in
     inetd(8).
'''

'''
drill5
windows ppl: The cat utility reads files sequentially, writing them to the standard output. The file operands are processed in command-line order.

'''

'''
as a file is opened in write, it is locked for writing. so if you dont close it, you cant ahve access to the file outside the program while it's open in python
'''