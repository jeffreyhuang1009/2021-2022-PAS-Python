#a formatter where we can insert stuff
formatter = "{} {} {} {}"

#print stuff by filling in spaces, the stuff is after the parenthesis in .format
print(formatter.format(1, 2, 3, 4))
#print stuff by filling in spaces, the stuff is after the parenthesis in .format
print(formatter.format("one", "two", "three", "four"))
#print stuff by filling in spaces, the stuff is after the parenthesis in .format
print(formatter.format(True, False, False, True))
#print stuff by filling in spaces, the stuff is after the parenthesis in .format
print(formatter.format(formatter, formatter, formatter, formatter))
#print stuff by filling in spaces, the stuff is after the parenthesis in .format
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
