'''
1331-rank-transform-of-an-array
'''

from typing import List


class Solution:
  def arrayRankTransform(self, arr: List[int]) -> List[int]:
    rank = {}
    ans = []
    i = 1

    for val in sorted(arr):
      if val not in rank:
        rank[val] = i
        i += 1

    # print('init:', rank)
    for val in arr:
      ans.append(rank[val])

    return ans

  def arrayRankTransform(self, arr: List[int]) -> List[int]:
    vals = sorted(set(arr))
    ranks = {val:idx+1 for idx, val in enumerate(vals)}
    ans = []
    
    for val in arr:
      ans.append(ranks[val])
    
    return ans