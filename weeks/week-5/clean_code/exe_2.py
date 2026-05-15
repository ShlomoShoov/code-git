def email_valided(user_email):
    if user_email:
        return True
    else:
        return False

def quantity_valided(quantity,stock):
        if quantity <= 0 or quantity > stock:
            return False
        else:
            return True
        
def calculate_price(product_price,quantity):
    price = product_price * quantity
    if quantity >= 10:
        price *= 0.9
    if quantity >= 50:
        price *= 0.85
    return price

def handle_purchase(user_email, product_name, product_price, stock, quantity):

    if not email_valided(user_email):
        print("Invalid user")
        return None
    
    if not quantity_valided(quantity=quantity,
                            stock=stock):
        print("Invalid quantity")
        return None

    price = calculate_price(product_price,quantity)

    stock -= quantity

    order_user = user_email
    order_product = product_name
    order_quantity = quantity
    order_total = price
    order_status = "confirmed"
    print(f"Order {order_status}: {order_user} bought {order_quantity}x {order_product} for ${order_total}")
    return order_user, order_product, order_quantity, order_total, order_status
