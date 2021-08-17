'''
There is a strange printer with the following two special properties:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.

Example 1:

Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:

Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.

Constraints:

1 <= s.length <= 100
s consists of lowercase English letters.
'''


class Solution:
  def strangePrinter(self, s: str) -> int:
    rs = []
    cache = {}
    
    def dp(l: int, r: int) -> int:
      if l >= r:
        return 0 if l > r else 1
      
      if (l, r) in cache:
        return cache[l, r]
      
      ans = 1 + dp(l+1, r)
      
      for m in range(l+1, r+1):
        if rs[m] == rs[l]:
          # printing rs[l:m-1] is the same as rs[l:m], since we can print
          # rs[l] till position m, instad of m-1; then add the rs[m+1:r] part.
          # it is implied that any number at position l must be the first number
          # to print, because otherwise it will overwrite any prior prints and
          # invalidate those prior steps, because 1 + dp(l+1, r) covered the 
          # other corner case; can't use the 1 + ... scheme, since that will 
          # double count the same numbers in the smaller intervals
          ans = min(ans, dp(l, m-1) + dp(m+1, r))
      
      cache[l, r] = ans
      return ans
    
    for ch in s:
      if rs and ch == rs[-1]:
        continue
        
      rs.append(ch)
    
    return dp(0, len(rs)-1)
  