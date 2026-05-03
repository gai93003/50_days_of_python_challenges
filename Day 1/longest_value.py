# Write a function called "longest_value" takes takes a dictionary as an argument and returns the first longest value of the dictionary. For example, the following dictionary should return - Apple as the longest value.
fruits = {"fruit": "apple", "color": "green"}

def longest_value(d: dict):
    # Using max and key len to get the longest value
    longest = max(d.values(), key=len)
    
    return longest
print(longest_value(fruits))