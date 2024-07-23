'''
3202. Find the Maximum Length of Valid Subsequence II

You are given an integer array nums and a positive integer k.
A subsequence sub of nums with length x is called valid if it satisfies:

(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.
Return the length of the longest valid subsequence of nums.

Example 1:

Input: nums = [1,2,3,4,5], k = 2

Output: 5

Explanation:

The longest valid subsequence is [1, 2, 3, 4, 5].

Example 2:

Input: nums = [1,4,2,3,1,4], k = 3

Output: 4

Explanation:

The longest valid subsequence is [1, 4, 1, 4].

Constraints:

2 <= nums.length <= 10^3
1 <= nums[i] <= 10^7
1 <= k <= 10^3
'''

from typing import List

class Solution:
  def maximumLength(self, nums: List[int], k: int) -> int:
    seq = {}
    long = 2
    
    for v0 in nums:
      v1 = v0 % k
      curr = {}
      
      for v2 in seq:
        v3 = (v1+v2) % k
        curr[v3] = max(curr.get(v3, 0), 1+seq[v2].get(v3, 1))
        long = max(long, curr[v3])
        
      # merge longest seq ending with v1
      d = seq.get(v1, {})
      for v2 in d:
        curr[v2] = max(curr.get(v2, 0), d[v2])
        long = max(long, curr[v2])
        
      curr[v1] = max(curr.get(v1, 0), 1)
      seq[v1] = curr
        
    return long
  