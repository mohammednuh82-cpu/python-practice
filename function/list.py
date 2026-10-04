# Python Lists
# A list stores multiple values in one variable.

fruits = ["apple", "banana", "mango", "orange"]

print(fruits)

# Accessing items
print(fruits[0])
print(fruits[2])

# Adding an item
fruits.append("grapes")
print(fruits)

# Changing an item
fruits[1] = "watermelon"
print(fruits)

# Removing an item
fruits.remove("orange")
print(fruits)

# Number of items
print("Total fruits:", len(fruits))

# Loop through a list
for fruit in fruits:
    print(fruit)

# Checking if an item exists
if "mango" in fruits:
    print("Mango is available")
