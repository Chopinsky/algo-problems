'''
2696. Minimum String Length After Removing Substrings
'''

class Solution:
  def minLength(self, s: str) -> int:
    stack = []
    
    for ch in s:
      if ch == 'D' and stack and stack[-1] == 'C':
        stack.pop()
        continue
        
      if ch == 'B' and stack and stack[-1] == 'A':
        stack.pop()
        continue
        
      stack.append(ch)
    
    return len(stack)
        