# program.py
from datetime import date

sum = 1 + 2
print(sum)

print("show this in the console")

sum = 1 + 2 # 3
product = sum * 2
print(product)

planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string

print(planets_in_solar_system)
print(distance_to_alpha_centauri)
print(can_liftoff)
print(shuttle_landed_on_the_moon)

print(type(distance_to_alpha_centauri)) ## <class 'float'>

left_side = 10
right_side = 5
print(left_side / right_side) # 2

print(date.today())

print("Today's date is: " + str(date.today()))

parsecs = 11
lightyears = 11 * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")

# entradas de datos
print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings " + name)

##
print("calculator program")
first_number = input("first number: ")
second_number = input("second number: ")
print(int(first_number) + int(second_number))

##
parsecs_input = input("Input number of parsecs:")
parsecs = int(parsecs_input)
lightyears = 3.26156 * parsecs

print(parsecs_input + " parsecs is " + str(lightyears) + " lightyears")

print("1" + 2)