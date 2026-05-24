############## Day 14: Flatten the list ####################

# Write a function called "flat_list" that takes one argument, a nested list. The function converts the nest list into a one-dimension list. For example [[2, 4, 5, 6]] should return [2, 4, 5, 6].

def flat_list(arr):
    return [arrItem for item in arr for arrItem in item]

print(flat_list([[2, 4, 5, 6]]))