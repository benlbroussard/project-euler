text = """Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
print(text)

# this is another manual one
#
# the square of the sum (1+2+...+n)**2 = (n*(n+1)/2)**2
#
# the sum of the squares 1**2 + 2**2 + ... + n**2 = n(n*(n+1)/2) - (n-1)n(n+1)/6
#
# for the 10 case this means: 
# (10*11/2)**2 = 55**2 = 3025
# and
# 10(10*11/2) - 9*10*11/6 = 550 - 165 = 385
# so
# 3025 - 385 = 2640
#
# for the 100 case:
# (100*101/2)**2 = 5050**2 = 25502500
# and
# 100(100*101/2) - 99*100*101/6 = 505000 - 166650 = 338350
# so

print('=======')
print('ANSWER:')
print('=======')

print('(1+2+3+...+100)^2 - (1^2+2^2+...+100^2)')
print('      25502500    -      338350    = 25164150')