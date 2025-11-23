# This is the file for the dictionaries. 

#  Dictionaries as a english words means that Looking for the meaning (Value) using a word (Key).

#  This acts as a mini Database in python. For storing data in a dictionary.
#  it can be empty or non-empty dictionary.

#  This is a empty dictionary Empty_Dict = {}. 
#  This is a non empty dictionary Dict = {
#                                           "Name" : "Keshav",
#                                        }

user = {
    "name": "Keshav",
    "age": 22,
    "country": "India"
}
# This will print the exact format.
print(user)

# This will print the key only.
for data in user :
   print(data)

# This will print the values only.
for data in user.values() :
  print(data)

# This will print both the key and values.
for k,v in user.items():
   print(k,":",v)

# Accessing a single value from the whole table.

demo = {
   "Name" : "Keshav Sharma",
   "Age" : 21,
   "Gender" : "M" 
   }

print(demo["Name"])
print(demo["Age"])

# Adding a key and a value to the existing dictionary.

demo["Remarks"] = "Good" # Adding a new data. 
demo["Age"] = 22 # Updating the existing data.

print(demo["Remarks"])
print(demo["Age"])

# If in case the key does not exists in the data provided.
# demo["Marks"] This is show error. 
#  instead use .Get to get the response as a value or none.
demo.get("Marks") # MAKE SURE TO USE CURLY BRACES INSTEAD OF SQUARE BRACES.

# To remove the key we use .pop method

demo.pop("Age")
# print(demo["Age"]) Running this will now give an error in the terminal.
