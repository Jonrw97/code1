name = 'Jonathan Watkins'
age = 35
height = round( 74 * 2.54 ) #centimeters
weight = round( 180 * 0.45 ) # kilograms
eyes = 'blue'
teeth = 'White'
hair = 'Brown'

print("Let's talk about {name}.")
print(f"He's {height} centimeters tall.")
print(f"He's {weight} Kilograms heavy.")
print("Actually that's not that heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it right.

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} i get {total}.")
