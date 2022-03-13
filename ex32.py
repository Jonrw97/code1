the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this kind of for-loop goes through a list

for number in the_count:
    print(f"This is count {number}")

#same as above

for fruit in fruits:
    print(f"Types of fruit: {fruit}")

#also we can go through mixed lists

for i in change:
    print(f"I have {i}")

#we can also build lists, first start with an empty done
elements = []

#then use the range function to do 0 to 5 counts

for i in range(0,6):
    print(f"adding {i} to the list")
    #append is used to add things from a list to another list.
    elements.append(i)

#now it can get printed about
for i in elements:
    print(f"Element was: {i}")

space = range(5,60,5)

for num in space:
    print(f"groups {num}")
