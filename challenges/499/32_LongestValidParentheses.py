'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0

Constraints:

0 <= s.length <= 3 * 10^4
s[i] is '(', or ')'.
'''

class Solution:
  def longestValidParentheses(self, s: str) -> int:
    stack = []
    long, length = 0, 0
    start = 0

    for i, c in enumerate(s):
      if c == '(':
        stack.append(i)
        continue

      j = start
      if stack:
        stack.pop()
        if stack:
          j = stack[-1] + 1
          
        length = i - j + 1
      
      #new start
      else: 
        length = i - j
        start = i + 1

      long = max(long, length)

    return long
    

  def longestValidParentheses0(self, s: str) -> int:
    if not s:
      return 0
    
    stack, prev = [], []
    long = 0
    last = None
    
    for i, ch in enumerate(s):
      if ch == '(':
        stack.append(i)
        continue
      
      if not stack:
        continue
        
      j = stack.pop()
      
      # init range
      if not last:
        last = [j, i]
        
      # expand both sides
      elif j == last[0]-1 and i == last[1]+1:
        last[0] -= 1
        last[1] += 1
        
      # expand right side
      elif j == last[1]+1:
        last[1] = i
      
      # reset to new range
      else:
        prev.append(last)
        last = [j, i]
        
      # print(i, j, last, prev)
      if last and prev and prev[-1][1]+1 == last[0]:
        l, _ = prev.pop()
        last[0] = l
      
      if last:
        long = max(long, last[1]-last[0]+1)
    
    return long
    