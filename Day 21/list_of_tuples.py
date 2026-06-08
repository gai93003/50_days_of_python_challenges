######### Day 21: List of Tuples ###########

# Write a function called "make_tuples" that takes two lists, equal lists, and combines them into a list of tuples. For example, if list a is [1,2,3,4] and list b is [5,6,7,8], your function should return [(1,5), (2,6), (3,7), (4,8)].

def make_tuples(list1, list2):
    new_list = []

    if len(list1) != len(list2):
        return "The two lists should have equal lengths"

    for item in range(len(list1)):
        new_list.append((list1[item], list2[item]))

    return new_list

fst = [1,2,3,4]
snd = [5,6,7,8]
rd = [9, 2, 3]

print(make_tuples(fst, snd))

print(make_tuples(fst, rd))