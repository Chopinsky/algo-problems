'''
You are given a 0-indexed string s and are tasked with finding two non-intersecting palindromic substrings of odd length such that the product of their lengths is maximized.

More formally, you want to choose four integers i, j, k, l such that 0 <= i <= j < k <= l < s.length and both the substrings s[i...j] and s[k...l] are palindromes and have odd lengths. s[i...j] denotes a substring from index i to index j inclusive.

Return the maximum possible product of the lengths of the two non-intersecting palindromic substrings.

A palindrome is a string that is the same forward and backward. A substring is a contiguous sequence of characters in a string.

Example 1:

Input: s = "ababbb"
Output: 9
Explanation: Substrings "aba" and "bbb" are palindromes with odd length. product = 3 * 3 = 9.
Example 2:

Input: s = "zaaaxbbby"
Output: 9
Explanation: Substrings "aaa" and "bbb" are palindromes with odd length. product = 3 * 3 = 9.
 

Constraints:

2 <= s.length <= 10^5
s consists of lowercase English letters.
'''


import math
from heapq import heappop, heappush


class Solution:
  '''
  key is to generate longest palindrom substr's 1-arm size using the manacher's algo,
  then to each char, find the longest palindrom in s[:l] and s[r:]
  '''
  def maxProduct(self, s: str) -> int:
    prod = 1
    n = len(s)
    if n == 2:
      return 1
    
    # manacher's algo
    n = len(s)
    base = '$' + s + '^'
    p = [0] * (n+2)  # palindrom's 1-arm length
    l, r = 0, -1     # current [left, right] range

    for i in range(1, n+1):
      # the longest pal if we're still in the range
      p[i] = max(0, min(r-i, p[l+(r-i)] if 0 <= l+r-i < n+2 else math.inf))
      
      # expand the palindrom if we can
      while i-p[i] >= 0 and i+p[i] < n and base[i-p[i]] == base[i+p[i]]:
        p[i] += 1

      # update the range
      if i+p[i] > r:
        l = i-p[i]
        r = i+p[i]

    p = p[1:-1]  # pop mocking chars
    prefix = [1] * n
    suffix = [1] * n
    stack = []
    
    for i in range(1, n):
      prefix[i] = max(prefix[i], prefix[i-1])
      while stack and stack[0][1] < i:
        heappop(stack)
        
      if stack:
        center = stack[0][0]
        prefix[i] = max(prefix[i], 2*(i-center) + 1)
        
      heappush(stack, (i, i+p[i]-1))
    
    stack.clear()
    
    for i in range(n-2, -1, -1):
      suffix[i] = max(suffix[i+1], suffix[i])
      while stack and stack[0][1] > i:
        heappop(stack)
        
      if stack:
        center = -stack[0][0]
        suffix[i] = max(suffix[i], 2*(center-i) + 1)
  
      heappush(stack, (-i, i-p[i]+1))
    
    for i in range(n-1):
      # print('pair:', i, prefix[i], suffix[i+1])
      prod = max(prod, prefix[i] * suffix[i+1])
    
    return prod
  