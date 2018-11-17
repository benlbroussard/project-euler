text = """Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

print(text)

import time
import math

# helper: build a palindromic number given first 3 digits
def build_pal(front):
  str_front = str(front)
  str_back = str_front[2] + str_front[1] + str_front[0]
  return int(str_front + str_back)


# check each palindromic number, not all ways to combine 2 3-digit factors
def answer():
  #steps = 0
  for i in range(1,901):
    pal = build_pal(1000 - i)
    
    # determine the lowest number to check as a factor (ceiling of the root)
    lowest_factor = int(math.ceil(pal**(1/2.0)))
    #print('i: ' + str(i) + ' pal: ' + str(pal) + ' lowest_factor: ' + str(lowest_factor))
    
    for j in range(lowest_factor, 1000):
      #steps += 1
      #print('j: ' + str(j))
      if pal % j == 0:
        #print(str(j) + ' x ' + str(pal/j) + ' = ' + str(pal))
        #print('steps: ' + str(steps))
        return {"factors": (j,pal/j),"pal":pal}
    



start_time = time.clock()
result = answer()
end_time = time.clock()


print('=======')
print('ANSWER:')
print('=======')
print(str(result["factors"][0]) + ' x ' + str(result["factors"][1]) + ' = ' + str(result["pal"]) + ' in ' + str(end_time - start_time) + ' seconds')

