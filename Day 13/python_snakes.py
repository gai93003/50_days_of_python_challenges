######### Extra Challenge: Pyramid of Snakes ############

# Write a function called "Python_snakes" that takes a number as an argument and creates the following shape, using the number's range: (hint: Use the loops and emoji library. If you pass 7 as argument, your code should print the following)

from emoji import emojize

def Python_snakes(n: int):
    # the loop to determine the number of rows of the pyramid

    for i in range(0, n):
        # The loop that determines number of columns
        
        for j in range(n, i, -1):
            # Print space between the snake signs
            print(end=" ")
        
        for k in range(0, i):
            # Printing the snake emoki
            print(emojize(':snake:'), end=" ")
        print("\n")

Python_snakes(7)