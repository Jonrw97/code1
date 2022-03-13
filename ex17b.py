from sys import argv; script, from_file, to_file = argv; print(f"Coping {from_file} to {to_file}\nComplete"); in_data = open(from_file).read(); out_file = open(to_file, 'w').write(in_data)

# when you add .write/read etc. to a file being open it doesnt need to be closed as it closes itself after the action
#; seperates code as if it were on a new line
