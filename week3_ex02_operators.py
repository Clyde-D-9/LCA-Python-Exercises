# Question 1: Arithmetric and Assignment Operators

x = 10
y = 5

x += 3
y *= 2

result = x / y

print(result)

# Question 2: Comparison and Logical Operators

a = 10
b = 20
c = 5

condition_1 = a > b
condition_2 = b % 2 == 0
condition_3 = c <= a

final_condition = condition_1 or (condition_2 and condition_3)

print(final_condition)

# Question 3: Conditional Statements

score = int(input("What is your test score from 0-100?"))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is: ", grade)

# Question 4: Combining Operators and Conditionals

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

operation = input("Choose an operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2 
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        result = "Error: Division by zero is not allowed."
    else:
        result = num1 / num2
else:
    result = "Error: Invalid operation."

print(result)