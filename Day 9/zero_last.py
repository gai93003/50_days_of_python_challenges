#################### Extra Challenges: Zeros to the End ##########################

# Write a function called "zero_last". This function takes a list as argument. if a list has zeros (0), it will move them to the front of the list and maintain the order of the other numbers in the list. If there are no Zeros in the list, the function should return the original list sorted in ascending order. For example, if you pass [1, 4, 6, 0, 7, 0, 9] as an argument, your code should return [1, 4, 6, 7, 9, 0, 0]. If you pass [2, 1, 4, 7, 6] as your argument, your code should return [1, 2, 4, 6, 7].

def zeros_last(arr):
    zeros = [zero for zero in arr if zero == 0]
    nums = [num for num in arr if num != 0]

    if len(zeros) == 0:
        return sorted(nums)
    else:
        return nums + zeros

print(zeros_last([1, 4, 6, 7, 9, 0, 0]))
print(zeros_last([2, 1, 4, 7, 6]))