################# Day 7: A String Range ##################

# Write a function called "string_range" that takes a single number and returns a string of its range. The string characters should be seperated by dots(.) For example, if you pass 6 as an argument, you function should return '0.1.2.3.4.5'.

def string_range(num):
    num = [str(item) for item in range(0, num)]

    return ".".join(num) #" ".join(num)

print(string_range(5))