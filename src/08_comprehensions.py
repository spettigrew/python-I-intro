"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [1, 2, 3, 4, 5]

print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
y = [0-9]
square = [x**3 for x in range(10)]
print(square)
#squares = [x**2 for x in range(10)]

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [x.upper() for x in ["foo","bar","baz"]]
#y = [name.capitalize() for name in a if name[0].upper() == 'B']

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')
print(x)
#evens = [num for num in x if num % 2 == 0]
#print(evens)

# What do you need between the square brackets to make it work? Pulls out the even numbers, from previous function when you type numbers separated by commas in the terminal.
y = [int(value) for value in x if int(value) % 2 == 0]

print(y)