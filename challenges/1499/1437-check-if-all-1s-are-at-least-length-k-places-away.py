'''
1437-check-if-all-1s-are-at-least-length-k-places-away
'''

from typing import List


class Solution:
  def kLengthApart(self, nums: List[int], k: int) -> bool:
    prev = -1
    n = len(nums)

    for i in range(n):
      if nums[i] == 0:
        continue

      # print('found:', (prev, i))
      if prev >= 0 and i-prev-1 < k:
        return False

      prev = i

    return True

        