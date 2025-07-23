'''
You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

Example 1:

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
Example 2:

Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
'''

from typing import List
from collections import defaultdict


class Solution:
  def maximumUniqueSubarray(self, nums: List[int]) -> int:
    n = len(nums)
    res = 0
    l = 0
    vals = defaultdict(int)
    curr = 0

    for r in range(n):
      val = nums[r]
      curr += val
      vals[val] += 1

      while l < r and vals[val] > 1:
        v0 = nums[l]
        curr -= v0
        vals[v0] -= 1
        l += 1

      # print('subarr', (l, r), curr)
      res = max(res, curr)

    return res
        
  def maximumUniqueSubarray(self, nums: List[int]) -> int:
    max_score, curr_score = 0, 0
    uniq = set()
    i, j = 0, 0
    n = len(nums)
    
    while j < n:
      while j < n and nums[j] not in uniq:
        uniq.add(nums[j])
        curr_score += nums[j]
        j += 1
        
      max_score = max(max_score, curr_score)
      # print(i, j, uniq)
      
      curr_score -= nums[i]
      uniq.discard(nums[i])
      i += 1
      
    return max_score
    