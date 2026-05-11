############ Day 8: Odd and Even ################

# Write a functinon called "odd_even" that has one paramenter and takes a list of numbers as an argument. The function returns the difference between the largest even number in the list and the smallest odd number in the list. For example, if you pass [1, 2, 4, 6] as an argument the function should return 6 - 1 = 5.

def odd_even(arr):
    smallest = min(arr)
    largest = max(arr)

    return largest - smallest

print(odd_even([1, 2, 4, 6]))