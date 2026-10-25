# Question 1: Basic Function Definition and Calling

def greet():
    print("Hello World!")
    
greet()

# Question 2: Function with Parameters

def personalized_greeting(name):
    print("Hello, " + name)

personalized_greeting("Clyde")

# Question 3: Function with Return Value

def square(num):
    return num * num

result = square(5)
print(result)

# Question 4: Function with Multiple Parameters and Return Value

def rectangle_area(length, width):
    return length * width

area = rectangle_area(4, 5)
print(area)

# Question 5: Using a Function as an Argument

def apply_operation(function, number):
    return function(number)

def double(num):
    return num * 2

print (apply_operation(double, 7))
print (apply_operation(square, 3))
