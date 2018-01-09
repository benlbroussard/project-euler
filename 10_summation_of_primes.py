text = """Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

print(text)

import time

# generate list of all odd numbers starting at 3 up to and including bound
def generate_odds(bound):
  odds = [(x*2 + 1) for x in range(1,bound//2)]
  if bound % 2 == 1:
    odds.append(bound)
  return odds

#print(generate_odds(11))

start_time = time.clock()

bound = 2000000
bound_root = int(bound**(1/2.0))
primes = generate_odds(bound)

# x*2+3: 0->3, 1->5, 2->7, 3->9, ...
# (x-3)/2: 3->0, 5->1, 7->2, ...
for i in range(0,len(primes)):
  if primes[i] > bound_root: # only go up to root of bound (which could be prime)
    break                    # any composite above that has a prime divisor less than it's root
  if primes[i] != 0:
    prime = primes[i]
    ctr = 3*prime
    while ctr <= bound:
      j = (ctr-3)/2
      primes[j] = 0
      ctr += 2*prime

primes.insert(0,2)

total = sum(primes)

end_time = time.clock()
runtime = end_time - start_time

print('=======')
print('ANSWER:')
print('=======')
print('sum of primes under ' + str(bound) + ': ' + str(total) + ' found in ' + str(runtime) + ' seconds')
