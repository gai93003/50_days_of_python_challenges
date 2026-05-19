##################### Day 11: Are They Equal #######################

# Write a function called "equal_strings". The function takes two strings as arguments and compares them. If the strings are equal (if the have the same characters and have equal length), it should return True, if they are not, it should return False. For example, "love" and "evol" should return True

def equal_strings(str1, str2):
    str1 = sorted(str1.lower())
    str2 = sorted(str2.lower())

    if str1 == str2:
        return True
    else: 
        return False
    
print(equal_strings("love", "evoL"))