# # Swap two variables without using a third variable.

A = 4
B = 2
A = A-B
B = A*B
print(A,B)

# # Take user input for name and age, then print:
# # "Hello <name>, you will turn 100 in the year <year>."
import datetime
FirstName = input("Enter your First Name:")
Age = int(input("Enter your Age:"))
DoB = int(datetime.datetime.now().year)
Year = int(DoB + (100 - Age))
print(f"Hello,{FirstName}, you will turn 100 in the year {Year}")


# Write a program to check whether a number is even or odd using conditionals.

A = int(input("Enter a random number:"))

if A % 2 == 0 :
   print ("Number is even")
elif A % 2 != 0:
   print("Number is odd")

# Input three numbers and print the largest one.
Num1 = int(input("Enter a random number:"))
Num2 = int(input("Enter a random number:"))
Num3 = int(input("Enter a random number:"))
print(f"You have entered three numbers that is {Num1},{Num2},{Num3}")
print("Now let's find out which number is largest")
if(Num1>Num2 and Num1>Num3):
   print(f"The number {Num1} is the largest number")
elif(Num2>Num3 and Num2>Num1):
   print(f"The number {Num2} is the largest number")
else:
   print(f"The number {Num3} is the largest number")


