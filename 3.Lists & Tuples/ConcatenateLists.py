a = [1,2]
b = [3,4]
c = a + b

print(c)
print(a)
print(b)
b = a.copy()
print(b)
a.extend(b)
print(a)

# You receive a list of order amounts:
Order = [1200,350,899,1500]
# Check the orders eligible for discounts 
discounted = [o for o in Order if o>1000]
print(discounted)