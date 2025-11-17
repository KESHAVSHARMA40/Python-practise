# Looping Through the lists

names_list_of_20 = [
    "Alexander", "Olivia", "Benjamin", "Charlotte", "Daniel",
    "Emily", "Felix", "Grace", "Henry", "Isabelle",
    "Jacob", "Katherine", "Liam", "Mia", "Noah",
    "Penelope", "Quinn", "Ryan", "Sophia", "Thomas"
]

names_list_of_20.sort()

#  if we use print directly it will be 
print(f"Sending email to: ", names_list_of_20)


# if we use looping it will be 
for Names in names_list_of_20 :
  
  print(f"Sending email to: ", Names)


# Example of list of students failing in exams
Marks = [100, 80, 44, 22, 55, 78, 12, 33]
for Results in Marks :
  if (Results > 33) :
    print(f"Pass")
  else :
    print(f"Fail")

emails = ["abc@", "xyz@gmail.com", "", "test", "user@mail.com"]

valid = [e for e in emails if "@" in e]

for Verified in valid:
  print(f"These are the valid email formats: ", Verified)


#  Looping a nested lists
m = [[1,2,3],[4,5,6],[7,8,9]]

# Loop through each row:
for rows in m :
  print(rows)

# Loop through every value:
for rows in m :
    for items in rows :
      print(items)