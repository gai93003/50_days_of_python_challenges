######### Extra Challenge: Reversed List ##########

str1 = 'leArning is hard, bUt if You appLy youRself ' \
'you can achieVe success'

# You are given a strings of words. Some of the words in the string contain uppercase letters. Write a code that will return all the words that have an uppercase letter. Your code should return a list of the words. Each word in the list should be reversed. Here is how you output should look:

# ['gninrAel', 'tUb', 'uoY', 'yLppa', 'flesRuoy', 'eVeihca']

def reversed_list(str1):
    new_arr = [word[::-1] for word in str1.split() if any(char.isupper() for char in word)]

    print(new_arr)


reversed_list(str1)