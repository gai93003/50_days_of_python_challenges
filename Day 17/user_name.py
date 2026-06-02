############# Day 17: User Name Generator ##############

# Write a function called "user_name", that creates a username for the user. The function should ask a user to input their name. 
# The function should then reverse the name and attach a randomly issued number between 0 - 9 at the end of the name. The function should return the username.
import random
def user_name():
    name = input("Enter your name: ")[::-1]
    randomNum = random.randint(0, 9)

    return f"{name}{randomNum}"


# Prevent the print statement from running during testing.

if __name__ == "__main__":
    print(user_name())