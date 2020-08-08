"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def multiple(cand, fact):
    """Check if cand (candidate) is a multiple of fact (factor)"""
    return cand % fact == 0


def sum_of_multiples(n, num_1, num_2):
    """
    Iterate through all numbers up to but not including n. If number
    is multiple of num_1 OR num_2, append it to mults. Return sum of
    mults.
    """
    mults = []
    for i in range(0, n):
        if multiple(i, num_1) or multiple(i, num_2):
            mults.append(i)

    return sum(mults)


print(sum_of_multiples(1000, 3, 5))
