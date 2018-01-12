text = """The decimal number, 585 = 10010010012 (binary), is palindromic 
in both bases. Find the sum of all numbers, less than one million, which 
are palindromic in base 10 and base 2. (Please note that the palindromic 
number, in either base, may not include leading zeros.)
"""

print(text)

import time, math

def bruteforce(ubound):
  pals = []
  for i in range(1,ubound + 1):
    if str(i) == str(i)[::-1] and bin(i)[2:] == bin(i)[2:][::-1]:
      #print('i: ' + str(i))
      pals.append(i)
  return pals

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

def get_base2_pals(ubound):
  ubound_digits = len(bin(ubound)[2:])
  
  pals = [1,3] # hardcoded 1 & 2 digit cases
  for digits in range(3,ubound_digits + 1):
    half_digits = int(math.ceil(digits/2.0) - 1)
    for j in range(0,2**half_digits): # 0-1, 0-3, 0-7, 0-15, etc
      bit_str = '1' + (half_digits - len(bin(j)[2:])) * '0' + bin(j)[2:]
      bit_str += bit_str[:int(math.floor(digits/2.0))][::-1]
      if int(bit_str,base=2) > ubound:
        return pals
      pals.append(int(bit_str,base=2))
      #print('bit_str: ' + bit_str + ', ubound: ' + str(ubound) + ', digits: ' + str(digits) + ', j: ' + str(j))
  return pals

def get_double_base_pals(ubound):
  ubound_digits = len(bin(ubound)[2:])
  
  pals = [1,3]
  for digits in range(3,ubound_digits + 1):
    half_digits = int(math.ceil(digits/2.0) - 1)
    for j in range(0,2**half_digits): # 0-1, 0-3, 0-7, 0-15, etc
      bit_str = '1' + (half_digits - len(bin(j)[2:])) * '0' + bin(j)[2:]
      bit_str += bit_str[:int(math.floor(digits/2.0))][::-1]
      if str(int(bit_str,base=2)) != str(int(bit_str,base=2))[::-1]:
        continue
      if int(bit_str,base=2) > ubound:
        return pals
      pals.append(int(bit_str,base=2))
      #print('bit_str: ' + bit_str + ', ubound: ' + str(ubound) + ', digits: ' + str(digits) + ', j: ' + str(j))
  return pals


ubound = 1000000

start_time = time.clock()
base10_pals = get_base10_pals(ubound)
end_time = time.clock()
runtime1 = end_time - start_time

start_time = time.clock()
base2_pals = get_base2_pals(ubound)
end_time = time.clock()
runtime2 = end_time - start_time

start_time = time.clock()
#double_base_pals = [pal for pal in base10_pals if pal in base2_pals]
double_base_pals = get_double_base_pals(ubound)
end_time = time.clock()
runtime3 = end_time - start_time

start_time = time.clock()
brute_pals = bruteforce(1000000)
end_time = time.clock()
runtime4 = end_time - start_time

print('double base palindromes less than 1,000,000: ' + str(double_base_pals))
print('base10 length:    ' + str(len(base10_pals)) + ', time: ' + str(runtime1))
print('base2 length:     ' + str(len(base2_pals)) + ', time: ' + str(runtime2))
print('double_base_length: ' + str(len(double_base_pals)) + ', time: ' + str(runtime3) + ', sum: ' + str(sum(double_base_pals)))
print('bruteforce_length:  ' + str(len(brute_pals)) + ', time: ' + str(runtime4))

print('==============')
print('ANSWER: 872187')
print('==============')

