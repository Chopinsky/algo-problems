'''
Given a string s, determine if it is valid.

A string s is valid if, starting with an empty string t = "", you can transform t into s after performing the following operation any number of times:

Insert string "abc" into any position in t. More formally, t becomes tleft + "abc" + tright, where t == tleft + tright. Note that tleft and tright may be empty.
Return true if s is a valid string, otherwise, return false.

Example 1:

Input: s = "aabcbc"
Output: true
Explanation:
"" -> "abc" -> "aabcbc"
Thus, "aabcbc" is valid.
Example 2:

Input: s = "abcabcababcc"
Output: true
Explanation:
"" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
Thus, "abcabcababcc" is valid.
Example 3:

Input: s = "abccba"
Output: false
Explanation: It is impossible to get "abccba" using the operation.

Constraints:

1 <= s.length <= 2 * 10^4
s consists of letters 'a', 'b', and 'c'
'''


class Solution:
  def isValid(self, s: str) -> bool:
    stack, nxt = list(s), []
    
    while stack:
      idx = 0
      for ch in stack:
        nxt.append(ch)
        
        if ch == 'a' and idx == 0:
          idx += 1
          
        elif ch == 'b' and idx == 1:
          idx += 1
          
        elif ch == 'c' and idx == 2:
          nxt = nxt[:-3]
          if nxt and nxt[-1] == 'a':
            idx = 1
          
          elif len(nxt) >= 2 and nxt[-2:] == 'ab':
            idx == 2
            
          else:
            idx = 0
          
        else:
          idx = 1 if ch == 'a' else 0
      
      if len(stack) == len(nxt):
        return False
      
      stack, nxt = nxt, stack
      nxt.clear()
      
    return True
  