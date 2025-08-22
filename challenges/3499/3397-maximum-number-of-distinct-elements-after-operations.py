'''
3397-maximum-number-of-distinct-elements-after-operations
'''

from typing import List


class Solution:
  def maxDistinctElements(self, nums: List[int], k: int) -> int:
    nums.sort()
    count = 0
    n = len(nums)

    for i in range(n):
      if i == 0 or nums[i-1] < nums[i]-k:
        nums[i] -= k
        count += 1
        continue

      if nums[i-1] == nums[i]+k:
        nums[i] += k
        continue

      nums[i] = nums[i-1]+1
      count += 1
      continue

    return count
        