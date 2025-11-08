'''
3739-count-subarrays-with-majority-element-ii
'''

from typing import List


class Solution:
  def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
    n = len(nums)
    count = [1] + [0]*(n+n+2)
    acc = [1] + [0]*(n+n+2)
    res = 0
    prefix = 0

    # count how many prefix sums are less than current prefix sum
    # then the subarrays ending at current index from these prefix
    # positions would be the "majority subarrays"
    for val in nums:
      prefix += 1 if val == target else -1
      count[prefix] += 1
      acc[prefix] = acc[prefix-1] + count[prefix]
      res += acc[prefix-1]

    return res
    

        