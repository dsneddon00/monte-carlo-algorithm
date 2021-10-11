



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
