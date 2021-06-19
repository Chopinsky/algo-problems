'''
For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.

Example 1:

Input: n = 3, k = 0
Output: 1
Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.

Example 2:

Input: n = 3, k = 1
Output: 2
Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.

Constraints:

1 <= n <= 1000
0 <= k <= 1000
'''


class Solution:
  '''
  idea is that we can get an array from any of the (n-1, k-i) arrays as long
  as k >= i, we can achieve this by appending number n to the (n-1, k-i) arrays,
  then shift k to the left by `i` times, which will create `i` extra inverse
  pairs, plus the existing `k-i` pairs, will generate the total of `k` pairs.
  Then the sum of (n, k) arrays will be sum((n-1, k-i) where i >= 0 and i <= k).
  '''
  def kInversePairs(self, n: int, k: int) -> int:
    dp = [[0 for _ in range(k+1)] for _ in range(n)]
    dp[0][0] = 1
    
    for i in range(1, n):
      s = 0
      for j in range(0, k+1):
        s += dp[i-1][j]
        if j > i:
          s -= dp[i-1][j-i-1]
          
        dp[i][j] = s
        if dp[i][j] == 0:
          break
    
    # print(dp)    
    
    return dp[n-1][k] % (10**9+7)