# Create an empty list
empty_1 = []
empty_2 = list()

# create a list with some items
fruits = ["apple", "banana", "orange"]

# access by index
fruits[0]

# reassign value at index
fruits[1] = "plum"
print(fruits)

# get the number in items
num_of_fruits = len(fruits)

# remove last element
removed_fruit = fruits.pop()
print(f"I removed {removed_fruit}")

# add a new fruit
fruits.append("pear")
print(fruits)

