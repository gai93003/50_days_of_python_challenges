########### Day 16: Sum the List ################

# Write a function called "sum_list" with one parameter that takes a nested list of integers as an argument and returns the sum of the integers. For example, if you pass [[2, 4, 5, 6], [2, 3, 5, 6]] as an argument your function should return a sum of 33.

nested_list = [[2, 4, 5, 6], [2, 3, 5, 6]]

def sum_list(lst):
    new_list = [number for item in lst for number in item]

    return sum(new_list)

print(sum_list(nested_list))