text = """Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

print(text)

import time

# find first n squares
def squares(n):
  return [x**2 for x in xrange(1,n+1)]

#print('squares(5): ' + str(squares(5)))

start_time = time.clock()

# generate all squares up to bound/2, iterate through them checking each against all squares above
# it to determine if the sum is a square, if so check a+b+c=bound and stop when it's true.
# see below for manual solution

bound = 1000 # always even
squarelist = squares(int(bound/2.0))

done = False
for i in range(0, len(squarelist)-1): # go up to the next-to-last one
  if done:
    break
  
  for j in range(i+1, len(squarelist)): # check the next one up to the last one
    a2 = squarelist[i]
    b2 = squarelist[j]
    c2 = a2 + b2
    if c2**(1/2.0) == int(c2**(1/2.0)): # is the sum of the squares a square?
      a = int(a2**(1/2.0))
      b = int(b2**(1/2.0))
      c = int(c2**(1/2.0))
      if a+b+c == bound: # is it our square (break at first instance)
        done = True
        break

end_time = time.clock()
runtime = end_time - start_time

print('=======')
print('ANSWER:')
print('=======')
print(str(a) + '+' + str(b) + '+' + str(c) + '=' + str(bound) + ' found in ' + str(runtime) + ' seconds')

# BY HAND:
# --------
# Every pythagorean triple (a,b,c) can be written as a=d(m^2-n^2), b=2dmn, c=d(m^2+n^2),
# where d is gcd(a,b,c), m>n, gcd(m,n)=1, and one of m or n is even, the other is odd
# a+b+c=d(m^2-n^2) + 2dmn + d(m^2+n^2) = 2dm(m+n) = bound, thus dm(m+n)=bound/2
# when bound == 1000, dm(m+n)=500. Note gcd(m,n) implies gcd(m,m+n)=1, also 500=2^2*5^3.
# If m was odd, m+n would be odd. But m>n, m<(m+n)<2m, so 5|m,(m+n) but gcd(m,m+n) = 1, so m is even.
# m = 2 or 4. m=2 implies 2<(m+n)<4, but 5|m+n, so m=4, m+n<8, so m+n = 5, so n=1 and d=500/(4*5)=25.
# a=25(4^2-1^2)=25*15=375, b=25*2*4*1=200, c=25(4^2+1^2)=25*17=425
# 375+200+425 = 1000 yay!