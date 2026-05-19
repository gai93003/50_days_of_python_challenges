################ Extra Challenges: Swap Values #####################

# Write a function called "swap_values". This function takes a list of numbers and swaps the first and the last element. For example, if you pass [2, 4, 67, 7] as a parameter, your function should return [7, 4, 67, 2]

def swap_values(arr):
    first = arr[0]
    last =  arr[-1]

    arr[0] = last
    arr[-1] = first

    return arr

print(swap_values([2, 4, 67, 7]))

    