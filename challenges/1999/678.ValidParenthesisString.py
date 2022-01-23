'''
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true
 

Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.
'''


from functools import lru_cache


class Solution:
  def checkValidString(self, s: str) -> bool:
    n = len(s)
    
    @lru_cache(None)
    def match(start: int, opened: int) -> bool:
      if start >= n:
        return opened == 0
      
      if opened < 0:
        return False
        
      for i in range(start, n):
        if s[i] == '(':
          opened += 1
        
        elif s[i] == ')':
          opened -= 1
          if opened < 0:
            return False
          
        # if '*' as '(', '', and ')'
        return match(i+1, opened+1) or match(i+1, opened) or match(i+1, opened-1)
        
      return opened == 0
        
    return match(0, 0)
  