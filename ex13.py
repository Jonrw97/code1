from sys import argv

script, first, second, third, fourth = argv  #variables are given when running the script on the command line !!only when argv is used!!
name = input("what is your name?")

print(f"{name}'s script is called:", script)
print(f"{name}'s first variable is:", first)
print(f"{name}'s second variable is:", second)
print(f"{name}'s third variable is:", third)
print(f"{name}'s fourth variable is:", fourth)
