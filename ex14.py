from sys import argv
script, user_name, item = argv
prompt = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questiosn.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"where do you live {user_name}?")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
Next you have started with a {item} in your inventory.
What do you wish to do with this item?
""")
use= input(prompt)

print(f" you use your {item} to {use} it breaks!")
