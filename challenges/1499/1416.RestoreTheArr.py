'''
A program was supposed to print an array of integers. The program forgot to print whitespaces and the array is printed as a string of digits s and all we know is that all integers in the array were in the range [1, k] and there are no leading zeros in the array.

Given the string s and the integer k, return the number of the possible arrays that can be printed as s using the mentioned program. Since the answer may be very large, return it modulo 109 + 7.

Example 1:

Input: s = "1000", k = 10000
Output: 1
Explanation: The only possible array is [1000]
Example 2:

Input: s = "1000", k = 10
Output: 0
Explanation: There cannot be an array that was printed this way and has all integer >= 1 and <= 10.
Example 3:

Input: s = "1317", k = 2000
Output: 8
Explanation: Possible arrays are [1317],[131,7],[13,17],[1,317],[13,1,7],[1,31,7],[1,3,17],[1,3,1,7]
Example 4:

Input: s = "2020", k = 30
Output: 1
Explanation: The only possible array is [20,20]. [2020] is invalid because 2020 > 30. [2,020] is ivalid because 020 contains leading zeros.
Example 5:

Input: s = "1234567890", k = 90
Output: 34
 

Constraints:

1 <= s.length <= 10^5
s consists of only digits and does not contain leading zeros.
1 <= k <= 10^9
'''

from functools import lru_cache


class Solution:
  def numberOfArrays(self, s: str, k: int) -> int:
    mod = 10**9 + 7
    n = len(s)
    
    @lru_cache(None)
    def dp(i: int):
      if i >= n:
        return 1
      
      if s[i] == '0':
        return 0
      
      cnt = 0
      base = 0
      
      for j in range(i, n):
        base = 10*base + int(s[j])
        if base > k:
          break
          
        # print((i,j,s[i:j]), base, dp(j+1))
        cnt = (cnt + dp(j+1)) % mod
        
      return cnt
    
    return dp(0)
      

  def numberOfArrays(self, s: str, k: int) -> int:
    if s[0] == '0':
      return 0
    
    if k < 10 and int(s[0]) > k:
      return 0
    
    mod = 10**9+7
    ns = len(s)
    sk = str(k)
    nk = len(sk)
    
    dp = [0] * ns
    for i in range(ns):
      count = 0
      if (i+1 < nk) or (i+1 == nk and int(s[:i+1]) <= k):
        count += 1
        
      # num starting from j, or s[j:i+1]
      for j in range(max(1, i-nk+1), i+1):
        # invalid division
        if not dp[j-1] or s[j] == '0':
          continue
          
        # increamental with s[j:i+1] plus all valid combos ending
        # with s[:j]
        if (i-j+1 < nk) or (i-j+1 == nk and int(s[j:i+1]) <= k):
          count += dp[j-1]
      
      dp[i] = count % mod
    
    return dp[-1]
  
