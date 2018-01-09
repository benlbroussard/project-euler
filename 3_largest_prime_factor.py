text = """Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

print(text)

import time

# go up to square root and remove by division from big number
def test_and_remove(my_num, ctr, primes):
  my_root = my_num ** (1/2.0)
  #print('test_and_remove(' + str(my_num) + ', ' + str(ctr) + ', ' + str(primes) + ')')
  
  while ctr <= int(my_root):
    #print('my_num: ' + str(my_num) + ', ctr: ' + str(ctr) + ', primes: ' + str(primes))
    if my_num % ctr == 0:
      primes.append(ctr)
      test_and_remove(my_num / ctr, ctr, primes)
      return
    
    ctr += 2
  
  # final call
  #print('final call')
  primes.append(my_num)
  return 


mynum = 600851475143
start_time = time.clock()
primes = []
test_and_remove(mynum, 3, primes)
end_time = time.clock()


print('=======')
print('ANSWER:')
print('=======')
print('primes in ' + str(mynum) + ': ' + str(primes) + ' in ' + str(end_time - start_time) + ' seconds')