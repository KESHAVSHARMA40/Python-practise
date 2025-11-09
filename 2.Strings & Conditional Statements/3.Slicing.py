# Slicing the process in which a particular value has been taken from the string.

A = "Hello_World"

print(A[-3:-1])

print(A[:5])
print(A[-5:])

# What is slicing, and how is it related to indexing?
# Slicing gives the multiple values from a string or list whereas Indexing gives ony one value at a time.


# Can you change a character in a string using indexing? Why or why not?
# No, the character cannot be changed directly using the indexing method but can be changed by creating a new variable

Word = "hello"
print(Word[0])
NewWord = "H" + Word[1:]
print(NewWord[0])
# Given a list nums = [10, 20, 30, 40], what does nums[-2] return?
nums = [10, 20, 30, 40]
print(nums[-2]) #It will give the output as 30.

# What’s the difference between nums[0:3] and nums[:3]?
# there is no such difference between the both, the final answer will be the same.

# If you get an IndexError, what’s the likely cause?
# The cause for the IndexError in the case of indexing could be most probably due to the out of limit indexing.