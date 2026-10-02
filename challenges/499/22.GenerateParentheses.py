'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

Constraints:

1 <= n <= 8
'''

import functools
from typing import List
from itertools import combinations

class Solution:
  def generateParenthesis(self, n: int) -> list[str]:
    @functools.cache
    def dp(n: int) -> tuple:
      if n == 1:
        return tuple(["()"])

      if n <= 0:
        return tuple([""])

      res = set()

      for i in range(1, n):
        for p0 in dp(i):
          if n-i > i:
            break

          for p1 in dp(n-i):
            res.add(p0+p1)
            res.add(p1+p0)

            if p0:
              res.add(p0[0] + p1 + p0[1:])
              res.add(p0[:-1] + p1 + p0[-1])

            if p1:
              res.add(p1[0] + p0 + p1[1:])
              res.add(p1[:-1] + p0 + p1[-1])

      return tuple(res)

    return sorted(dp(n))

  def generateParenthesis(self, n: int) -> List[str]:
    @functools.cache
    def generate(num: int) -> List[str]:
      if num == 0:
        return ['']
      
      if num == 1:
        return ['()']
    
      ans = []
      
      for i in range(num):
        for l in generate(i):
          for r in generate(num-1-i):
            ans.append('(' + l + ')' + r)
            
      return ans
    
    return generate(n)
    
  
  def generateParenthesis0(self, n: int) -> List[str]:
    if n == 1:
      return ['()']
    
    ans = []
    def build(idx: List[int]):
      s = '('
      j = 0
      
      for i in range(1, 2*n):
        if j < n-1 and i == idx[j]:
          j += 1
          s += '('
        else:
          s += ')'
        
      ans.append(s)
      return
    
    indices = [i for i in range(1, 2*n-1)]
    
    for idx in combinations(indices, n-1):
      found = True
      idx = list(idx)
      
      for j, pos in enumerate(idx):
        if 2*j + 3 <= pos:
          found = False
          break
      
      if found:
        build(idx)
    
    return ans
  