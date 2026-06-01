############### Extra Challenge: What's my Age? ###############

# Write a function called "your_age". This function asks a student to enter their name and then it returns their age. 
# For example, if a user enters Peter as their name, your function should return, "Hi, Peter, you are 27 years old."
# This function reads dat from the database (dictionary below). If the name is not in the dictionary, your code should tell the user that their name is not in the dictionary, and ask them for their age.
# Your code should then add the name and age to the dictionary of names_age below.
# Once added your code should return to the user "Hi, (added name), you are (added age) years old". Remember to convert the input from user to lowercase letters

names_age = {
    "jane": 23,
    "kerry": 45,
    "tim": 34,
    "peter": 27
}

def your_age():

    while True:
        nam = input("Enter your name: ").lower()

        if nam in names_age:
            return f"Hi, {nam}, you are {names_age[nam]} years old."
        else:
            age = int(input("Enter your age: "))

            names_age[nam] = age

            print("Name successfully added, try again.")


print(your_age())