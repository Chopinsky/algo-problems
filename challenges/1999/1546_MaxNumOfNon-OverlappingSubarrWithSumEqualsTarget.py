'''
Given an array nums and an integer target, return the maximum number of non-empty non-overlapping subarrays such that the sum of values in each subarray is equal to target.

Example 1:

Input: nums = [1,1,1,1,1], target = 2
Output: 2
Explanation: There are 2 non-overlapping subarrays [1,1,1,1,1] with sum equals to target(2).
Example 2:

Input: nums = [-1,3,5,1,4,2,-9], target = 6
Output: 2
Explanation: There are 3 subarrays with sum equal to 6.
([5,1], [4,2], [3,5,1,4,2,-9]) but only the first 2 are non-overlapping.

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
0 <= target <= 10^6
'''


from typing import List
from collections import defaultdict


class Solution:
  def maxNonOverlapping(self, nums: List[int], target: int) -> int:
    prefix_sum, count = 0, 0
    seen = {0}
    
    for val in nums:
      prefix_sum += val
      if prefix_sum - target in seen:
        prefix_sum = 0
        count += 1
        seen.clear()

      seen.add(prefix_sum)
          
    return count
    
    
  def maxNonOverlapping0(self, nums: List[int], target: int) -> int:
    prefix = 0
    n = len(nums)
    cnt = [0] * n
    ps = defaultdict(list)
    most_cnt = 0
    
    for i in range(n):
      prefix += nums[i]
      prev = prefix - target
      
      for j in ps[prev]:
        cnt[i] = max(cnt[i], 1+cnt[j])
        
      if i > 0:
        cnt[i] = max(cnt[i], cnt[i-1] + (1 if nums[i] == target else 0))
        
      if prefix == target:
        cnt[i] = max(1, cnt[i])
        
      ps[prefix].append(i)
      most_cnt = max(most_cnt, cnt[i])
      # print(nums[i], prefix, prev, cnt[i])
        
    return most_cnt
                     