'''
1409-queries-on-a-permutation-with-key
'''

from typing import List


class Solution:
  def processQueries(self, queries: List[int], m: int) -> List[int]:
    p = [i+1 for i in range(m)]
    ans = []

    for val in queries:
      pos = p.index(val)
      p.pop(pos)
      p = [val] + p
      # print('iter:', val, p)
      ans.append(pos)

    return ans
        