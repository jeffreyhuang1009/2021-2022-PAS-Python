tabby_cat = "\tI'm tabbed in."
persian_cat="I'm split\non a line."
backslash_cat="I'm \\\n \ta\t \\\n cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* catnip\n\t*Grass
'''

print (tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


#know the escape sequences
#\\ Backslash (\)
#\' Single-quote (') \" Double-quote (")
#\a ASCII bell (BEL)
#\b ASCII backspace (BS)
#\f ASCII formfeed (FF)
#\n ASCII linefeed (LF)
#\N{name} Character named name in the Unicode database (Unicode only) \r ASCII carriage return (CR)
#\t ASCII horizontal tab (TAB)
#\uxxxx Character with 16-bit hex value xxxx (Unicode only) \Uxxxxxxxx Character with 32-bit hex value xxxxxxxx (Unicode only) \v ASCII vertical tab (VT)
#\ooo Character with octal value oo
#\xhh Character with hex value hh
#double quote and single quotes are the same
#%s uses the str function and %r uses the repr function
#%s is just plain text, %r is text with '' around it