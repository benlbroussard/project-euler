text = """Longest Collatz sequence
Problem 14

The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

print(text)

import time

# collatz recursion
def collatz(num, terms):
  terms.append(num)
  if num == 1:
    return
  elif num%2 == 0:
    collatz(num/2, terms)
    return
  else:
    collatz(3*num + 1, terms)
    return

#terms = []
#collatz(13, terms)
#print(terms)

start_time = time.clock()

longest = 0
for i in range(2, 1000000):
  terms = []
  collatz(i, terms)
  if len(terms) > longest:
    longest = len(terms)
    terms_of_longest = terms

end_time = time.clock()
runtime = end_time - start_time

print('=======')
print('ANSWER:')
print('=======')
print('terms of longest: ' + str(terms_of_longest))
print('longest: ' + str(terms_of_longest[0]) + ' with ' + str(longest) + ' terms')
print('found in ' + str(runtime) + ' seconds')

