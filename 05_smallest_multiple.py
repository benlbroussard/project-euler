text = """Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

print(text)

# This one is easy. For the 10 case, we just have to have enough primes to cover 1 through 10.
# If we have a number in 1-10 that isn't covered by our prime list, then it won't divide the 
# bignum we're looking for and if we have too many primes, then it won't be the smallest number.
# For the 10 case we have the following prime factorizations:
# 2=2, 3=3, 4=2*2, 5=5, 6=2*3, 7=7, 8=2*2*2, 9=3*3, and 10=5*2
# Note that 4 just requires one extra 2, and we already have a 2 and a 3 by the time we get to 6,
# so we need 2*3*2*5*7*2*3 = 2520
# 
# For the 20 case, we additionally have to cover the following:
# 11=11, 12=2*2*3, 13=13, 14=2*7, 15=3*5, 16=2*2*2*2, 17=17, 18=2*3*3, 19=19, 20=2*2*5
# so we need 2*3*2*5*7*2*3 * 11*13*2*17*19 = 2520 * 92378 = 232792560


print('=======')
print('ANSWER:')
print('=======')
print('2*3*2*5*7*2*3 * 11*13*2*17*19 = 2520 * 92378 = 232792560')