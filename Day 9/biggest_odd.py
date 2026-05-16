################ Day 9: Biggest Odd Number ##################

# Create a function called "biggest_odd" that takes a string of numbers and returns the biggest odd number in the list. For example, if you pass "23569" as an argument, your function should return 9. Use list comprehension.

def biggest_odd(nums):
    arr = list(nums)

    odd_nums = [num for num in arr if int(num) % 2 == 1]

    return max(odd_nums)


biggest_odd("23569")