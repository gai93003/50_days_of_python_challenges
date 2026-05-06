############## Day 4: Only Floats ##############

# Write a function called "only_floats", which takes two parameters a and b, and return 2 if both arguments are floats, return 1 if only the argument is a float, and return 0 if neither argument is a float. If you pass(12.1, 23) as an argument, you function should return a 1.


def only_floats(num1, num2):
    if isinstance(num1, float) and isinstance(num2, float):
        return 2
    else:
        return 1
    

print(only_floats(12.1, 23))
print(only_floats(2.2, 4.3))