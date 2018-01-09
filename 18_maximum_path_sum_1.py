text = """Maximum path sum I
Problem 18

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

              75
             95 64
            17 47 82
           18 35 87 10
          20 04 82 47 65
         19 01 23 75 03 34
        88 02 77 73 07 63 67
       99 65 04 28 06 16 70 92
      41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
"""

print(text)

import time

# example: triangle = [[1],[2,3],[4,5,6],[7,8,9,10]]
def triangle_path(tri):
  """
  Determine shortest 1-step paths, 2-step paths, 3-step paths, ..., n-step path
  Iterate from bottom up starting at n-1 row getting the shortest path for each element
  based on the previously stored answers.
  """
  n = len(tri)
  answers = []
  for num in tri[-1]:
    answers.append({'dist':num,'path':list([num])})
  #print('n: ' + str(n) + ' answers: ' + str(answers))
  
  steps = 0
  for i in reversed(range(len(tri)-1)):
    prev_answers = list(answers)
    answers = []
    for j in range(len(tri[i])):
      steps += 2
      left = tri[i][j] + prev_answers[j]['dist']
      right = tri[i][j] + prev_answers[j+1]['dist']
      
      if left >= right:
        ans_ix = j
        ans_dist = left
      else:
        ans_ix = j+1
        ans_dist = right
      new_path = list(prev_answers[ans_ix]['path'])
      new_path.append(tri[i][j])
      answers.append({'dist':ans_dist, 'path':new_path})
      
      #print('i: ' + str(i) + ' j: ' + str(j) + ' answers: ' + str(answers))
  final = {}
  final['path'] = list(reversed(answers[0]['path']))
  final['dist'] = answers[0]['dist']
  print('steps: ' + str(steps))
  return final


start_time = time.clock()

#triangle = [[1],[2,3],[4,5,5],[7,8,10,10]]
triangle = [[75],
[95,64],
[17,47,82],
[18,35,87,10],
[20,4,82,47,65],
[19,1,23,75,3,34],
[88,2,77,73,7,63,67],
[99,65,4,28,6,16,70,92],
[41,41,26,56,83,40,80,70,33],
[41,48,72,33,47,32,37,16,94,29],
[53,71,44,65,25,43,91,52,97,51,14],
[70,11,33,28,77,73,17,78,39,68,17,57],
[91,71,52,38,17,14,91,43,58,50,27,29,48],
[63,66,4,68,89,53,67,30,73,16,69,87,40,31],
[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]
answer = triangle_path(triangle)

end_time = time.clock()
runtime = end_time - start_time

print('=======')
print('ANSWER:')
print('=======')
print('found in ' + str(runtime) + ' seconds')
print('final answer: ' + str(answer))












