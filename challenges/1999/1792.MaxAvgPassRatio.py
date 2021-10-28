from typing import List
from heapq import heappop, heappush


class Solution:
  def max_pass_ratio(self, classes: List[List[int]], extra: int) -> float:
    q = []
    for p, t in classes:
      heappush(q, (p/t - (p+1)/(t+1), p, t))
    
    while extra:
      # add the student to score the best improvement
      # to this class
      _, p, t = heappop(q)
      p += 1
      t += 1

      # make sure the best average improvement is 
      # scored by adding this extra student, by using 
      # the potential avg improvement as the key.
      heappush(q, (p/t - (p+1)/(t+1), p, t))
      extra -= 1

    total = 0
    n = len(classes)
    # print(q)

    for _, p, t in q:
      total += p / t

    return (total / n)


s = Solution()
t = [
  [[[1,2], [3,5], [2,2]], 2, 0.78333],
  [[[2,4], [3,9], [4,5], [2,10]], 4, 0.53485],
]

for c, e, ans in t:
  res = s.max_pass_ratio(c, e)
  print('\n==========\nTest case:', c, e)
  print('Expected:', ans)
  print('Gotten  :', res)
