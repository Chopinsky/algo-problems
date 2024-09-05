'''
2740. Find the Value of the Partition
'''

from typing import List

class Solution:
  def findValueOfPartition(self, nums: List[int]) -> int:
    nums.sort()
    value = float('inf')
    
    for i in range(1, len(nums)):
      value = min(value, nums[i]-nums[i-1])
    
    return value
        