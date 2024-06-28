import math

#The operands are 3 & 4
print(4 + 3)  # Addition
print(4 - 3)  # Subtraction
print(4 * 3)  # Multiplication
print(4 % 3)  # Modulus
print(4 / 3)  # Division
print(4 ** 3)  # Exponential
print(4 // 3)  # Floor division

#Write strings in python
print("Jeffery")  # Name
print("Mutuku")  # Last Name
print("Kenya")  # Country
print("I am enjoying 30 days of python")  # string

#Check the Data types
print(type(10))  # integer
print(type(9.8))  # float
print(type(True))  # Boolean
print(type(4 - 4j))  # complex
print(type(['Jeffery', 'Python', 'Kenya']))  # list
print(type((1, 2, 3)))  # tuple
print(type({'Name': 'Jeffery', 'Age': '20'}))  # dictionary
print(type({1, 2, 3}))

#Find an Euclidian distance between (2, 3) and (10, 8)
a = (10, 8)
b = (2, 3)
print(math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2))
