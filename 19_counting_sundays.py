text = """Counting Sundays
Problem 19

You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

print(text)

import time

start_time = time.clock()

# jan 1 day means there will be this many sundays on the first of a month that year
num_sun_reg = [2,2,2,1,3,1,1] # double and triple checked
num_sun_leap = [3,2,1,2,2,1,1]

# pattern repeats every 28 years from 1/1/1901. 100-28*3 = 100-84 = 16
# so we need the # of sundays on firsts of months for the first 16 year and first 28 years

day_ctr = 0 # monday of 1900, will be updated to tuesday of 1901 on first pass, but 1900 wasn't a leap year but the code thinks it was, so set to 0 (sun) instead of 1 (mon) to let code wrongly add 2
first_16 = 0
full_28 = 0
for i in range(1,29): # 1901-1928
  day_ctr += 1
  if i%4 == 1:
    day_ctr += 1 # add two days the year after leap year
  
  hold = 0
  if i%4 == 0: # leap year
    hold = num_sun_leap[day_ctr%7]
  else:
    hold = num_sun_reg[day_ctr%7]
  
  full_28 += hold
  if i <= 16:
    first_16 += hold
    #print('i: ' + str(i) + ' day_ctr: ' + str(day_ctr%7) + ' hold: ' + str(hold) + ' first_16: ' + str(first_16))

#print('first_16: ' + str(first_16) + ' full_28: ' + str(full_28))
answer = 3*full_28 + first_16

end_time = time.clock()
runtime = end_time - start_time

print('=======')
print('ANSWER:')
print('=======')
print('found in ' + str(runtime) + ' seconds')
print('final answer: ' + str(answer))


