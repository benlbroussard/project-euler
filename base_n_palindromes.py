import math
from base_n import base_n, to_int

"""
Base n palindromes are funky, because it's hard to imagine something like base 1 million.
Think of it as each digit being a number in a list (base_n class literally treats them this way).

I have a technique that builds palindromes for any base by counting up and then
prepending each prefix and flipping it to have palindromes. It catches them all
and it's pretty fast. There is a base case to handle because there's no middle to
count through until you get to >= 3 digits.
"""


def get_base_n_palindromes(ubound, base):
  n_ubound = base_n(ubound,base)
  n_ubound_digits = len(n_ubound.string)
  
  # bruteforce the first two digits
  pals = []
  for i in range(0,2): # 1&2 digit base cases
    for j in range(base**i,base**(i+1)): # not counting zero
      n_j = base_n(j,base)
      if n_j.string ==  n_j.string[::-1] and j <= ubound:
        #print('j: ' + str(j) + ', n_j: ' + str(n_j.string))
        pals.append(j)
  pals.sort()
  #print('1&2 digit pals: ' + str(pals))
  
  for digits in range(3,n_ubound_digits + 1):
    half_digits = int(math.ceil(digits/2.0) - 1)
    for j in range(0,base**half_digits): # 0-9, 0-99, 0-999, etc. for base 10
      for prefix in range(1,base):
        # add prefix, add zero padding, add j-counter in base, add flipped beginning
        pal_str = []
        pal_str += base_n(prefix,base).string
        pal_str += (half_digits - len(base_n(j,base).string)) * base_n(0,base).string 
        pal_str += base_n(j,base).string
        pal_str += pal_str[:int(math.floor(digits/2.0))][::-1]
        if to_int(pal_str,base) > ubound:
          continue
        pals.append(to_int(pal_str, base))
        #print('pal_str: ' + str(pal_str) + ', ubound: ' + str(ubound) + ', digits: ' + str(digits) + ', half_digits: ' + str(half_digits) + ', j: ' + str(j) + ', prefix: ' + str(prefix))
  pals.sort()
  pals = [pal for pal in pals if pal < ubound]
  return pals

lengths = []
for base in range(2,37):
  #base = 5
  ubound = 1000000
  pals = get_base_n_palindromes(ubound, base)
  print('base: ' + str(base) + ', num pals: ' + str(len(pals)))
  lengths.append(len(pals))

#print('lengths: ' + str(lengths))




# easier to understand in base 10, include for reference
def get_base10_pals(ubound):
  ubound_digits = len(str(ubound))
  
  pals = range(1,10) + range(11,100,11) # [1,3,...,9,11,33,...,99] hardcoded 1 & 2 digit cases
  for digits in range(3,ubound_digits + 1):
    half_digits = int(math.ceil(digits/2.0) - 1)
    for j in range(0,10**half_digits): # 0-9, 0-99, 0-999, etc.
      for n in range(1,10): # could speed up by stepping by 2 here and for base case
        pal_str = str(n) + (half_digits - len(str(j))) * '0' + str(j)
        pal_str += pal_str[:int(math.floor(digits/2.0))][::-1]
        if int(pal_str) > ubound:
          return pals
        pals.append(int(pal_str))
        #print('pal_str: ' + pal_str + ', ubound: ' + str(ubound) + ', digits: ' + str(digits) + ', j: ' + str(j) + ', n: ' + str(n))
  return pals