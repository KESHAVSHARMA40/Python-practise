# 1️⃣ Create a function that returns a salary slip:

# Input → basic salary
# Output → total salary after HRA, PF, Bonus.

def salary_slip(base_salary):
  hra = base_salary * 0.20
  pf = base_salary * 0.12
  bonus = base_salary *0.10

  final_salary = base_salary + hra + bonus - pf

  return {

    "Basic Salary": base_salary,
    "HRA": hra,
    "PF": pf,
    "Bonus": bonus,
    "Final_Salary": final_salary
  }


print(salary_slip(50000))


# 2️⃣ Create a function that takes unlimited numbers and returns:

# max

# min

# average

# Use *args.


def numbs(*args):
  maximum = max(args)
  minimum = min(args)
  avg = sum(args) / len(args)

  return maximum, minimum, avg

print(numbs(10,20,30,40,50,60))



# 3️⃣ Write a function that validates a signup form:

# Inputs:

# email

# password

# age

# Return:

# True/False

# error message if any


def signup(email, password, age):
  if "@" not in email:
     return False, "Invalid Email"
  
  if len(password) < 8:
     return False, "Password too short"
  
  if age < 18:
     return False, "Under 18"
  
  return True, "Signup Successful"

print(signup("test@gmail.com", "Helloworld", 22))




# 4️⃣ Build a mini “billing system”:

# Function receives:

# product name

# quantity

# price

# Returns a dictionary:

# {
#   "name": ...,
#   "total": ...
# }



def Billing(product_name, quantity, price):
    total = quantity * price

    return {
       "Item": product_name,
       "Quantity": quantity,
       "Price": price,
       "Total": total
    }

print(Billing("Pen", 5, 10))

