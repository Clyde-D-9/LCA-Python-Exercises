# Question 1: Creating and Modifying Lists

fruitList = ["apple", "orange", "mango","banana", "grape"]

fruitList.append("peach")
fruitList.insert(0, "kiwi")
fruitList.remove("banana")

print(fruitList)

# Question 2: List Operations

numList = [1, 2, 3, 4, 5]

squaredList = [num ** 2 for num in numList]

sum = sum(numList)
average = sum / len(numList)

print("Squared List: ", squaredList)
print("Sum: ", sum)
print("Average: ", average)

# Question 3: Creating and Modifying Dictionaries

capitalsdict = {
    "South Africa": "Pretoria",
    "Japan": "Tokyo",
    "France": "Paris",
}

capitalsdict["Germany"] = "Berlin"
capitalsdict["South Africa"] = "Cape Town"
del capitalsdict["France"]

print(capitalsdict)

# Question 4: Dictionary Operations

fruitclrdict = {
  "Apple":"Red",
  "Orange":"Orange",
  "Grape":"Purple",
  "Banana":"Yellow"
}

print("Fruits:")
keys = fruitclrdict.keys()
print(keys)

print("Fruit Colours:")
values = fruitclrdict.values()
print(values)

fruit = "Grape"
if fruit in fruitclrdict:
    print(f"\nThe color of {fruit} is {fruitclrdict[fruit]}")
else:
    print(f"\n{fruit} is not in the dictionary")

