text = """Number letter counts
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

print(text)

import time

start_time = time.clock()

# one,two,three,four,five,six,seven,eight,nine
singles = len('onetwothreefourfivesixseveneightnine')

# ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen
teens = len('teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen')

# ten twenty's + singles + ten thirty's + singles + ...
twenty_to_ninenine = 10*len('twentythirtyfortyfiftysixtyseventyeightyninety') + 8*singles

# one hundred * 100 + two hundred * 100 + ... = 100*(9*len('hundred')+singles)
hundreds = 100*(9*len('hundred')+singles)
hundreds += 9*(singles+teens+twenty_to_ninenine) # 9 sets of 1-99
hundreds += len('and')*99*9 # 9 sets of 99 ands

one_thou = len('onethousand')

answer = singles + teens + twenty_to_ninenine + hundreds + one_thou

end_time = time.clock()
runtime = end_time - start_time

print('=======')
print('ANSWER:')
print('=======')
print('found in ' + str(runtime) + ' seconds')
print('number of letters: ' + str(answer))

