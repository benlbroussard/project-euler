text = """Power digit sum
Problem 16

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

"""

print(text)

import time

mynum = 2**1000
mystr = str(mynum)
mysum = 0
for num in mystr:
  mysum += int(num)

print('=======')
print('ANSWER:')
print('=======')
print('sum of digits of 2^1000: ' + str(mysum))






