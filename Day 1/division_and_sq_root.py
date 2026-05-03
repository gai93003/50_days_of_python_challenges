# Write a function called "divide_or_square" that takes one argument(a number), and returns the square root of the number if it is divisible by 5, returns its remainder if it is not divisible by 5. For example, if you pass 10 as an argument, then you function should return 3.16 as the square root.

def divide_or_square(num):
    reminder = num % 5
    sqrt = num ** 0.5

    if reminder == 0:
        return f'The square-root of {num} if {round(sqrt, 2)}'
    else:
        return f'The reminder of {num} divide by 5 is {reminder}'
    
    
print(divide_or_square(11))
print(divide_or_square(10))