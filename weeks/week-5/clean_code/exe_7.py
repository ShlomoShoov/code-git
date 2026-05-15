TAX = 0.17


def processart(prices,quantities,user_type):
  
  total=0

  for i in range(len(prices)):
    price =prices[i]
    quantity=quantities[i]
    total=total+price*quantity

  # add totalax
  total = total + total * TAX

  #we shold give him discunt if he premium user
  if user_type=='premium':
    total=total*0.9

  # better diccunt to vip user
  elif user_type=='vip':
    total = total * 0.8

  # chake if the customer should pay for his delivery

  # 500 and up - shipping free
  if total>500:
    shipping=0

  # 25 if between 200 to 500

  elif total > 200:
    shipping = 25

  # otherwise full price
  else:
    shipping=50

  total=total+shipping

  
  return total
