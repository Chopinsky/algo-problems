'''
You are given an integer array cards of length 4. You have four cards, each containing a number in the range [1, 9]. You should arrange the numbers on these cards in a mathematical expression using the operators ['+', '-', '*', '/'] and the parentheses '(' and ')' to get the value 24.

You are restricted with the following rules:

The division operator '/' represents real division, not integer division.
For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.
For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not allowed.
You cannot concatenate numbers together
For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.
Return true if you can get such expression that evaluates to 24, and false otherwise.

Example 1:

Input: cards = [4,1,8,7]
Output: true
Explanation: (8-4) * (7-1) = 24

Example 2:

Input: cards = [1,2,1,2]
Output: false

Constraints:

cards.length == 4
1 <= cards[i] <= 9
'''


from functools import lru_cache
from typing import List, Tuple, Set
from collections import defaultdict



class Solution:
  def judgePoint24(self, cards: List[int]) -> bool:
    nums = [(val, 1) for val in cards]
    duals = {}
    
    @lru_cache(None)
    def get_list(a: Tuple[int, int], b: Tuple[int, int]) -> Set[Tuple[int, int]]:
      res = set()
      au, ad = a
      bu, bd = b
      
      # plus
      res.add((au*bd + ad*bu, ad*bd))
      
      # minus
      res.add((au*bd - ad*bu, ad*bd)) # a-b
      res.add((ad*bu - au*bd, ad*bd)) # b-a
        
      # times
      res.add((au*bu, ad*bd))
      
      # div
      if au and bd:
        res.add((ad*bu, au*bd))
        
      if ad and bu:
        res.add((au*bd, ad*bu))
      
      return res
      
    for i in range(3):
      for j in range(i+1, 4):
        if cards[i] <= cards[j]:
          a, b = nums[i], nums[j]
        else:
          a, b = nums[j], nums[i]
          
        duals[1<<i | 1<<j] = get_list(a, b)
    
    # print(duals)
    keys = list(duals)
    n = len(keys)
    
    # case 1: duals interact with duals
    for i in range(n-1):
      for j in range(i+1, n):
        ki, kj = keys[i], keys[j]
        if ki & kj > 0:
          continue
        
        for vi in duals[ki]:
          for vj in duals[kj]:
            if vi[0]/vi[1] > vj[0]/vj[1]:
              a, b = vj, vi
            else:
              a, b = vi, vj
              
            for u, d in get_list(a, b):
              if u % d == 0 and u // d == 24:
                # print('duals')
                return True
    
    # print('d', duals[3])
    
    # case 2: 1 interact 1 with duals
    triples = defaultdict(set)
    for key, lst in duals.items():
      for i in range(4):
        if 1<<i & key > 0:
          continue
          
        for val in lst:
          if nums[i][0]/nums[i][1] > val[0]/val[1]:
            a, b = val, nums[i]
          else:
            a, b = nums[i], val
            
          triples[1<<i | key] |= get_list(a, b)
        
    # print('t', triples[7])
        
    for key, lst in triples.items():
      for i in range(4):
        if 1<<i & key > 0:
          continue
          
        for val in lst:            
          if nums[i][0]/nums[i][1] > val[0]/val[1]:
            a, b = val, nums[i]
          else:
            a, b = nums[i], val
            
          for u, d in get_list(a, b):
            if u % d == 0 and u // d == 24:
              # print('all', format(key, '#04b'), i, a, b, u, d)
              return True
          
    return False
        