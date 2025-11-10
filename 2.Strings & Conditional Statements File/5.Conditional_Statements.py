# Operator	  Meaning	                        Example
# ==	        Equal to	                      a == b
# !=	        Not equal to	                  a != b
# <	          Less than	                      a < b
# >	          Greater than	                  a > b
# <=	        Less than or equal to	          a <= b
# >=	        Greater than or equal to	      a >= b
# and	        Both conditions must be True	  x > 0 and y > 0
# or	        Either condition can be True	  x > 0 or y > 0
# not	        Negates condition	not           x == 5


# Q-1 Ask the user for a number and check if it’s positive, negative, or zero.

# Num1 = int(input("Enter a random number: "))

# if Num1 > 0:
#   print("The number entered is positive")
# elif Num1 <0:
#   print("The number entered is Negative")
# else :
#   print("The number entered is zero")


# Q-2 Ask for a password and check if it matches "Python@123".
# user1 = (input("Enter your username: "))
# Pass1 = (input("Enter your password: "))

# if Pass1 == "Python@123": 
#   print(f"Welcome Back! {user1}")
# else :
#   print(f"Invalid username or password, please try again")

#Q-3 Bank Loan Eligibility Check

# Input: age, income, and credit score.

# Conditions:

# Eligible if age ≥ 21, income ≥ 25,000, and credit score ≥ 650.

# Else → Not eligible.

Age = int(input("please enter your age: "))
Income = float(input("please enter your income: "))
Credit_Score =int(input("Please enter your Credit Score: "))

if Age >= 21 or Income >=25000 or Credit_Score >=650 :
  print("You are eligible")
else :
  print("You are not eligible")