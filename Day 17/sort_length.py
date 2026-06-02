################# Extra Challenge: Sort by Length #################

# Write a function called "sort_length" that takes a list of strings as an argument, and sorts the strings in ascending order according to their length. For example, the list above should return:

names = ["Peter", "Jon", "Andrew"]

# ["Jon", "Peter", "Andrew"]

# Do not use the built-in sort functions

def sort_length(arr: list):
    
    for item in range(len(arr)):
        for j in range(len(arr) - 1):
            # Check if any of the words is longer than the other

            if len(arr[j]) > len(arr[j + 1]):
                # Swap the longest for the shortest

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

if __name__ == "__main__":
    print(sort_length(names))