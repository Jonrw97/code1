from sys import argv

script,input_file = argv  #argv to give files when programme is run

def print_all(f):
    #print("<<<< print_all: f=",f)
    print(f.read()) # function created to read a file when print_all is inputed
    #print(">>>> print_all: f=",f)

def rewind(f):
    #print("<<<< rewind: f=",f)
    f.seek(0) # function to rewind file?how does this work exactly
    #print(">>>> rewind: f=",f)

def print_a_line(line_count, f):
    #print("<<<< print_a_line: f=",f)
    #print("<<<< print_a_line: line_count=",line_count)
    print(line_count,f.readline()) # function to read exactly one line anywhere in the file aslong as line number is given
    #print(">>>> print_a_line: f=",f)
    #print(">>>> print_a_line: line_count",line_count)

current_file = open(input_file)

print("First let's print the whole file:\n") # file is printed out in full
print_all(current_file)

print("Now lets rewind, kind of like a tape.")# file gets set back to begining
rewind(current_file)

print("lets print 3 lines.")  # !!!current_line doesnt do anything other than just print a number readline just prints a single line based on where you are in the file!!!

current_line = 1
print_a_line(current_line,current_file)# first line is printed with current_line being 1

current_line += 1
print_a_line(current_line,current_file)# second line printed Current_line is 2

current_line += 1
print_a_line(current_line,current_file)# Third line current_file is 3
