text = """Lattice paths
Problem 15

Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""

print(text)

import time

# create the permutations leaving out the unallowed ones
def permutations(right_and_down,elements_left,used_list,perms):
  #print('elements_left: ' + str(elements_left) + ' used_list: ' + str(used_list) + ' perms: ' + str(perms))
  
  for element in elements_left:
    # if elements before element in right or down are not in used_list, continue
    if element in right_and_down[0]: # determine if element in right or down
      right_and_down_ix = 0
    else:
      right_and_down_ix = 1
    location = right_and_down[right_and_down_ix].index(element) # find index of element in right or down
    skip = False
    for prior in right_and_down[right_and_down_ix][0:location]: # look at prior elements in right or down
      if prior not in used_list: # if prior elements not already used, there will be an illegal reversal
        #print('prior: ' + str(prior) + ' used_list: ' + str(used_list) + ' skip element: ' + str(element))
        skip = True
        break
    if skip:
      continue
    
    new_used_list = list(used_list)
    new_used_list.append(element)
    #print('new_used_list: ' + str(new_used_list))
    new_elements_left = list(elements_left)
    new_elements_left.remove(element)
    #print('new_elements_left: ' + str(new_elements_left))
    if len(new_elements_left) == 0:
      new_perm = list(new_used_list)
      perms.append(new_perm)
      #print('new_perm: ' + str(new_perm))
      continue
    permutations(right_and_down,new_elements_left, new_used_list,perms)
  
  return

def factorial(n):
  factors = list(range(2,n+1))
  prod = 1
  for factor in factors:
    prod *= factor
  return prod

'''
start_time = time.clock()

for i in range(2,10):
  start_time = time.clock()
  n = i
  elements = [str(x) for x in range(2*n)]
  right = list(elements[0:len(elements)/2])
  down = list(elements[(len(elements)/2):])
  right_and_down = [right,down]
  perms = []
  permutations(right_and_down,elements, [], perms)
  answer = len(perms)
  end_time = time.clock()
  print('n: ' + str(n) + ' answer: ' + str(answer) + ' time: ' + str(end_time-start_time))

#for perm in perms:
#  s=""
#  for letter in perm:
#    s+=letter
#  print(s)
'''

start_time = time.clock()

n=20
# do 40 choose 20 or 40!/(20!*20!)
answer = factorial(2*n)/(factorial(n)**2)

end_time = time.clock()
runtime = end_time - start_time

print('=======')
print('ANSWER:')
print('=======')
print('found in ' + str(runtime) + ' seconds')
print('number of paths: ' + str(answer))


