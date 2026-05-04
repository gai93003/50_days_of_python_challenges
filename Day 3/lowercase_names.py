################ Lowercase Names ###############

# You are given a list of names above. This list is made up of names of lowercase and uppercase letters. Your task is to write a code that will return a tuple of all the names in the list that have only lowercase letters. Your tuple should have names sorted alphabetically in descending order. Using the list above, your code should return:
n = ['kerry', 'dickson', 'John', 'Mary', 'carol', 'Rose', 'adam']
# ('kerry', 'dickson', 'carol', 'adam')


def register_check(names):
    lower = tuple(name for name in names if name[0].islower())

    return lower

print(register_check(n))