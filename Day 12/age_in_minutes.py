############ Extra Challenge: Your Age in Minutes ###############

# Write a function called age_in_minutes that tells a user how old they are in minutes. Your code should ask the user to enter their year of birth, and it should return their age in minuts (by subtracking their year of birth from the current year).

# Here are the things to look out for:

# a) The user can only input a 4-digit year of birth. For example, 1930 is a valid year. However, entering any number longer or less than 4 digits long should render input invalid. Notify the user to input a four digits number.

# b) If a user enters a year before 1900, your code should tell the user that input is invalid. If the user enters the year after the current year, the code should tell the user, to input a valid year.

# The code should run until the user inputs a valid year. Your function should return the user's age in minutes. For example, if someone enters 1930, as their year of birth your function should return: 

# You are 48,355,200 minutes old.

from datetime import datetime

def your_age():
    while True:
        birth_year = input('Enter your year of birth: ')
        if len(birth_year) != 4:
            print('Please enter a four digits year')
        elif int(birth_year) < 1900 or int(birth_year) > 2026:
            print('Please enter a valid year')
        else:
            # This returns the current year
            now1 = int(datetime.now().strftime("%Y"))
            age = (now1 - int(birth_year)) * 525600
            return f'You are {age:,} minutes old.'
  
  
print(your_age())