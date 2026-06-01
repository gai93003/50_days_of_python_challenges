############# Extra Challenge: Unpack A Nested ################

# Write a code that generates a list of the following numbers from the nested list above -34, 67, 78. You oput shuld be another: [34, 67, 78]. The list output should not have duplicates.

nested_list = [[12, 34, 56, 67], [34, 68, 78]]

def add_num(lst):
    new_list = []

    for num in lst:
        for item in num:
            if item in [34, 67, 78]:
                if item not in new_list:
                    new_list.append(item)

    return new_list

print(add_num(nested_list))