'''
1027. Longest Arithmetic Subsequence

Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

Recall that a subsequence of an array nums is a list nums[i1], nums[i2], ..., nums[ik] with 0 <= i1 < i2 < ... < ik <= nums.length - 1, and that a sequence seq is arithmetic if seq[i+1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).

Example 1:

Input: nums = [3,6,9,12]
Output: 4
Explanation: 
The whole array is an arithmetic sequence with steps of length = 3.
Example 2:

Input: nums = [9,4,7,2,10]
Output: 3
Explanation: 
The longest arithmetic subsequence is [4,7,10].
Example 3:

Input: nums = [20,1,15,3,10,5,8]
Output: 4
Explanation: 
The longest arithmetic subsequence is [20,15,10,5].

Constraints:

2 <= nums.length <= 1000
0 <= nums[i] <= 500
'''

from typing import List
from collections import Counter, defaultdict


class Solution:
  def longestArithSeqLength(self, nums: List[int]) -> int:
    seen = []
    long = 1
    
    for v0 in nums:
      s0 = {v0:1}
      for (v1, s1) in seen:
        diff = v0-v1
        s0[diff] = max(s0.get(diff, 0), 1+s1.get(diff, 1))
        
      long = max(long, max(s0.values()))
      seen.append((v0, s0))

    # print(seen)
    return long
  
  
  def longestArithSeqLength(self, nums: List[int]) -> int:
    n = len(nums)
    if n <= 2:
      return n
    
    dp = {}
    long = max(Counter(nums).values())
    # print(long)
    
    for base in nums:
      curr = defaultdict(int)

      for val in dp:
        if base == val:
          continue
          
        diff = base-val
        if diff not in dp[val]:
          curr[diff] = max(curr[diff], 2)
        else:
          curr[diff] = max(curr[diff], 1+dp[val][diff])

      dp[base] = curr
      if curr:
        long = max(long, max(curr.values()))

    # print(dp)
    return long
  