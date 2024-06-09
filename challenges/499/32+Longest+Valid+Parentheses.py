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

Test cases:

"(()"
")()())"
""
"()"
"()(())"
"(()())"
"((()))())"
"(())()(()(("
"()(((()(()))))"
'''

class Solution:
  def longestValidParentheses(self, s: str) -> int:
    stack = []
    long = 0
    n = len(s)
    
    def expand(l: int, r: int):
      # expand the valid range to [l, r]
      while l-1 >= 0 and r+1 < n and s[l-1] == '(' and s[r+1] == ')':
        l -= 1
        r += 1
      
      # can merge
      while stack and stack[-1][1] == l-1:
        l, _ = stack.pop()
        
      if l > 0 and r < n-1 and s[l-1] == '(' and s[r+1] == ')':
        l, r = expand(l, r)
      
      return (l, r)
    
    i = 0
    while i < n:
      ch = s[i]
      if ch == '(' or i == 0 or s[i-1] != '(':
        i += 1
        continue
        
      l, r = expand(i-1, i)
      stack.append((l, r))
      long = max(long, r-l+1)
      
      # quick shift
      i = max(i, r)
      i += 1
    
    return long
  
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
    