'''
3660-jump-game-ix
'''

from typing import List


class Solution:
  def maxValue(self, nums: List[int]) -> List[int]:
    n = len(nums)

    # suffix min
    s = nums.copy()
    for i in range(n-2, -1, -1):
      s[i] = min(s[i], s[i+1])

    ans = []
    high = 0

    for i, val in enumerate(nums):
      high = max(high, val)

      # end of the connected component (which must be 
      # an subarray), can't go right
      if i == n-1 or high <= s[i+1]:
        ans.extend([high] * (i+1-len(ans)))
        high = 0

    return ans
        