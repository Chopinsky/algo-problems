'''
2616. Minimize the Maximum Difference of Pairs

You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.

Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.

Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.

Example 1:

Input: nums = [10,1,2,7,1,3], p = 2
Output: 1
Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5. 
The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.
Example 2:

Input: nums = [4,2,1,2], p = 1
Output: 0
Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, which is the minimum we can attain.

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
0 <= p <= (nums.length)/2
'''

from typing import List


class Solution:
  def minimizeMax(self, nums: List[int], p: int) -> int:
    nums.sort()
    l, h = 0, nums[-1]-nums[0]
    last = h
    
    def check(d: int) -> bool:
      idx = 1
      cnt = 0
      
      while idx < len(nums) and cnt < p:
        if nums[idx]-nums[idx-1] <= d:
          cnt += 1
          idx += 2
        else:
          idx += 1
      
      return cnt >= p
    
    while l <= h:
      m = (l + h) // 2
      if check(m):
        last = m
        h = m - 1
      else:
        l = m + 1
        
    return last
        

  '''
  use greedy to check if we can get p-pairs that satisfy the max-diff value,
  and we can use binary search to figure out the max-diff value.
  '''
  def minimizeMax(self, nums: List[int], p: int) -> int:
    nums.sort()
    n = len(nums)
    l, r = 0, nums[-1]-nums[0]
    
    def check(diff):
      cnt = 0
      idx = 0
      
      while idx < n-1 and cnt < p:
        if nums[idx+1]-nums[idx] <= diff:
          cnt += 1
          idx += 1
        
        idx += 1
        continue
      
      return cnt >= p
    
    last = r
    while l <= r:
      mid = (l + r) // 2
      if check(mid):
        last = mid
        r = mid - 1
      else:
        l = mid + 1
        
    return last
  