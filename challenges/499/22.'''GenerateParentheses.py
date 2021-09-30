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
  