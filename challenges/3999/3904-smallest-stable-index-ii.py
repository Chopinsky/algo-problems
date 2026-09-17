'''
3904-smallest-stable-index-ii
'''

from math import inf


class Solution:
  def firstStableIndex(self, nums: list[int], k: int) -> int:
    n = len(nums)
    high = [-inf]*n
    low = [inf]*n

    for i, val in enumerate(nums):
      if i == 0:
        high[i] = val
      else:
        high[i] = max(high[i-1], val)

    for i in range(n-1, -1, -1):
      val = nums[i]
      if i == n-1:
        low[i] = val
      else:
        low[i] = min(low[i+1], val)

    for i in range(n):
      score = high[i] - low[i]
      if score <= k:
        return i

    return -1
        