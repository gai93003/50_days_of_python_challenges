################# Day 6: User Name Generator #################

# Write a function called "user_name" that generates a username from the user's email. The code should ask the user to input an email and the code should return everything before the @ sign as their user name. For example, if someone enters ben@gmail.com, the code should return ben as their username.

def user_name(email):
    username = email.split("@")[0]

    return f'Your user name is {username.capitalize()}'

your_email = input("Enter your email: ")
print(user_name(your_email))