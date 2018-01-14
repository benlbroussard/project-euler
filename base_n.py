import math

class base_n:
  
  def __init__(self, number, base):
    self.integer = number
    self.base = base
    self.chars_per_digit = len(str(base-1)) # 10 needs 1 digit, 0-9
    if self.integer < base:
      self.num_digits = 1 # can't take log of zero, only 1 digit for nums smaller than base
    else:
      self.num_digits = int(math.floor(math.log(self.integer,self.base)) + 1)  # b**0 case needed
    
    # build base_n string: (base 1000, 4 digit string) 003_534_110_099 == 3,534,110,099
    # but reversed would be 099_110_534_003 == 99,110,534,003
    self.string = []
    hold_int = self.integer
    for exp in range(0,self.num_digits)[::-1]: # in base 2, 4 == 100, so we want 2^2, 2^1, 2^0, or 2,1,0
      hold_str = str(int(math.floor(1.0*hold_int / base**exp)))
      hold_str = '0' * (self.chars_per_digit - len(hold_str)) + hold_str
      self.string.append(hold_str)
      if hold_int >= base**exp:
        hold_int = hold_int % base**exp
      #print('exp: ' + str(exp) + ', base: ' + str(base) + ', base**exp: ' + str(base**exp) + ', hold_str: ' + hold_str + ', hold_int: ' + str(hold_int))
  
def to_int(digits, base):
  int_form = 0
  for i in range(0,len(digits)):
    int_form += base**i * int(digits[i])
  return int_form

