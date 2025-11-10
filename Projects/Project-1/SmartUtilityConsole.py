print("\t\t\tWelcome to Smart Utility Console \n\t\tYour one-stop solution for all the essential tools")

# --------------------------------------------------------------------------------------------#
App1 = print("1. Discount Calculator")
App2 = print("2. Loan Eligibility Calculator")
App3 = print("3. Electricity Bill Calculator")

# --------------------------------------------------------------------------------------------#
SelectedApp = int(input("Please enter the number for your selection: "))
if ( 0 < SelectedApp <= 3): 
  print(f"You have selected : {SelectedApp}")
else :
  print("Invalid Selection, please try again!")

# --------------------------------------------------------------------------------------------#
if SelectedApp == 1:
    print("Welcome to Discount Calculator")
    TotalAmount = int(input("Please enter the total amount of purchase: "))

    if TotalAmount > 10000:
        print("You are eligible for a 20'%' discount on your bill")
        Bill = TotalAmount - (TotalAmount * 20 / 100)
    elif TotalAmount > 5000:
        print("You are eligible for a 10'%' discount on your bill")
        Bill = TotalAmount - (TotalAmount * 10 / 100)
    else:
        print("You are not eligible for any discount")
        Bill = TotalAmount

    print(f"Your total payable amount is ${Bill}")

# --------------------------------------------------------------------------------------------#

elif SelectedApp == 2 : 
     print("Welcome to Loan Eligibility Calculator")
     Age = int(input("please enter your age: "))
     Income = float(input("please enter your income: "))
     Credit_Score =int(input("Please enter your Credit Score: "))
     if Age >= 21 and Income >=25000 and Credit_Score >=650 :
       print("You are eligible")
    
     else:
       print("You are not eligible") 

# --------------------------------------------------------------------------------------------#

elif SelectedApp == 3 : 
      print("Welcome to Electricity Bill Calculator")
      Units = int(input("Please enter the Units utilized: "))
      if Units <= 100 :
       print("You will be charged $5 per unit")
       Amount = 5 * Units
       print("$",Amount + 50)
      elif 100 < Units <=200 :
       print("You will be charged $7 per unit")
       Amount = 7 * Units
       print("$",Amount + 50)
      else : 
       print("You will be charged $10 per unit")
       Amount = 10 * Units
       print("$", Amount +50)

# --------------------------------------------------------------------------------------------#

else :
   print("Thank You!") 