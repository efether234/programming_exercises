"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_of_multiples(n, num_1, num_2):
    """
    Create list of all whole numbers starting at 0, up to but not including
    n that are also factors of num_1 or num_2. Return sum of that list.
    """
    return sum([i for i in range(n) if i % num_1 == 0 or i % num_2 == 0])


print(sum_of_multiples(1000, 3, 5))
