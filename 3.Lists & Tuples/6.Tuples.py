#  Tuples 

#  Must remember to put the "  ,  " after adding a single value to create a tuple.
#  for example A = (1,) THIS IS A TUPLE Value.

tup = (1,)
print(tup)
print(type(tup))

A = (1,2,3,4,5,6,7,1,2,3,4,5,6,7,8,9)
print(A.count(3))


#  Tuple unpacking 

def get_user():
  return ("Keshav", 22,"India")

name, age, country = get_user()

print(name)
print(age)
print(country)

#  Question for practice
# You received this tuple from an API:
# response = ("Keshav Sharma", 200, True)

def data(): 
  return ("Keshav Sharma", 200, True)

name, r_Value, B_value = data()

print(name,r_Value,B_value)


