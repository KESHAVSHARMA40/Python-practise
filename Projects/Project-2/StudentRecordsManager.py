students = {
                "Roll" : {
                            "Details" : {}
                         }
            }

while True:
    print("\n1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Analytics")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
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

    elif choice == "2":

            for roll, details in students.items():
                  print(f"\nRoll: {roll}")
            for keys, values in details.items() :
                  print(f"{keys.capitalize}: {values}")

    elif choice == "3":
            
              search = input("Please enter the name of the student you want to search for: ")
              for s,v in students,students.values():
                    if students.get("Name") == search :
                          print(s,":",v)
              
              
              
                    
        
              
    elif choice == "4":
        pass  # TODO: update
    elif choice == "5":
        pass  # TODO: delete
    elif choice == "6":
        pass  # TODO: analytics
    elif choice == "7":
        break
    else :
        break
