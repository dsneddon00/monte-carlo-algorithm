import math
import random

def main():




def monteCarlo(num):
    # Implement (in Python) a function that takes an integer as input and returns True or False as output,
    #indicating whether or not the integer is prime. Use the Monte Carlo probabalistic algorithm discussed
    #in section 7.2, so that it will finish in reasonable time given several hundred digit test numbers.
    #We will use this piece of code later when we implement RSA encription.

    # Hint: Replace the Python command:
    # remainder = b ** e % n
    # with the equivalent but far faster:
    # remainder = pow(b,e,n)


def generateNumberRandom(min, max):
    return random.randrange(min, max)


if __name__ == "__main__":
    main()

# Notes from class - 10/1/2021
# IsPrimeMiller(n):
#   reps = 10
#   for i in range(reps):
#       ok = millerstest(n)
#       if not ok:
#            return False # for sure not prime
#   return True # n is probably prime

# Notes from class - 10/4/2021
# refer to pg 286 of the book
# def IsPrimeMiller(n):


# Notes from class - 10/8/2021
# n = 101
# n-1 = 100 = 2^(5)(T) = 2^(2)(25)
# s = 2
# T = 25

# b must be a random number between 2 nad 100
# for now, b = 2
# b^(T) % n is 1    2^(25) % 101 is 1 ? no (10)
# j = 0 b^(2*T) % n is (n-1)    2^(25) % 101 is 100? no
# j = 1     2^50 % 101 is 100? yes
