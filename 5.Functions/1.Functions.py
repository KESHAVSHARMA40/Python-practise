#  Functions 


def calculate_Total(price, quantity):
   return price*quantity

if __name__ == "__main__":
   price = int(input("Enter the price: "))
   quantity = int(input("Enter the quantity: "))

   total = calculate_Total(price,quantity)
   print("Total is:",total)

# 1. Default parameters
def greet(name="Guest"):
    return f"Hello, {name}"

FName = input("Enter your name: ")

print(greet())
print(greet(FName))


# 2. Keyword Arguments
def profile(name, age, city):
    print(name, age, city)

profile(age=22, name="Keshav", city="Toronto")

name= input("Enter your name: ")
age= int(input("Enter your age: "))
city= input("Enter your city: ")

profile(age=age, name=name,city=city)

# 3. *args --> multiple positional arguments

def total(*nums):
    return sum(nums)

print(total(10,20,30,40,50,60))

# 4. **kwargs --> multiple keyword arguments

def details(**info):
    print(info)
phone = int(input("Enter phone number: "))
Dob = input("Enter Dob: ")
email = input("Enter email: ")

details(phone= phone, Dob= Dob, email=email)


# 5. Functions calling other functions 
def cal_tax(amount):
    return amount * 0.18

def final(amount):
    return amount + cal_tax(amount)

amount = int(input("Enter the amount: "))
print(final(amount))

# 6. Functions with multiple returns

def student_marks(maths, science, eng):
    total = maths + science + eng
    avg = total / 3
    return total, avg
    
t, a = student_marks(90, 85, 88)

print(t,a)

# 7. Function as a reusable utilities

def discount(price):
    if price >1000:
        return price * 0.8
    elif price >500:
        return price * 0.9
    return price

price = int(input("Enter the price: "))
print(discount(price))

# 8. Anonymous Functions(lambda)

square = lambda x:x*x
print(square(5))

abc = int(input("Enter the number: "))
print(square(abc))