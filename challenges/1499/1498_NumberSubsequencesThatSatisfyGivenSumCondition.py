'''
1498. Number of Subsequences That Satisfy the Given Sum Condition

You are given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.

Example 1:

Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)
Example 2:

Input: nums = [3,3,6,8], target = 10
Output: 6
Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
Example 3:

Input: nums = [2,3,3,4,6,7], target = 12
Output: 61
Explanation: There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61).

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
1 <= target <= 10^6
'''

from bisect import bisect_right
from functools import lru_cache
from typing import List


class Solution:
  def numSubseq(self, nums: List[int], target: int) -> int:
    mod = 10**9 + 7
    nums.sort()
    
    @lru_cache(None)
    def calc(m: int) -> int:
      return pow(2, m, mod)
    
    i, j = 0, len(nums)-1
    cnt = 0
    
    while i <= j:
      while i <= j and nums[i]+nums[j] > target:
        j -= 1
        
      if i > j:
        break
        
      cnt = (cnt + calc(j-i)) % mod
      i += 1
      
    return cnt
    

  def numSubseq(self, nums: List[int], target: int) -> int:
    nums.sort()
    count = 0
    mod = 10**9 + 7
    
    # nums[i] as the min value in the subseq, find the max
    # value for the subseq
    for i in range(len(nums)):
      # won't find another match
      if 2*nums[i] > target:
        break
        
      # the the max-value index for the range
      j = bisect_right(nums, target-nums[i]) - 1
      if j < i:
        break
        
      # find all combinations of numbers that can form
      # the subseq with nums[i] as the min-val of the array
      count = (count + pow(2, j-i, mod)) % mod
      # count = (count + (1 << (j-i))) % mod
      
    return count
  