def calculate_discount(price, discount_percent):
    if discount_percent >=  0.2:
        discount = discount_percent * price
        last_price = price - discount
        return last_price
    else:
        return price
    
print(f"The answer is {calculate_discount(1000, 0.1)}")


#QUESTION 2
def calculate_discount():
        price = int(input("Enter the price of the commodity : "))
        discount_percent = float(input("Enter the discount given for the product : "))
        if discount_percent >= 0.1:
            discount = discount_percent * price
            last_price = price - discount
            return last_price
        else:
             return price
             
print(f"The price of the commodity is {calculate_discount()}")