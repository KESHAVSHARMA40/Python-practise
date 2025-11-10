# String datatype has few functions that can be used in the various scenarios.

#  Upper() ## This will convert all the characters from lower to upper case.
FirstName = "Keshav"
print(f"My Name is {FirstName}")
FirstName = FirstName.upper()
print(f"My Name is {FirstName}")

#  Lower() ## This will convert all the characters lowercase

Password = "MaN_iS_POWer_FUll_IN_the_woRlD"
print(Password)
Password = Password.lower()
print(Password)

# Title() ## This will capitalize the first letter of each word.

LastName = "sharma"
print(LastName.title())

#  Strip() ##This will remove the extra space from the front and back of the word.
Word = "   Hello Keshav, How are you doing?  "
print(Word)
print(Word.strip())

#  Replace() ## This will replace the old letter or word with the new one.
Statement1 = "Hey, I am sure you will be doing good in the exams"
Statement2 = "Yes, I know that the exams are going to be easy for me"
print(f"{Statement1} \n  {Statement2}")
Statement1 = Statement1.replace("exams","examination")
Statement2 = Statement2.replace("exams","examination")
print(f"{Statement1} \n  {Statement2}")


# Find() ## This will help to find the word in the sentence or -1 if not found.
print(Statement1.find("doing"))
print(Statement2.find("easy"))

#  Startswith() and Endswith()

print(Statement1.startswith("Hey"))
print(Statement1.startswith("Hello"))

# "-".Join([],[],[])  ## This will join the elements of the list into a string.

A = (["2025", "10","06"])
DateA = "-".join(A)
print(DateA)

# Q-1 Cleaning and formatting the user Input before saving that into the database.

# FName = input("Please enter your firstname: ")
# LName = input("Please enter your last name: ")
# print(FName +" "+ LName)
# FullName = (FName + " "+ LName).strip().title()
# print(FullName)

#Q-2 Get the user input for the password in uppercase only and also make sure the password should contain only string datatype.
P1 = input("Enter your password in uppercase only using string values: ")
P1 = P1.upper().strip()
print(f"Your Password is {P1}")
