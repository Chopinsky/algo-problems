'''
2452. Maximum Number of Non-overlapping Palindrome Substrings

You are given a string s and a positive integer k.

Select a set of non-overlapping substrings from the string s that satisfy the following conditions:

The length of each substring is at least k.
Each substring is a palindrome.
Return the maximum number of substrings in an optimal selection.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "abaccdbbd", k = 3
Output: 2
Explanation: We can select the substrings underlined in s = "abaccdbbd". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
It can be shown that we cannot find a selection with more than two valid substrings.
Example 2:

Input: s = "adbcda", k = 2
Output: 0
Explanation: There is no palindrome substring of length at least 2 in the string.
 
Constraints:

1 <= k <= s.length <= 2000
s consists of lowercase English letters.
'''

from bisect import bisect_left
from functools import lru_cache


class Solution:
  def maxPalindromes(self, s: str, k: int) -> int:
    n = len(s)
    if k == 1:
      return n

    odd, even = [], []
    odd_padding = k // 2
    even_padding = max(0, (k//2) - 1)
    
    def pal_size(i: int):
      o, e = 0, 0
      
      # odd size
      l, r = i, i
      while o < k and l >= 0 and r < n and s[l] == s[r]:
        o = r - l + 1
        l -= 1
        r += 1
      
      l, r = i, i+1
      while e < k and l >= 0 and r < n and s[l] == s[r]:
        e = r - l + 1
        l -= 1
        r += 1
      
      return o, e
    
    for i in range(n):
      o, e = pal_size(i)
      if o >= k:
        odd.append(i)
        
      if e >= k:
        even.append(i)
      
    # print(odd, even)  
    if not odd and not even:
      return 0
    
    @lru_cache(None)
    def dp(i: int) -> int:
      l, r = i+odd_padding, i+even_padding
      if l >= n and r >= n:
        return 0
      
      # if we don't take any from odd or even cand
      base = dp(i+1)
      
      # if take next odd-len pal
      j = bisect_left(odd, l)
      if j < len(odd) and odd[j] >= l:
        base = max(base, 1 + dp(odd[j] + odd_padding + 1))
      
      # if take next even-len pal
      j = bisect_left(even, r)
      if j < len(even) and even[j] >= r:
        base = max(base, 1 + dp(even[j] + even_padding + 2))
      
      return base
    
    return dp(0)
      