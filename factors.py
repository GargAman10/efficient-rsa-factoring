import sys
from random import randint

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def pollards_rho(n, max_iterations=1000):
    if n % 2 == 0:
        return 2
    for _ in range(max_iterations):
        x = randint(1, n-1)
        y = x
        c = randint(1, n-1)
        g = 1
        while g == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            g = gcd(abs(x - y), n)
        if g != n:
            return g
    return n
