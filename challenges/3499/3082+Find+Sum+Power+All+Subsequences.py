'''
Find the Sum of the Power of All Subsequences

You are given an integer array nums of length n and a positive integer k.

The power of an array of integers is defined as the number of subsequences with their sum equal to k.

Return the sum of power of all subsequences of nums.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input:  nums = [1,2,3], k = 3 

Output:  6 

Explanation:

There are 5 subsequences of nums with non-zero power:

The subsequence [1,2,3] has 2 subsequences with sum == 3: [1,2,3] and [1,2,3].
The subsequence [1,2,3] has 1 subsequence with sum == 3: [1,2,3].
The subsequence [1,2,3] has 1 subsequence with sum == 3: [1,2,3].
The subsequence [1,2,3] has 1 subsequence with sum == 3: [1,2,3].
The subsequence [1,2,3] has 1 subsequence with sum == 3: [1,2,3].
Hence the answer is 2 + 1 + 1 + 1 + 1 = 6.

Example 2:

Input:  nums = [2,3,3], k = 5 

Output:  4 

Explanation:

There are 3 subsequences of nums with non-zero power:

The subsequence [2,3,3] has 2 subsequences with sum == 5: [2,3,3] and [2,3,3].
The subsequence [2,3,3] has 1 subsequence with sum == 5: [2,3,3].
The subsequence [2,3,3] has 1 subsequence with sum == 5: [2,3,3].
Hence the answer is 2 + 1 + 1 = 4.

Example 3:

Input:  nums = [1,2,3], k = 7 

Output:  0 

Explanation: There exists no subsequence with sum 7. Hence all subsequences of nums have power = 0.

Constraints:

1 <= n <= 100
1 <= nums[i] <= 10^4
1 <= k <= 100
'''

from typing import List
from functools import lru_cache

class Solution:
  def sumOfPower(self, nums: List[int], k: int) -> int:
    s0 = sum(nums)
    if s0 <= k:
      return 0 if s0 < k else 1
    
    mod = 10**9 + 7
    n = len(nums)
    
    suffix = [val for val in nums]
    for i in range(n-2, -1, -1):
      suffix[i] += suffix[i+1]
    
    @lru_cache(None)
    def dp(i: int, rem: int):
      if i >= n or rem < 0:
        return 0
      
      if rem == 0:
        c0 = 1 if i == n-1 else dp(i+1, 0)
        return (2*c0) % mod
      
      if rem >= suffix[i]:
        return 1 if rem == suffix[i] else 0
      
      val = nums[i]
      if val > rem:
        return (2*dp(i+1, rem)) % mod
      
      # if i == 0:
      #   print(dp(i+1, rem-val), dp(i+1, rem))
      
      return (dp(i+1, rem-val) + 2*dp(i+1, rem)) % mod
    
    return dp(0, k)
        