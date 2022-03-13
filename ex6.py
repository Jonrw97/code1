types_of_people = 10  # variable given an amount
x = f"there are {types_of_people} types of people" #variable given a phrase with previous variable included

binary = "binary" #variable
do_not = "don't" #variable

y = f"Those who know {binary} and those who {do_not}." # same as x variable but 2 included variables

print(x) # x variable is printed out
print(y) # same as x just wit y variable

print(f"I said: '{x}'") # python code used with in string to show x variable
print(f"I also said: '{y}'") # same as line 12 just with y variable

hilarious = False # hilarious given value false
joke_evaluation = "Isn't that joke funny?! {}" # joke_evaluation given value with 2 braces for future string

print(joke_evaluation.format(hilarious)) # joke_evaluation variable inputed with python code format() to show hilarious variable value

w= "This is the left side of..." # variable given value
e = "a string with a rightside." # variable given value
print(w+e) # 2 variables printed to create alonger string
