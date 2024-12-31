'''
2466. Count Ways To Build Good Strings

Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:

Append the character '0' zero times.
Append the character '1' one times.
This can be performed any number of times.

A good string is a string constructed by the above process having a length between low and high (inclusive).

Return the number of different good strings that can be constructed satisfying these properties. Since the answer can be large, return it modulo 109 + 7.

Example 1:

Input: low = 3, high = 3, zero = 1, one = 1
Output: 8
Explanation: 
One possible valid good string is "011". 
It can be constructed as follows: "" -> "0" -> "01" -> "011". 
All binary strings from "000" to "111" are good strings in this example.
Example 2:

Input: low = 2, high = 3, zero = 1, one = 2
Output: 5
Explanation: The good strings are "00", "11", "000", "110", and "011".

Constraints:

1 <= low <= high <= 10^5
1 <= zero, one <= low
'''


class Solution:
  def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
    mod = 10**9+7
    stack = [0]*(high+1)
    stack[0] = 1

    for i in range(high+1):
      j0 = i+zero
      if j0 <= high:
        stack[j0] = (stack[j0] + stack[i]) % mod

      j1 = i+one
      if j1 <= high:
        stack[j1] = (stack[j1] + stack[i]) % mod

    stack[0] = 0

    return sum(stack[low:]) % mod
        
  def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
    o, z = [0]*(high+1), [0]*(high+1)
    total = 0
    mod = 10**9 + 7
    
    for ln in range(1, high+1):
      if ln >= one:
        if ln == one:
          o[ln] = 1
        else:
          o[ln] = (o[ln] + o[ln-one] + z[ln-one]) % mod
        
      if ln >= zero:
        if ln == zero:
          z[ln] = 1
        else:
          z[ln] = (z[ln] + z[ln-zero] + o[ln-zero]) % mod
        
      if ln >= low:
        total = (total + o[ln] + z[ln]) % mod
      
    return total
        
  def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
    mod = 10**9 + 7
    total = 0
    dp = [0] * (high + 1)
    dp[zero] += 1
    dp[one] += 1
    
    for base in range(min(zero, one), high+1):
      v0, v1 = base+zero, base+one
      if base >= low:
        total = (total + dp[base]) % mod
      
      if v0 <= high:
        dp[v0] = (dp[v0] + dp[base]) % mod
        
      if v1 <= high:
        dp[v1] = (dp[v1] + dp[base]) % mod
    
    # print(dp)
    # print(sum(dp[low:]))
    return total
    