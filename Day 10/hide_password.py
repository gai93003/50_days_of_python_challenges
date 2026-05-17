################ Day 10: Hide my Password #####################

# Write a function called "hide_password" that takes no parameters. The function takes an input (a password) from a user and returns a hidden password. For example, if the user enters "hello" as a password the function should return "****" as a password and the user that the password is 4 characters long.

def hide_password(password):
    arr = [letter.replace(letter, "*") for letter in list(password)]

    return "".join(arr)

print(hide_password("hello"))    