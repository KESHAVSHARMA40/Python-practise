# Concatenation is the process of joining the two or more string values and converting it into a single string value

FirstName = "Keshav"
LastName = "Sharma"
FullName = FirstName + " " + LastName
print(FullName)

FName = str(input("Please enter your FirstName:"))
LName = str(input("Please enter your LastName:"))
FinalName = FName + " " + LName
print(f"Please verify your fullName, is it {FinalName}?")
I1= input("Type Y if Yes or N if No: ")
Y = str("Y")
N = str("N")
if(I1 == Y):
  print("Thank you for confirming")
elif(I1 == N):
  print("Please check again")
else:
  print("Invalid Answer")


Street_Number = (input("Please enter your Street or House Number: "))
Street_Name = (input("Please enter your street name: "))
City = (input("Please enter your city: "))
PostalCode = input("Please enter your postal code: ")
Full_Address = Street_Number + " " + Street_Name + ", " + City + ", " + PostalCode
print(f"Your full address is {Full_Address}")
