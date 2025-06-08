'''
3346-maximum-frequency-of-an-element-after-performing-operations-i
'''

from collections import Counter
from typing import List


class Solution:
  def maxFrequency(self, nums: List[int], k: int, ops: int) -> int:
    max_freq = 1
    c = Counter(nums)
    nums.sort()
    l, r = 0, 0
    n = len(nums)

    for val in range(nums[0], nums[-1]+1):
      while l < n and nums[l] < val-k:
        l += 1

      while r < n and nums[r] <= val+k:
        r += 1

      # print('iter:', val, (l, r))
      cnt = c.get(val, 0)
      freq = cnt + min(ops, (r-l) - cnt)
      max_freq = max(max_freq, freq)

    return max_freq
        