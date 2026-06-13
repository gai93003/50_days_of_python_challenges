########### Extra Challenge: Multiply Words ############

s = "love live and laugh"

# Write a function called "multiply_words" that takes a string as an argument and multiples the length of each word in the string by the length of other words in the string.
# For example, the string should return 240 - love (4) live (4) and (3) laugh (5). However, your function should only multiply words will all lowercase letters.
# If a word has one upper case letter, it should be ignored. For example, the following string: s = "Hate war love Peace" should return 12 - war(3) love (4).
# Hate and Peace will be ignored because they have at least one uppercase letter.

import math
def multiply_words(s: str):
    arr = []
    m = 0
    for word in s.split():
        if word.islower():
            arr.append(len(word))
            m = math.prod(arr)
    return 'The prod of the word lengths is', m


str2 = "love live and laugh"
str3 = "Hate war love Peace"
print(multiply_words(str2))
print(multiply_words(str3))