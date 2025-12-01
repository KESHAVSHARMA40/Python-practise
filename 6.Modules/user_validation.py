def user_validation(email, password):
   if "@" not in email :
      return False, print("Email is Invalid")
   
   if len(password) >8:
      print("Password is strong")
   else :
      return False, print("Password is weak")
   