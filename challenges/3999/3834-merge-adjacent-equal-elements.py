'''
3834-merge-adjacent-equal-elements
'''

from typing import List


class Solution:
  def mergeAdjacent(self, nums: List[int]) -> List[int]:
    ans = []

    for val in nums:
      ans.append(val)
      while len(ans) >= 2 and ans[-1] == ans[-2]:
        ans[-2] += ans.pop()

    return ans
