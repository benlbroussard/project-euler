text = """Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

print(text)

import time

# brute force method
def brute_force(bound):
  total = 0
  
  for i in range(0,bound):
    if i%3 == 0 or i%5 == 0:
      total += i
  
  return total


my_bound = 1000
start_time = time.clock()
bf_answer = brute_force(my_bound)
end_time = time.clock()

print('=======')
print('ANSWER:')
print('=======')
print('')
print('sum of multiples of 3 and 5 below ' + str(my_bound) + ':')
print(str(bf_answer))
print('')
print('runtime: ' + str(end_time - start_time) + ' seconds')


# look at the pretty pattern
#for i in range(1,8):
#  bf_answer = brute_force(10**i)
#  print(str(10**i) + ': ' + str(bf_answer))

# 10: 23
# 100: 2318
# 1000: 233168
# 10000: 23331668
# 100000: 2333316668
# 1000000: 233333166668
# 10000000: 23333331666668
# 100000000: 2333333316666668
#
# 10**3 has 2 3's and 1 6
# 10**4 has 3 3's and 2 6's
# 10**5 has 4 3's and 3 6's
# 10**6 has 5 3's and 4 6's
# 10**7 has 6 3's and 5 6's
# 10**8 has 7 3's and 6 6's
#
# 10**n is a 2 then n-1 3's then a 1 then n-2 6's then an 8
