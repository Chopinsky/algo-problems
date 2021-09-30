'''
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Example 3:

Input: s = "a"
Output: "a"

Example 4:

Input: s = "ac"
Output: "a"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''


class Solution:
  def longestPalindrome(self, s: str) -> str:
    def count(i: int, j: int):
      c = 0
      if i == j:
        c += 1
        i -= 1
        j += 1
        
      while i >= 0 and j < len(s):
        if s[i] != s[j]:
          break
          
        c += 2
        i -= 1
        j += 1
          
      return c, i+1, j
      
    max_len = 1
    max_pal = s[0]
    
    for i in range(1, len(s)):
      max_local, b, e = max(count(i-1, i), count(i, i))
      if max_local > max_len:
        max_len = max_local
        max_pal = s[b:e]
        
      # print(i, max_local, b, e)
      max_len = max(max_len, max_local)
        
    return max_pal
  