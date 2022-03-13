def add(a,b):
    print(f"Adding {a} + {b}")
    return a + b # return will give back the values when called upon they must just be given a variable

def subtract(a,b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a,b):
    print(f"Dividing {a} / {b}")
    return a / b

print("Let's do some maths with just fuctions!")

age = add(30,5) #variable age given so when age is called later it return 35 because it ran 30 + 5 in the return code
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle")

what = add(age, subtract(height,multiply(weight,divide(iq,2))))# functions can be called within fuction the are run from last inputed int the string to first inputed
print(age + height - weight * iq/2)                            # !!functions run inside out / out(inside)!!
print("That becomes:", what, "Can you do it by hand?")

print(100+25-4*56/67*70)
answer = add(100,subtract(25,multiply(4,divide(56,multiply(67,70)))))#!!!!doesnt follow bodmas!!!!
print(answer)
