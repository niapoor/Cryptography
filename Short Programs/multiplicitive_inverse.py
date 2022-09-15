#!/usr/bin/env python3

m = 13
a = 5

def gcd(a, b):
    if ( b == 0 ):
        return a
    else:
        return gcd( b, a % b )

def multiplicitive_inverse(m, a, i):
    if ( (a * i) % m != 1 ):
        multiplicitive_inverse(m, a, i + 1)
    elif ( gcd(a, m) != 1 ):
        print("Does not have a multiplicitive inverse")
    else:
        print("The multiplicitive inverse of " + str(a) + " in Z" + str(m) + " is " + str(i))

multiplicitive_inverse(m, a, 0)