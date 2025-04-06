'''
1331. Rank Transform of an Array
'''

from typing import List

class Solution:
  def arrayRankTransform(self, arr: List[int]) -> List[int]:
    vals = sorted(set(arr))
    ranks = {val:idx+1 for idx, val in enumerate(vals)}
    ans = []
    
    for val in arr:
      ans.append(ranks[val])
    
    return ans
        