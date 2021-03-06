text = """Even Fibonacci numbers
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

print(text)

import time

# add as you build
def build_up(bound):
  fib_prev = 0
  fib_curr = 1
  
  total = 0
  
  while fib_curr <= bound:
    hold = fib_curr
    fib_curr += fib_prev
    fib_prev = hold
    
    if fib_prev % 2 == 0:
      total += fib_prev
  
  return total


my_bound = 4000000
start_time = time.clock()
answer = build_up(my_bound)
end_time = time.clock()

print('=======')
print('ANSWER:')
print('=======')
print('')
print('sum of even fibonacci numbers below ' + str(my_bound) + ':')
print(str(answer))
print('')
print('runtime: ' + str(end_time - start_time) + ' seconds')