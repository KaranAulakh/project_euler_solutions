
"""
Problem 3.

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

def brute_force_solution(num):
    """
    This solution works, but is quite slow, you have to iterate down from every number and for each possible factor you have to 
    again determine if the factor is prime or not, giving us O(n)^2 time complexity, making this solution longer than minutes for even
    a value as small as 600851475143
    """
    for i in range(num, 1, -1):
        if num % i == 0 and is_prime(i):
            return i

    return "No prime factor found"

def brute_force_optimized(num):
    """
    Counting down is not needed as we know that a factor cannot exist in the top half of the number, at best if the number is divisible by 2
    the largest factor is half of the number. Thus, we can instead divide the number by values, counting up. The result of the first division
    will give us the highest possible factor
    """
    largest_prime_factor = None

    for i in range(2, num):
        if num % i == 0:
            possible_prime = num // i
            if is_prime(possible_prime):
                return possible_prime
            elif is_prime(i):
                largest_prime_factor = i

    # if no factor was found using the bigger of the two return the smaller one instead
    if largest_prime_factor != None:
        return largest_prime_factor
    
    return "No prime factor found"

def is_prime(num):
    """
        returns a boolean if the given number is a prime number
    """
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

print(brute_force_optimized(600851475143))