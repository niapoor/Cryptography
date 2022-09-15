#!/usr/bin/env python3

from asyncio.windows_events import NULL
import sys

global N    # N must be prime
global p    # p and q must be coprime
global q    # q must be larger than p

N = 13      # Setting default values for variables
p = 6
q = 7

def assign_value(index, currentVar):
    try:
        sys.argv[index]
    except:
        print("No value assigned to " + currentVar)
        return NULL
    else:
        if (sys.argv[index].isnumeric()):
            return int(sys.argv[index])
        else:
            print("Invalid value assigned to " + currentVar)
            return NULL

def take_in_parameters():
    for i in range(1, len(sys.argv)):
        if (sys.argv[i].startswith("-")):
            if (sys.argv[i].lower() == "--options" or sys.argv[i].lower() == "-o"):
                print("==== Options ====")
            elif (sys.argv[i].lower() == "-n"):
                global N
                if (assign_value(i+1, "N") != NULL):
                    N = assign_value(i+1, "N")
                    print("'N' has been assigned the value " + sys.argv[i+1])
            else:
                print("A non valid option was input")

# Confirms if the input values meet the requirements for the NTRU Encryption
def confirm_requirements():
    if ( p >= q ):                          # Make sure p is smaller than q
        print("p is not smaller than q")
        return False
    elif ( gcd(p, q) != 1 ):                # Make sure p and q are coprime
        print("p and q are not coprime")
        return False
    elif ( is_prime(N) == False ):          # Make sure N is prime
        print("N is not prime")
        return False
    else:                                   # If these requirements are met, the encryption can continue
        return True

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

def run_encryption():
    if ( confirm_requirements() == False ):
        print("One or more requirements for input values were not met. Encryption will not run.")
        return
    print("Reached")

take_in_parameters()
run_encryption()