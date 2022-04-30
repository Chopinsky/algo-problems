'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 10^5
s consists of lowercase English letters.
'''

class Solution:
  def validPalindrome(self, s: str) -> bool:
    def pali(l: int, r: int, rem: int) -> bool:
      while l < r:
        if s[l] != s[r]:
          if rem == 0:
            return False
          
          return pali(l+1, r, rem-1) or pali(l, r-1, rem-1)
          
        l += 1
        r -= 1
        
      return True
      
    return pali(0, len(s)-1, 1)
  