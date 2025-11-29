students = {
                "Roll" : {
                            "Details" : {}
                         }
            }

while True:
    print("\n1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update information")
    print("5. Delete Student")
    print("6. Exit")
    

    choice = int(input("Enter choice: "))

    if choice == 1:
                Roll = int(input("Enter your Roll number: "))
                name = input("Please Enter the name of the student: ")
                age = int(input("Please enter the age of the student: "))
                city = input("Enter your city: ")
                students[Roll] = {
                      "Name" : name,
                      "Age" : age,
                      "City" : city
                }
                print("Thank you for filling the details")

    elif choice == 2:

            for roll, details in students.items():
                  print(f"\nRoll: {roll}")
                  for keys, values in details.items() :
                       print(f"{keys}: {values}")

    elif choice == 3:
            
              roll = int(input("Enter the roll number:"))
              if roll in students:
                    print(students[Roll])
              else:
                    print("Student not found")
              
              
    elif choice == 4:
              
                roll = int(input("Enter roll number to update: "))
                if roll in students:
                    students[roll]["name"] = input("New name: ")
                    students[roll]["age"] = int(input("New age: "))
                    students[roll]["city"] = input("New city: ")
                    print("Updated!")
                else:
                    print("Not found.")

       
    elif choice == 5:

                roll = int(input("Enter roll number to delete: "))
                if roll in students:
                        del students[roll]
                        print("Deleted!")
                else:
                        print("Student not found.")


    elif choice == 6:
        break
    else :
        print("Invalid choice, TRY-AGAIN")
        break
