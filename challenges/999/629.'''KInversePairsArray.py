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
    # dp stores
    mod = 10**9 + 7
    dp = [[0]*(k+1) for _ in range(n+1)]

    # init condition: if n==1, only k==0 has 1 solution
    dp[1][0] = 1
    
    # looping through all (n, k) problems
    for i in range(2, n+1):
      # initial count is 0
      cnt = 0

      # for each (n-1, j) solution, we can shift number `n` by j times to
      # generate the answer for the (n, k) solution
      for j in range(0, k+1):
        # all previous solutions (e.g. j0 inverse pairs), just
        # shift number (j-j0) times to create total of `j` inverse
        # pairs, so we just add them to the running sum
        cnt += dp[i-1][j] 

        # minus the illicit cases -- even `i` swaps won't yield j more
        # reverse pairs from these base cases
        if j >= i:
          cnt -= dp[i-1][j-i]
          
        dp[i][j] = cnt % mod
        if dp[i][j] == 0:
          break
    
    # print(dp)
    return dp[n][k]