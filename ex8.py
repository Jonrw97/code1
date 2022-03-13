formatter = "I can say {} {} {} {} "

print(formatter.format( 1, 2, 3, 4))
print(formatter.format( "one", "two", "three", "four"))
print(formatter.format( True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
     "Sweat on my palms",
     "I cant stop thinking about my wrongs",
     "So leave me to drown in my own misery",
     "cause these cold dead hands cant go on"
))

#variable formatter has 4 {} for format to in put

# another way to debug, repr shows the string as written in python
lines = ("Sweat on my palms",
 "I cant stop thinking about my wrongs",
 "So leave me to drown in my own misery",
 "cause these cold dead hands cant go on")
#print(repr(lines))
