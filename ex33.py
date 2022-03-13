numbers = []

def expand(space, interval):
    i = 0
    while i < space:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + interval
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

expand(5,1)
print("The numbers: ")

for num in numbers:
    print(num)
