'''
1984-minimum-difference-between-highest-and-lowest-of-k-scores
'''

from typing import List


class Solution:
  def minimumDifference(self, nums: List[int], k: int) -> int:
    nums.sort()
    diff = nums[-1] - nums[0]

    for i in range(len(nums)-k+1):
      j = i+k-1
      # print('iter:', (i, j), nums[j], nums[i])
      diff = min(diff, nums[j]-nums[i])

    return diff
        