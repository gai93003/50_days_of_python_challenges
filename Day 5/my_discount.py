################# Day 5: My Discount #####################

# Create a function called my_discount. The function takes no arguments but asks the user to input the price and the discount (percentate) of the product. Once the user inputs the price and discount, it calculates the price after the discount. The function should return the price after the discount. For example, if the user enters 150 as price and 15% as the discount your function should return 127.5.

def my_discount():
    price = input("Please enter the price: ")
    discount = input("Please enter the discount: ")
    
    return int(price) - (int(price) * (int(discount) / 100))

print(my_discount())