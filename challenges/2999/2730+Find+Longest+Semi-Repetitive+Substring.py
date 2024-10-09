class Solution:
  def longestSemiRepetitiveSubstring(self, s: str) -> int:
    stack = []
    n = len(s)
    
    for i in range(1, n):
      if s[i] == s[i-1]:
        if stack and stack[-1][1] == i-1:
          stack[-1][1] = i
        else:
          stack.append([i-1, i])
    
    # print('done:', stack)
    if not stack:
      return n
    
    l0 = stack[0][0] + 2
    l1 = n - stack[-1][1] + 1
    long = max(l0, l1)
    m = len(stack)
    # print('ends:', l0, l1)
      
    for i in range(m):
      l, r = stack[i]
      if r-l == 1:
        head = stack[i-1][1] if i > 0 else 0
        tail = stack[i+1][0] if i < m-1 else n-1
        long = max(long, tail-head+1)
      
      elif i > 0:
        head = stack[i-1][1]
        tail = l+1
        long = max(long, tail-head+1)
    
    return long