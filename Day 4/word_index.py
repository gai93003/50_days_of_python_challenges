############# Extra Challenge: Index of the Longest Word ###################

# Write a function called word_index that takes one argument, a list of strings and return the index of the longest word in the list. If there is not longest word (if all the strings are of the same length), the function should return zero(0). For example, the list below should return 2.

words1 = ["Hate", "remorse", "vengence"]

# And this list below, should return zero (0)

words2 = ["Love", "Hate"]


def word_index(lst):
    longest = max(lst, key=len)
    shortest = min(lst, key=len)

    if longest == shortest:
        return 0
    else:
        return lst.index(longest)

print(word_index(words1))
print(word_index(words2))