############## Day 13: Pay Your Tax #################

# Write a function called "your_vat". The function takes no parameter. The function asks the user to input the price of an item and VAT(vat should be a percentage). The function should rturn the price of the item plus VAT. If the price is 220 and VAT is 15% your code should return a vat inclusive price of 253. Makesure that your code can handle ValueError. Ensure the code runs until valid numbers are entered. (Hint: Your code should include a while loop).

def your_vat():
    while True:
        price = int(input("Please enter the price: "))
        vat = int(input("Please enter your vat: "))

        if not isinstance(price, int) or not isinstance(vat, int):
            print("Please enter valid values.")
        else:
            valueVat = price * (vat / 100)

            return round(price + valueVat)
        

print(your_vat())