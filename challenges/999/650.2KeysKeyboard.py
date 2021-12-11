'''
There is only one character 'A' on the screen of a notepad. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.

Example 1:

Input: n = 3
Output: 3
Explanation: Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
Example 2:

Input: n = 1
Output: 0

Constraints:

1 <= n <= 1000
'''


from functools import lru_cache


class Solution:
  def minSteps(self, n: int) -> int:
    @lru_cache(None)
    def reduce(n: int) -> int:
      if n == 1:   
        return 0

      # increament by 1 till the divisor, then repeat
      d = 2
      while n%d != 0:
        d = d + 1
      
      return reduce(n//d) + d
    
    return reduce(n)
          
          
  def minSteps0(self, n: int) -> int:
    dp = [(0, 0), (2, 1), (3, 1)]
    if n <= 3:
      return dp[n-1][0]
    
    while len(dp) < n:
      curr = len(dp)+1
      cnt = curr
      inc = 1
      
      for last in range(2, curr):
        if last+last == curr and dp[last-1][0]+2 < cnt:
          cnt = dp[last-1][0] + 2
          inc = last
          
        if (curr-last) % (dp[last-1][1]) == 0:
          extra = (curr-last) // dp[last-1][1]
          if dp[last-1][0] + extra < cnt:
            cnt = dp[last-1][0] + extra
            inc = dp[last-1][1]
          
        
      dp.append((cnt, inc))
      
    # print(dp)
    return dp[-1][0]
      