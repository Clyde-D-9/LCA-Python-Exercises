# Question 1: Variable Assignment and String manipulation

name = input("What is your name? ")
age = input("What is your age? ")

print("Hello, " + name + "! You are " + age + " years old.")

# Question 2: Integer Operations

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

area = length * width

print("The area of the rectangle is: " + str(area))

# Question 3: Working with Floats

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("The temperature in Fahrenheit is: ", round(fahrenheit, 2))
