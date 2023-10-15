'''
You are given a 0-indexed array nums of non-negative integers, and two integers l and r.

Return the count of sub-multisets within nums where the sum of elements in each subset falls within the inclusive range of [l, r].

Since the answer may be large, return it modulo 109 + 7.

A sub-multiset is an unordered collection of elements of the array in which a given value x can occur 0, 1, ..., occ[x] times, where occ[x] is the number of occurrences of x in the array.

Note that:

Two sub-multisets are the same if sorting both sub-multisets results in identical multisets.
The sum of an empty multiset is 0.

Example 1:

Input: nums = [1,2,2,3], l = 6, r = 6
Output: 1
Explanation: The only subset of nums that has a sum of 6 is {1, 2, 3}.
Example 2:

Input: nums = [2,1,4,2,7], l = 1, r = 5
Output: 7
Explanation: The subsets of nums that have a sum within the range [1, 5] are {1}, {2}, {4}, {2, 2}, {1, 2}, {1, 4}, and {1, 2, 2}.
Example 3:

Input: nums = [1,2,1,3,5,2], l = 3, r = 5
Output: 9
Explanation: The subsets of nums that have a sum within the range [3, 5] are {3}, {5}, {1, 2}, {1, 3}, {2, 2}, {2, 3}, {1, 1, 2}, {1, 1, 3}, and {1, 2, 2}.

Constraints:

1 <= nums.length <= 2 * 10^4
0 <= nums[i] <= 2 * 10^4
Sum of nums does not exceed 2 * 10^4.
0 <= l <= r <= 2 * 10^4
'''

from typing import List
from collections import Counter


class Solution:
  def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
    mod = 10**9+7
    c = Counter(nums)
    dp, nxt = [0]*(r+1), [0]*(r+1)
    dp[0] = 1
    
    if 0 in c:
      dp[0] += c[0]
      del c[0]
    
    def update(v0: int, cnt: int):
      s = [dp[i] for i in range(v0)]
      
      for v1 in range(v0, r+1):
        idx = v1 % v0
        nxt[v1] = s[idx]
        
        # update prefix-accumulations
        s[idx] = (s[idx] + dp[v1]) % mod
        
        # pop left
        left_val = v1 - v0*(cnt+1)
        if left_val >= 0:
          s[idx] = (s[idx]+mod-dp[left_val]) % mod
        
      # merge back
      for i in range(len(nxt)):
        if i > 0:
          dp[i] = (dp[i] + nxt[i]) % mod

        nxt[i] = 0
    
    for val in sorted(c):
      if val > r:
        break
        
      update(val, c[val])
      
    cnt = 0
    for i in range(l, r+1):
      cnt = (cnt + dp[i]) % mod
    
    return cnt
