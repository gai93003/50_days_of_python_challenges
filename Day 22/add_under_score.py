########## Day 22: Add Under_Score ############

# Create three functions. The first called "add_hash" takes a string and adds a hash "#" between the words.
# The second function called "add_underscore" removes the hash (#) and replaces it with an underscore "_".
# The third function called "remove_underscore", removes the underscore and replaces it with nothing. If you pass "Python" as an argument for the three functions, and you call them at the same time like:
# print(remove_underscore(add_underscore(add_hash("Python")))) it should return "Python".

def add_hash(str1):
    new_str = list(str1)

    result = f"#".join(new_str)

    return result

def add_underscore(str2):
    new_str = str2.replace("#", "_")

    return new_str

def remove_underscore(str3):
    new_str = str3.replace("_", "")

    return new_str

# print(add_hash("Python"))
# print(add_underscore("P#y#t#h#o#n"))
# print(remove_underscore("P_y_t_h_o_n"))

print(remove_underscore(add_underscore(add_hash("Python"))))