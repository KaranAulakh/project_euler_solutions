"""
Problem 1:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def problem1():
    """
    Brute Force Solution
    we can solve this procedurally by simple brute force. We need to iterate through all numbers
    below 1000 and check if they are multiples of 3 or 5. If they are, we add them to a sum.

    sum = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


    Effiecient Mathematic Solution

    We can solve this much quicker by using the method below to determine the sum of any k and m where k
    is the multiple and m is the number of times that multiple exists in our range. For example, with all 
    multiples of 3 below 10: k is 3 and m is also 3, since only 3 multiples exist in that range (3, 6, 9).

    Using this method we can find all multiples of 3, add all multiples of 5, and subtract all multiples of
    15 as those are counted twice. 
    """

    return sum_k_of_m(3, 999 // 3) + sum_k_of_m(5, 999 // 5) - sum_k_of_m(15, 999 // 15)


def sum_k_of_m(k, m):
    """
    Uses Gauss's formula to sum the first m multiples of k -> k * ((m * (m + 1)) / 2)
    Intution: For example, for multiples of 3 under 10, k = 3 and m = 3. We can think of this as such

    3 + 6 + 9 = 18 can also be seen as 3 * (1 + 2 + 3)
    Here the 3 on the lefthand is our k value the lefthand is represented with ((m * (m + 1)) / 2)
    Gauss's formula gives us the sum of uniformingly increasing values using triangular number formula.
    1 + 2 + 3 = 6 = (3 * 4) / 2
    """
    return k * ((m * (m + 1)) / 2)



print(problem1())