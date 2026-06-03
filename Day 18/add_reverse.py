########### Extra Challenge: Add and Reverse #############

# Write a function called "add_reverse". This function takes two lists as argument and adds each corresponding number, and reverses the outcome. For example if you pass [10, 12, 34] and [12, 56, 78]. Your code should return [112, 22, 68]. If the two lists are not of equal lengths, the code should return a message that "the lists are not of equal lengths".

def add_reverse(n: list, k:list):
    new_list = []

    if len(n) == len(k):
        for i in range(0, len(n)):
            new_list.append(n[i] + k[i])
            new_list.reverse()
        return new_list
    else: 
        return f"Lists have different lengths"
    
list1 = [10, 12, 34]
list2 = [12, 56, 78]

print(add_reverse(list1, list2))