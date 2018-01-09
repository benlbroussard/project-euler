text = """Amicable numbers
Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

print(text)

import time
import euler

# get the primes, combine into factors, sum the factors
def get_factors(n):
  if n < 1:
    return []
  
  factors = [1]
  root_n = n**(1/2.0)
  
  if n%2 == 0: # odd numbers cannot have even factors
    start = 2
    step = 1
  else:
    start = 3
    step = 2
  
  for i in range(start,n+1,step):
    #print('i: ' + str(i) + ' root_n: ' + str(root_n) + ' n: ' + str(n) + ' factors: ' + str(factors))
    if i >= root_n: # already have all factors larger than root_n, but n might be a square
      if i == root_n: # if so, add the integer root
        factors.append(i)
      break
    
    if n%i == 0:
      factors.append(i)
      factors.append(n/i)
    
  factors.sort()
  #print('factors: ' + str(factors))
  return factors

#print(get_factors(6))

start_time = time.clock()

bound = 10000

factor_sums = []
for i in range(0,bound):
  i_factors = get_factors(i)
  i_sum = sum(i_factors)
  factor_sums.append((i,i_sum))
  #print('i: ' + str(i) + ' factors: ' + str(i_factors) +' sum: ' + str(i_sum))
#print('factor_sums: ' + str(factor_sums))

amicable_numbers = []
for i in range(len(factor_sums)):
  a1 = factor_sums[i][0]
  b1 = factor_sums[i][1]
  if a1 == b1:
    continue # a != b is a requirement of amicable numbers stated in the text
  if b1 < bound:
    a2 = factor_sums[b1][1]
  else:
    continue # skip if the sum of the factors of j is >= bound, we're looking for under bound (and we'll get an index error)
  #print('i: ' + str(i) + ' a1: ' + str(a1) + ' b1: ' + str(b1) + ' b2: ' + str(factor_sums[b1][0]) + ' a2: ' + str(a2))
  if a1 == a2 and (b1,a1) not in amicable_numbers: # check if switched amicable numbers already in list, then it's a duplicate
    amicable_numbers.append((a1,b1))

#print('amicalbe numbers: ' + str(amicable_numbers))


answer = 0
for i in range(len(amicable_numbers)):
  answer += amicable_numbers[i][0]
  answer += amicable_numbers[i][1]

end_time = time.clock()
runtime = end_time - start_time

print('=======')
print('ANSWER:')
print('=======')
print('found in ' + str(runtime) + ' seconds')
print('final answer: ' + str(answer))
