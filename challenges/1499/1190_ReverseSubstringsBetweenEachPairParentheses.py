'''
1190. Reverse Substrings Between Each Pair of Parentheses

You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.
Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.

Constraints:

1 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It is guaranteed that all parentheses are balanced.
'''

class Solution:
  def reverseParentheses(self, s: str) -> str:
    curr = ''
    stack = []
    
    for ch in s:
      if ch == '(':
        stack.append(curr)
        curr = ''
        continue
        
      if ch == ')':
        curr = curr[::-1]
        if stack:
          curr = stack.pop() + curr
          
        continue
        
      curr += ch
    
    return curr
        
  def reverseParentheses(self, s: str) -> str:
    stack = ['']
    
    for i in range(len(s)):
      if s[i] == '(':
        stack.append('')
        continue
        
      if s[i] == ')':
        src = stack.pop()
        stack[-1] += src[::-1]
        continue
        
      stack[-1] += s[i]
      
    return stack[0]
    