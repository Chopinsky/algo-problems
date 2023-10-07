'''
1420. Build Array Where You Can Find The Maximum Exactly K Comparisons

You are given three integers n, m and k. Consider the following algorithm to find the maximum element of an array of positive integers:

You should build the array arr which has the following properties:

arr has exactly n integers.
1 <= arr[i] <= m where (0 <= i < n).
After applying the mentioned algorithm to arr, the value search_cost is equal to k.
Return the number of ways to build the array arr under the mentioned conditions. As the answer may grow large, the answer must be computed modulo 109 + 7.

Example 1:

Input: n = 2, m = 3, k = 1
Output: 6
Explanation: The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]
Example 2:

Input: n = 5, m = 2, k = 3
Output: 0
Explanation: There are no possible arrays that satisify the mentioned conditions.
Example 3:

Input: n = 9, m = 1, k = 1
Output: 1
Explanation: The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]

Constraints:

1 <= n <= 50
1 <= m <= 100
0 <= k <= n
'''

from functools import lru_cache


class Solution:
  def numOfArrays(self, n: int, m: int, k: int) -> int:
    mod = 10**9 + 7
    
    @lru_cache(None)
    def dp(i: int, last: int, rem: int):
      if m-last < rem:
        return 0
      
      if rem == 0:
        # print('end:', (i, last))
        return pow(last, (n-i), mod)
      
      if i >= n:
        return 0
      
      cnt = 0 if i == 0 else (last * dp(i+1, last, rem)) % mod
      # print('base:', (i, last, rem), cnt)
      
      for val in range(last+1, m+1):
        c0 = dp(i+1, val, rem-1)
        if c0 <= 0:
          break
          
        cnt = (cnt + c0) % mod
        # print((i, last, rem), val, c0)
      
      return cnt
      
    return dp(0, 0, k)
