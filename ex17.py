from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"coping from {from_file} to {to_file}")

in_file = open(from_file)
in_data = in_file.read()

print(f"The input data is {len(in_data)} bytes long.")   # len() tells the length of a file in bytes

print(f"Does the output file exists?{exists(to_file)}")  # exists() tells if a file in in the current directory
print("Ready, hit RETURN to contine, CTRL-C to aport.")
input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print("Alright, all done.")

in_file.close()
out_file.close()
