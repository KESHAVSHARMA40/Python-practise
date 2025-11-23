#  In this we will see the dictionaries within dictionaries.

Portfolio = {
  "Name" : "Keshav",
  "Age" : 21,
  "Gender" : "M", 
  "languages_Learnt" : [
    "Python", "HTML5", "CSS", "GITHUB"
                       ],
  "Profile" : { 
    "UserId" : 101,
    "Password" : "JackyChan"

  }
}

print(Portfolio["Profile"]["UserId"])
print(Portfolio["languages_Learnt"])


# 1️⃣ Create a dictionary for a student: name, age, grade. Print all values.
# 2️⃣ Update the grade in the dictionary.
# 3️⃣ Add a new key "passed": True.


Student = {
  "Name" : "Shubham", 
  "Age" : 25,
  "Grade" : 78
}
Student 

for k,v in Student.items() :
  print(k,":",v)

# 4️⃣ Given this dict:
emp = {"id":101, "name":"Amit", "salary":50000}

# Increase salary by 10%.
NewSalary = (emp["salary"] + (emp["salary"] *10/100))
print(NewSalary)

# 5️⃣ Use .get() to safely access "bonus" key.
print(emp.get("Bonus"))



# 7️⃣ Store 3 users in a dictionary, each user itself being a dictionary.

Profile = {
  "User1" : {
      "UserId" : 1,
      "JobRole" : "Developer",
      "Salary" : 40000
  },
  "User2" : {
      "UserId" : 2,
      "JobRole" : "IT Support",
      "Salary" : 20000
  },
  "User3" : {
      "UserId" : 3,
      "JobRole" : "Marketing Manager",
      "Salary" : 50000
  }
}
print(Profile["User1"])
print(Profile["User2"])
print(Profile["User3"])



# 8️⃣ Extract the second skill from this:
dev = {"name":"Keshav", "skills":["Python","SQL","Git"]}

Answer = (dev["skills"][1])
print(Answer)


# 9️⃣ From this JSON-like dict:
api = {
    "status": 200,
    "data": {
        "user": {
            "name": "Raj",
            "active": True
        }
    }
}
# Print the username and active status.

print(api["data"]["user"]["name"])
print(api["data"]["user"]["active"])

# 🔟 Convert two lists:
keys = ["name","age","city"]
values = ["Keshav",22,"Delhi"]

# Into a dictionary without using loops.

result = dict(zip(keys,values))
print(result)