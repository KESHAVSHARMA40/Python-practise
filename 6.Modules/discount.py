def calculate_discount(price):
    
    if price >= 50000 :
        final_price = price - (price * 0.40)
        return final_price
    elif price >= 25000 :
          final_price = price - (price * 0.30)
          return final_price
    elif price >= 10000 :
          final_price = price - (price * 0.20)
          return final_price
    elif price >= 5000 :
          final_price = price - (price * 0.10)
          return final_price
    elif  price <=5000 :
          return price
    
def discount_given(price, percent): 
     
      total = price - (price * (percent/100))
      return total