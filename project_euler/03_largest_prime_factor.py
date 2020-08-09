"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def largest_prime_factor(n):
    factors = []
    for i in range(n, 0, -1):
        if n % i == 0 and is_prime(i):
            return i
            
        # print(i)

    return None


print(largest_prime_factor(13195))
