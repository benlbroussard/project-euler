text = """Factorial digit sum
Problem 20

n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!


"""

print(text)

import time

factorial_list = list(range(2,101))
mynum = 1
for num in factorial_list:
  mynum *= num
mystr = str(mynum)
mysum = 0
for num in mystr:
  mysum += int(num)

print('=======')
print('ANSWER:')
print('=======')
print('sum of digits of 100!: ' + str(mysum))