########### Day 20: Capitalize First Letter ############

# Write a function called capitalize. This function takes a string as an argument and capitalizes the first letter of each word. For example, 'i like learning' becomes 'I Like Learning'.

def capitalize(str1):
    new_str = [word.capitalize() for word in str1.split()]

    return f" ".join(new_str)


str1 = 'i like learning'

print(capitalize(str1))