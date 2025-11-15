# A list is a container that stores multiple in one variable.

fruits = ["Apple", "Mango", "Banana"]

# How to find the first fruit?

print(fruits[0])
print(fruits[1])

# modifying new items to the existing data of the list.
fruits[2] = "Watermelon"

print(fruits)

# append() Adding items at the end of the list 
fruits.append("Orange")

print(fruits)

# insert() adds items to the specific index
fruits.insert(5,"Guava")

# remove() removes first value in the list


# pop() removes items at the specific index 
last = fruits.pop()   #Guava removed
first = fruits.pop(0) #Apple removed

# sort() sorts list in the ascending order
fruits.sort()
print(fruits)

# reverse 
fruits.reverse()
print(fruits)

# len() length of the list
print(len(fruits))