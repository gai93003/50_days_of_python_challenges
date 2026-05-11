############# Extra Challenges: List of Prime Numbers ###############

# Write a function called "prime_numbers". This function asks a user to enter a number (integer) as an argument and returns a list of all the prime numbers within its range. For example, if user enters 10, your code should return [2, 3, 5, 7] as prime numbers.

def prime_numbers() -> list:
    prime_num = []
    n = int(input("Please enter a number (integer): "))

    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_num.append(i)

    return prime_num

print(prime_numbers())