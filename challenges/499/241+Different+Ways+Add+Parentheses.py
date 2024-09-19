'''
241. Different Ways to Add Parentheses
'''

from typing import List
from functools import lru_cache

class Solution:
  def diffWaysToCompute(self, expression: str) -> List[int]:
    s = ""
    stack = []
    ans = []
    
    for ch in expression:
      if ch == '+' or ch == '-' or ch == '*':
        stack.append(int(s))
        stack.append(ch)
        s = ""
      else:
        s += ch
        
    if s:
      stack.append(int(s))
      
    # print(stack)
    
    def calc(x: int, y: int, op: str):
      if op == '+':
        return x+y
      
      if op == '-':
        return x-y
      
      return x*y
    
    @lru_cache(None)
    def dp(i: int, j: int) -> List:
      if i == j:
        return [stack[i]]
      
      res = []
      for k in range(i+1, j+1, 2):
        lv = dp(i, k-1)
        rv = dp(k+1, j)
        
        for v0 in lv:
          for v1 in rv:
            res.append(calc(v0, v1, stack[k]))
        
      return tuple(res)
      
    return dp(0, len(stack)-1)
        