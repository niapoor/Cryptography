#!/usr/bin/env python3

import sys
import random

global N    # N must be prime
global p    # p and q must be coprime
global q    # q must be larger than p
global f    # the first polynomial
global g    # the second polynomial

N = 13      # Setting default values for variables
p = 6
q = 7
f = []
g = []


# A function that gets the greatest common denominator of two functions
def gcd(a, b):
    # If the mod of the previous run of the function (or the input) was 0, return the gcd a
    if ( b == 0 ):
        return a
    # Otherwise, take the modulo of the current values and run the function again recursively
    else:
        return gcd( b, a % b )

# A function that returns whether or not a number is prime
def is_prime(a):
    for i in range(2, a):
        if( a % i == 0 ):
            return False
    return True


def compute_random_polynomial(polynomial):
    degree = (random.randint(1, N - 1))
    while degree != 0:
        polynomial.append(random.randint(-1, 1))
        degree = degree - 1
    if((-1 not in polynomial) and (1 not in polynomial)):
        compute_random_polynomial(polynomial)
    return polynomial

compute_random_polynomial(f)
compute_random_polynomial(g)

