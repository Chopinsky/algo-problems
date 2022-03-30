'''
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.

Example 1:

Input: s = "()"
Output: 1
Example 2:

Input: s = "(())"
Output: 2
Example 3:

Input: s = "()()"
Output: 2
 

Constraints:

2 <= s.length <= 50
s consists of only '(' and ')'.
s is a balanced parentheses string.
'''


class Solution:
  def scoreOfParentheses(self, s: str) -> int:
    def dp(i: int, j: int) -> int:
      if i+1 == j:
        return 1
      
      bal = 0
      start = i
      score = 0
      
      for k in range(i, j+1):
        if s[k] == '(':
          bal += 1
        else:
          bal -= 1
          
        if bal == 0:
          if start == i and k == j:
            return 2 * dp(i+1, j-1)
          
          score += dp(start, k)
          start = k+1
          
      return score
      
    return dp(0, len(s)-1)
  