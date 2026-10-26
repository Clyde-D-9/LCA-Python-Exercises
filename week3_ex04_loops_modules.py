# Question 1: Using a for loop with a list

fruits = ("apple", "orange", "mango", "peach", "grape", "banana")

for fruit in fruits:
    print(fruit)

# Question 2: Using a while loop for countdown

i = 5

while i>=1:
    print(i)
    i=i-1

# Question 3: Using a for loop with range()

for number in range(1, 11):
    print(number ** 2)

# Question 4: Using the random module

import random

Colours = ("red", "blue", "yellow", "purple", "green", "orange", "pink", "brown", "black", "white")

for i in range(3):
    print(random.choice(Colours))

# Question 5: Creating and using a custom module

import math_operations

print("Addition", math_operations.add(10, 5))
print("Subtraction", math_operations.subtract(10, 5))
print("Multiplication", math_operations.multiply(10, 5))
print("Division", math_operations.divide(10, 5))

while True:
    print("\n--Simple Calculator--")
    print("1, Addition")
    print("2, Subtraction")
    print("3, Multiplication")
    print("4, Division")
    print("5, Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "5":
        print("Exiting calculator.")
        break

    if choice not in ("1", "2", "3", "4"):
        print("Invalid choice. Please choose a valid option.")
        continue

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

    if choice == "1":
        result = math_operations.add(num1, num2)
    elif choice == "2":
        result = math_operations.subtract(num1, num2)
    elif choice == "3":
        result = math_operations.multiply(num1, num2)
    elif choice == "4":
        result = math_operations.divide(num1, num2)

    print("Result: ", result)
