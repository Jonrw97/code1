from sys import argv

script, filename = argv   #argv variables

print(f"We're going to erase {filename}.") #f string
print("If you don't want that hit CTRL-C (^c).")
print("If you don't want that, hit RETURN")

input("?")

print("opening file...")
target = open(filename, 'w') #file getting opened / open has added codes, w = writing x = create new file  these must be used if you intend to write or etc as it will return an error

print("Truncating the file. Goodbye!")
target.truncate()                            #empting file

print("Now I'm going to ask you for three lines")

line1 = input("Line 1: ")   #input
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file,")

target.write(f"{line1}\n{line2}\n{line3}")  # Lines being written in with a single argument using f-string /(alternative but ineffiecnt)using + escapes must have " " when using variables


print("And finally we close it so we can read it,")
target.close()

file = open(filename) #when re opening a file it must be given a new variable as previous variable is lost when file is closed

print(file.read())
