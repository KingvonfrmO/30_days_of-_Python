import math

#Day 2: 30 days of Python

#Declaring Variables
First_name = 'Jeffery'
Last_name = 'Mutuku'
Full_name = First_name + Last_name
Country = 'Kenya'
City = 'Nairobi'
age = 20
year = 2023
is_married = 'Yes'
is_true = True
is_light_on = False
a, b, c = 1, 2, 3

#Checking the type of variables
print(type(First_name))
print(type(Last_name))
print(type(Full_name))
print(type(Country))
print(type(City))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(a))

#find the length of your first name
print(len(First_name))

#Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
print(num_one + num_two)  # Addition
print(num_one - num_two)  # Subtraction
print(num_one * num_two)  # Multiplication
print(num_one % num_two)  # Modulus
print(num_one / num_two)  # Division
print(num_one ** num_two)  # Exponential
print(num_one // num_two)  # Floor division

#area of circle
radius = 30
area_of_circle = math.pi * radius ** 2
print(area_of_circle)

#Circumfrence of circle
circum_of_circle = math.pi * (radius * 2)

#user_radius and calculate the area
user_radius = int(input("Enter Your radius: "))
area_of_circle = math.pi * user_radius ** 2
print(area_of_circle)


