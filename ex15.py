from sys import argv

script,filename = argv   #argv given parameters when program is run on terminal

txt = open(filename)  #open() opens a file to be used until given a comand    !!!! file must be opened before anything else can be done to file!!!!

print(f"Here's your file {filename}:")
print(txt.read())                      #read command will read file that has been opened
txt.close()
print("Type the filename again:")
file_again = input('>')

txt_again = open(file_again)

print(txt_again.read))
txt_again.close()                           #close command closes files after use  !! remember to close files once you have finished with them
