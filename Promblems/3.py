
"""
Problem 3.

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

def brute_force_solution(num):
    # count down to find the first number and break
    for i in range(num, 1, -1):
        if num % i == 0 and is_prime(i):
            return i

    return "No prime factor found"


def is_prime(num):
    """
        returns a boolean if the given number is a prime number
    """
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

print(brute_force_solution(600851475142))