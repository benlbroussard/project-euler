# generate list of all odd numbers starting at 3 up to and including bound
def odds_list(bound):
  """
  Returns list of odds from 3 to bound (inclusive if bound is odd).
  """
  odds = [(x*2 + 1) for x in range(1,bound//2)]
  if bound % 2 == 1:
    odds.append(bound)
  return odds

#print(generate_odds(11))


def primes_list(bound):
  """
  Returns a list of all primes <= bound.
  """
  if bound < 2:
    raise ValueError('bound must be 2 or more')
  bound_root = int(bound**(1/2.0))
  odds = odds_list(bound)
  
  # x*2+3: 0->3, 1->5, 2->7, 3->9, ...
  # (x-3)/2: 3->0, 5->1, 7->2, ...
  for i in range(0,len(odds)):
    if odds[i] > bound_root: # only go up to root of bound (which could be prime)
      break                    # any composite above that has a prime divisor less than it's root
    if odds[i] != 0:
      prime = odds[i]
      ctr = 3*prime # 2*prime would be even, so skip it since we only have odd numbers in our odds list
      while ctr <= bound:
        j = (ctr-3)/2 # get odds index from number
        odds[j] = 0 # set multiples of the prime to zero
        ctr += 2*prime # our list only has odd ones, and adding one prime would make it even
    
  result = [x for x in odds if x != 0]  
  result.insert(0,2)
  return result

#print('result: ' + str(prime_list(1)))


def factorize(n, prime_list = []):
  """
  Returns prime factorization of n. 
  Faster if given a prime_list of appropriate size, otherwise generates one.
  
  TODO:
   - use prime list if given, verify that prime_list[-1] >= n**(1/2.0), I assume it's prime if I haven't found a prime divisor <= n**(1/2.0)
  """
  
  def test_and_remove(my_num, ctr, primes):
    # handle 1 case
    if my_num == 1:
      return
    # handle 2 case
    if my_num%2 == 0:
      if primes == []:
        primes.append(list([ctr]))
      else:
        primes[-1].append(ctr)
      if my_num / 2 == 1: # last run for a power of two
        return
      else:
        test_and_remove(my_num / 2, 2, primes)
        return
    if ctr == 2:
      ctr += 1
    
    # handle non-2 case
    my_root = my_num ** (1/2.0)
    #print('test_and_remove(' + str(my_num) + ', ' + str(ctr) + ', ' + str(primes) + ')')
    
    while ctr <= int(my_root):
      #print('my_num: ' + str(my_num) + ', ctr: ' + str(ctr) + ', primes: ' + str(primes))
      if my_num % ctr == 0:
        if primes == []:
          primes.append(list([ctr]))
        elif ctr in primes[-1]:
          primes[-1].append(ctr)
        else:
          primes.append(list([ctr]))
        test_and_remove(my_num / ctr, ctr, primes)
        return
      
      ctr += 2
    
    # final call
    #print('final call')
    if primes == []:
      primes.append(list([my_num]))
    elif my_num in primes[-1]:
      primes[-1].append(my_num)
    else:
      primes.append(list([my_num]))
    return
  
  # if prime_list is given
  def test_and_remove_known_primes(my_num, known_ix, primes, known_primes):
    # handle 1 case
    if my_num == 1:
      return
    
    my_root = my_num ** (1/2.0)
    my_prime = known_primes[known_ix]
    #print('test_and_remove(' + str(my_num) + ', ' + str(ctr) + ', ' + str(primes) + ')')
    
    while my_prime <= int(my_root):
      #print('my_num: ' + str(my_num) + ', ctr: ' + str(ctr) + ', primes: ' + str(primes))
      if my_num % my_prime == 0:
        if primes == []:
          primes.append(list([my_prime]))
        elif my_prime in primes[-1]:
          primes[-1].append(my_prime)
        else:
          primes.append(list([my_prime]))
        test_and_remove_known_primes(my_num / my_prime, known_ix, primes, known_primes)
        return
      
      known_ix += 1
      my_prime = known_primes[known_ix]
    
    # final call
    #print('final call')
    if primes == []:
      primes.append(list([my_num]))
    elif my_num in primes[-1]:
      primes[-1].append(my_num)
    else:
      primes.append(list([my_num]))
    return
  
  if prime_list == []:
    factorization = []
    test_and_remove(n, 2, factorization)
    return factorization
  else:
    #print('prime_list[-10:-1]: ' + str(prime_list[-10:-1]))
    prime_list.append(n) # if I use a prime list up to the prime before int(n**1/2), I can get an index out of bounds, so I throw n on the end, though I'll never check it 'cause I only check up to n**1/2
    factorization = []
    test_and_remove_known_primes(n,0,factorization,prime_list)
    return factorization


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
      factors.append(int(n/i))
    
  factors.sort()
  #print('factors: ' + str(factors))
  return factors

def permute(instr): # returns ordered permutations!
    #print(f'instr: {instr}')
    if len(instr) == 1: # base case
        return [instr]
    subperms = []
    for i in range(0,len(instr)):
        #print(f'letter: {instr[i]}, instr: {instr}')
        for subperm in permute(instr[:i] + instr[i+1:]):
            #print(f'letter: {instr[i]}, subperm: {subperm}, instr: {instr}')
            subperms.append(instr[i] + subperm)
    return subperms
