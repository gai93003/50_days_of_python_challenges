######## Extra Challenge: Even Number or Average #########

# Write a function called "even_or_average" that ask a user to input five numbers. Once the user is done, the code should return the largest even number in the inputted numbers. If there is no even number in the list, the code should return the average of all the five numbers.

def even_or_average():
    user_inputs = list(input("Please enter 5 numbers: "))
    numbers = [int(num) for num in user_inputs]
    sums = sum(numbers)

    even_num = 0

    for num in numbers:
        if num % 2 == 0:
            if num > even_num:
                even_num = num

    aveage_nums = sums / len(numbers)

    if even_num == 0:
        return aveage_nums
    else:
        return even_num


print(even_or_average())