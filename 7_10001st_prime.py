text = """10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

print(text)

import time

# generate all primes up through 10001st: 
#  - handle 2 case, then only check odd numbers
#  - test each odd number for divisibility by the found primes up to its root
#  - if it isn't divisible, add to prime list and update prime count by 1
def build_primes(bound):
  primes = [2,3]
  
  #steps = 0
  ctr = 3
  while len(primes) < bound:
    #print('ctr: ' + str(ctr))
    ctr += 2
    ctr_root = int(ctr**(1/2.0))
    prime = True
    #print('ctr: ' + str(ctr) + ' ctr_root: ' + str(ctr_root) + ' primes: ' + str(primes))
    
    for i in xrange(1,len(primes)):
      #steps += 1
      if primes[i] > ctr_root: # only check primes up to root of ctr
        #print('last prime checked: ' + str(primes[i]))
        break
      
      if ctr % primes[i] == 0:
        prime = False
        #print(str(ctr) + ' is divisible by ' + str(primes[i]))
        break
      
    if prime:
      primes.append(ctr)
    
    if (ctr + 2) % 3 == 0:
      ctr += 2
  
  #print('steps: ' + str(steps))
  return {str(bound):primes[-1],"primes":primes}



print('=======')
print('ANSWER:')
print('=======')
bound = 10001
start_time = time.clock()
result = build_primes(bound)
end_time = time.clock()

print(str(bound) + 'th prime: ' + str(result[str(bound)]) + ' found in ' + str(end_time - start_time) + ' seconds')