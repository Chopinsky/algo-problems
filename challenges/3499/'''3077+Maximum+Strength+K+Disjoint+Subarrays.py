'''
3077. Maximum Strength of K Disjoint Subarrays

You are given a 0-indexed array of integers nums of length n, and a positive odd integer k.

The strength of x subarrays is defined as strength = sum[1] * x - sum[2] * (x - 1) + sum[3] * (x - 2) - sum[4] * (x - 3) + ... + sum[x] * 1 where sum[i] is the sum of the elements in the ith subarray. Formally, strength is sum of (-1)i+1 * sum[i] * (x - i + 1) over all i's such that 1 <= i <= x.

You need to select k disjoint subarrays from nums, such that their strength is maximum.

Return the maximum possible strength that can be obtained.

Note that the selected subarrays don't need to cover the entire array.

Example 1:

Input: nums = [1,2,3,-1,2], k = 3
Output: 22
Explanation: The best possible way to select 3 subarrays is: nums[0..2], nums[3..3], and nums[4..4]. The strength is (1 + 2 + 3) * 3 - (-1) * 2 + 2 * 1 = 22.
Example 2:

Input: nums = [12,-2,-2,-2,-2], k = 5
Output: 64
Explanation: The only possible way to select 5 disjoint subarrays is: nums[0..0], nums[1..1], nums[2..2], nums[3..3], and nums[4..4]. The strength is 12 * 5 - (-2) * 4 + (-2) * 3 - (-2) * 2 + (-2) * 1 = 64.
Example 3:

Input: nums = [-1,-2,-3], k = 1
Output: -1
Explanation: The best possible way to select 1 subarray is: nums[0..0]. The strength is -1.

Constraints:

1 <= n <= 10^4
-10^9 <= nums[i] <= 10^9
1 <= k <= n
1 <= n * k <= 10^6
k is odd.
'''

from typing import List
from collections import defaultdict

class Solution:
  def maximumStrength(self, nums: List[int], k: int) -> int:
    n = len(nums)
    dp = {}
    dp[n, 0, 0] = 0
    
    def get(i, j, k):
      if j == 0:
        return 0 if k == 0 else -float('inf')
      
      if (i, j, k) not in dp:
        return -float('inf')
      
      return dp[i, j, k]
    
    for i in range(n-1, -1, -1):
      for j in range(min(k, n-i)+1):
        val = nums[i]*j if j%2 == 1 else -nums[i]*j
        
        # not select the number
        dp[i, j, 0] = max(get(i+1, j, 0), get(i+1, j, 1))
        
        # select the number
        dp[i, j, 1] = val + max(
          get(i+1, j-1, 0), # subarray end at i
          get(i+1, j-1, 1), # subarray end at i, a new subarray start at i+1
          get(i+1, j, 1),   # subarray continues to i+1
        )
    
    # print(dp)
    return max(get(0, k, 0), get(0, k, 1))

  def maximumStrength(self, nums: List[int], k: int) -> int:
    n = len(nums)
    
    # dp[i, j, k] is the max strength for suffix nums[i:] that needs
    # to split into j subarrays, and k = 0 or 1, where k = 0 means
    # no subarray in the iteration, and k = 1 means there is a continuous
    # subarray in the iteration
    dp = defaultdict(lambda: -float('inf'))
    dp[n, 0, 0] = 0
    
    for i in range(n-1, -1, -1):
      for j in range(min(k, n-i)+1):
        factor = j if j%2 == 1 else -j
        
        # continue the existing subarray by adding current element, then 
        # add the max of (end this subarray at i) or (continue this subarray
        # to i+1)
        dp[i, j, 1] = nums[i]*factor + max(dp[i+1, j-1, 0], dp[i+1, j, 1])
        
        # current subarray is empty, so we can choose to get the max of 
        # (empty subarray but from index i+1) or (start the subarray at i and
        # add the first element of nums[i] to it)
        dp[i, j, 0] = max(dp[i+1, j, 0], dp[i, j, 1])
    
    # print(dp)
    return max(dp[0, k, 0], dp[0, k, 1])
        