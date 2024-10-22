import math

def rsa_factoring(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, math.isqrt(num) + 1):
            if num % i == 0:
                return False
        return True

    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            factor = n // i
            if is_prime(i) and is_prime(factor):
                return (i, factor)
    return None
