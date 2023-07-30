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

from functools import lru_cache


class Solution:
  def strangePrinter(self, s: str) -> int:
    @lru_cache(None)
    def dp(i: int, j: int) -> int:
      if i >= j:
        return 1 if i == j else 0
      
      ch_set = set(s[i:j+1])
      if len(ch_set) == 1:
        return 1
      
      if len(ch_set) == j-i+1:
        return j-i+1
      
      ch = s[i]
      stack = []
      start, end = -1, -1
      
      for k in range(i+1, j+1):
        if s[k] == ch:
          if start >= 0:
            stack.append((start, end))
            
          start, end = -1, -1
          
        else:
          end = k
          if start < 0:
            start = k
            
      if start >= 0 and end >= 0:
        stack.append((start, end))
      
      # print('init:', (i, j), stack)
      if not stack:
        return 1
      
      ops = 1+dp(stack[0][0], j)
      prev = 0
      
      for k in range(len(stack)):
        i0, j0 = stack[k]
        prev += dp(i0, j0)
        nxt = 0 if k == len(stack)-1 else dp(stack[k+1][0], j)
        ops = min(ops, 1+prev+nxt, 1+dp(stack[0][0], j0)+nxt)
        
        end = j if k == len(stack)-1 else stack[k+1][0]-1
        if end != j:
          ops = min(ops, dp(i, end)+nxt)
      
      if stack[-1][1] != j:
        ops = min(ops, dp(i, stack[-1][1]))
        
      # print('done:', (i, j), s[i:j+1], ops)
      return ops
      
    return dp(0, len(s)-1)
        

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
  